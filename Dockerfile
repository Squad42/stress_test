FROM python:3.6.8-alpine

LABEL Squad42 project: stress test

COPY stress_test/ /stress_test
COPY requirements.txt /stress_test/
WORKDIR /stress_test/

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt

CMD ["python3","-u","__main__.py"]

