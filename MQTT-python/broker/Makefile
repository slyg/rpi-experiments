start:
	docker build -t slyg/mqtt-broker .
	docker run \
		-d \
		--cap-add=ALL \
		--name mqtt-broker \
		--privileged \
		--rm \
		-v /lib/modules:/lib/modules \
		-u root \
		-p 1883:1883 \
		slyg/mqtt-broker

stop:
	docker stop mqtt-broker

.DEFAULT_GOAL := start
.PHONY: default stop
