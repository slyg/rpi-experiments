FROM resin/raspberrypi3-node

ENV WORKDIR /usr/src/app/
ENV INITSYSTEM on

WORKDIR $WORKDIR

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
     python \
     python-dev \
     python-pip \
     gcc \
     make \
     pigpio \
  && rm -rf /var/lib/apt/lists/*

COPY package.json $WORKDIR/package.json

RUN npm --unsafe-perm install

COPY index.js $WORKDIR/index.js

ENTRYPOINT modprobe i2c-dev && npm start
