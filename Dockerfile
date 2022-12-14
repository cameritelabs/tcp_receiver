FROM python:3.9.7-slim-buster

COPY . /root/tcp_receiver

RUN apt update

WORKDIR /root/tcp_receiver

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 9950


CMD ["/usr/local/bin/python", "-u", "tcp_receiver.py"]
