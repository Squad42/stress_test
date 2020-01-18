import config
import consul
import time
import urllib.request
import sys


CONSUL_SERVER=None
print("APP START")
while CONSUL_SERVER is None:
    try:
        print("Creating consul connection to {}:{}..".format(config.CONFIG_HOST,config.CONFIG_PORT))
        CONSUL_SERVER = consul.Consul(host=config.CONFIG_HOST,
                                      port=int(config.CONFIG_PORT))
    except:
        CONSUL_SERVER = None
        print("Not able to connect to Consul server")
        time.sleep(3)
sys.stdout.flush()       
stress=False        
while True:
      
    index = None
    print("Reading stress_test key from consul server..")
    sys.stdout.flush()
    index, data = CONSUL_SERVER.kv.get("stress_test", index=index)
    print("stress_test value successfully read from consul server..")
    sys.stdout.flush()
    '''
    try:
        print("Reading stress_test key from consul server..")
        index, data = CONSUL_SERVER.kv.get("stress_test", index=index)
        print("stress_test value successfully read from consul server..")
    except:
        print("Consul connection error!")
        time.sleep(3)
        continue
    '''    
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
    sys.stdout.flush()    
    if not stress:
        time.sleep(10)  
    else:
        for path in config.ENDPOINTS_IMAGEUPLOAD.split(";"):
            for i in range(1000):
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
        sys.stdout.flush()
        for path in config.ENDPOINTS_IMAGECATALOGUE.split(";"):
            for i in range(1000):
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
        sys.stdout.flush()                
