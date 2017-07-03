FROM resin/raspberrypi3-node

ENV WORKDIR /usr/src/app/
ENV INITSYSTEM on

WORKDIR $WORKDIR

# Install pigpio
RUN apt-get update \
 && apt-get install --no-install-recommends make unzip \
 && wget abyz.co.uk/rpi/pigpio/pigpio.zip \
 && unzip pigpio.zip \
 && cd PIGPIO \
 && make \
 && sudo make install

COPY package.json $WORKDIR/package.json

RUN npm install

COPY app.js start.sh $WORKDIR/

ENTRYPOINT npm start
