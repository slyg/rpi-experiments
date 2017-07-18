FROM resin/raspberrypi3-python:3.6.1

ENV INITSYSTEM on

RUN pip install rpi.gpio

COPY . .

CMD python3 rainbow.py
