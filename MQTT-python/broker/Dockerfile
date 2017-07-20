FROM resin/raspberrypi3-alpine

RUN apk add --update \
      mosquitto \
      mosquitto-clients \
 && rm -rf /var/cache/apk/*

EXPOSE 1883

ENTRYPOINT mosquitto
