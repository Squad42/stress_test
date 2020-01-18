import config
import consul
import time
import urllib.request


CONSUL_SERVER=None

while CONSUL_SERVER is None:
    try:
        CONSUL_SERVER = consul.Consul(host=config.CONFIG_HOST,
                                      port=config.CONFIG_PORT)
    except:
        CONSUL_SERVER = None
        print("Not able to connect to Consul server")
        time.sleep(3)
       
stress=False        
while True:      
    index = None
    try:
        index, data = CONSUL_SERVER.kv.get("stress_test", index=index)
    except:
        print("Consul connection error!")
        time.sleep(3)
        continue
    if data is not None:
        if "true" in str(data["Value"]).lower():
            stress=True
            print("Stress test ON!!")
        else:
            stress=False 
            print("Stress test OFF")
    else:
        stress=False 
        print("Stress test OFF")
        
    if not stress:
        time.sleep(10)  
    else:
        for i in range(10000):
            for path in config.ENDPOINTS_IMAGEUPLOAD.split(";"):
                try:
                    contents = urllib.request.urlopen("http://{}:{}{}".format(config.HOST_IMAGEUPLOAD,
                                                                      config.PORT_IMAGEUPLOAD,
                                                                      path)).read()
                except:
                    print("Problem with http request to http://{}:{}{}".format(config.HOST_IMAGEUPLOAD,
                                                                      config.PORT_IMAGEUPLOAD,
                                                                      path))
                    time.sleep(1)
                    break
            
            for path in config.ENDPOINTS_IMAGECATALOGUE.split(";"):
                try:
                    contents = urllib.request.urlopen("http://{}:{}{}".format(config.HOST_IMAGECATALOGUE,
                                                                      config.PORT_IMAGECATALOGUE,
                                                                      path)).read()
                except:
                    print("Problem with http request to http://{}:{}{}".format(config.HOST_IMAGEUPLOAD,
                                                                      config.PORT_IMAGEUPLOAD,
                                                                      path))
                    time.sleep(1)
                    break    
