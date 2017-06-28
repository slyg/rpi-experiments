FROM resin/raspberry-pi-alpine-node

ENV WORKDIR /usr/src/app/
ENV INITSYSTEM on

WORKDIR $WORKDIR

COPY package.json $WORKDIR/package.json

RUN npm install

COPY app.js $WORKDIR/app.js

ENTRYPOINT npm start
