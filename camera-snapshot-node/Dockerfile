FROM resin/raspberry-pi-alpine-node

ENV WORKDIR /usr/src/app/
ENV INITSYSTEM on

WORKDIR $WORKDIR

COPY package.json $WORKDIR/package.json

RUN npm install

RUN mkdir -p /opt/vc/bin
COPY opt_vc /opt/vc

RUN ls -l /opt/vc/

ENV PATH $PATH:/opt/vc/bin

COPY app.js $WORKDIR/app.js

ENTRYPOINT npm start
