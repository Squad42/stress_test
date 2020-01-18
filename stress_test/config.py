import os



# CONFIG SERVER
if "CONSUL_HOST" in os.environ:
	CONFIG_HOST = os.environ["CONSUL_HOST"]
else:
    CONFIG_HOST = "localhost"
if "CONSUL_PORT" in os.environ:
	CONFIG_PORT = os.environ["CONSUL_PORT"]
else:
    CONFIG_PORT = 8500


if "HOST_IMAGEUPLOAD" in os.environ:
	HOST_IMAGEUPLOAD = os.environ["HOST_IMAGEUPLOAD"]
else:
    HOST_IMAGEUPLOAD = "image-upload-service"
if "PORT_IMAGEUPLOAD" in os.environ:
	PORT_IMAGEUPLOAD = os.environ["PORT_IMAGEUPLOAD"]
else:
    PORT_IMAGEUPLOAD = 5000  
if "ENDPOINTS_IMAGEUPLOAD" in os.environ:
	ENDPOINTS_IMAGEUPLOAD = os.environ["ENDPOINTS_IMAGEUPLOAD"]
else:
    ENDPOINTS_IMAGEUPLOAD = "/;/landing_page;"   
    


if "HOST_IMAGECATALOGUE" in os.environ:
	HOST_IMAGECATALOGUE = os.environ["HOST_IMAGECATALOGUE"]
else:
    HOST_IMAGECATALOGUE = "image-upload-service"
if "PORT_IMAGECATALOGUE" in os.environ:
	PORT_IMAGECATALOGUE = os.environ["PORT_IMAGECATALOGUE"]
else:
    PORT_IMAGECATALOGUE = 5000 #5001  
if "ENDPOINTS_IMAGECATALOGUE" in os.environ:
	ENDPOINTS_IMAGECATALOGUE = os.environ["ENDPOINTS_IMAGECATALOGUE"]
else:
    ENDPOINTS_IMAGECATALOGUE = "/" 


    