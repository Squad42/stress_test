FROM python:3.6.8-alpine

LABEL Squad42 project: stress test

COPY stress_test/ /stress_test
COPY requirements.txt /stress_test/
WORKDIR /stress_test/

ENV CONSUL_HOST "35.190.207.89"
ENV CONSUL_PORT "80"
ENV HOST_IMAGECATALOGUE 35.233.116.57
ENV HOST_IMAGEUPLOAD 35.233.116.57

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt

CMD ["python3","__main__.py"]

