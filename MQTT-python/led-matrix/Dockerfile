FROM resin/raspberrypi3-debian:jessie-20161130

WORKDIR /usr/src/app
ENV INITSYSTEM on

RUN apt-get update && \
    apt-get install -yq --no-install-recommends \
      python3 \
      sense-hat \
      raspberrypi-bootloader \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# To install vcgencmd
ENV USERLANDVER 771a9aa7155442615bbe4cd6cf87b29b90cd228a
RUN apt-get update && \
    apt-get install -yq --no-install-recommends \
      build-essential cmake git \
    && git clone https://github.com/raspberrypi/userland.git && \
    cd userland && \
    git checkout -b build ${USERLANDVER} && \
    bash ./buildme && \
    cd .. && \
    rm -rf userland && \
    apt-get remove \
      build-essential cmake git \
    && apt-get autoremove && apt-get clean && rm -rf /var/lib/apt/lists/*

# Build extra library requirements
RUN apt-get update && \
    apt-get install -yq --no-install-recommends \
      build-essential libssl-dev libffi-dev libyaml-dev python3-dev python3-pip \
 && pip3 install \
      rpi.gpio \
      paho-mqtt \
 && apt-get remove \
      build-essential libssl-dev libffi-dev libyaml-dev python3-dev python3-pip \
 && apt-get autoremove \
 && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY . .
COPY start.sh ./

CMD ./start.sh
