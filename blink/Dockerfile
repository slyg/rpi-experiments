FROM resin/rpi-raspbian:latest

RUN apt-get -q update \
 && apt-get -qy install \
    python \
    python-pip \
    python-dev \
    python-pip \
    gcc \
    make

RUN pip install rpi.gpio atexit

COPY ./blink.py ./blink.py

CMD python blink.py
