#!/bin/bash

raspivid -o - \
  -t 0 \
  -w 640 \
  -h 480 \
  -fps 20 | cvlc -vvv stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=:8160}' :demux=h264

# then open http://<rpi>:8160 in VLC
