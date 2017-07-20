FROM resin/raspberrypi3-python:3.6.1

ENV INITSYSTEM on

WORKDIR /www

RUN apt-get update \
 && apt-get install --no-install-recommends make unzip \
 && wget abyz.co.uk/rpi/pigpio/pigpio.zip \
 && unzip pigpio.zip \
 && cd PIGPIO \
 && make \
 && sudo make install

RUN pip install \
      rpi.gpio \
      paho-mqtt

ENTRYPOINT python3 detect-motion.py
