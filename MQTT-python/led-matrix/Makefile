start:
	docker build -t slyg/mqtt-python-led-matrix .
	docker run \
		-it \
		-d \
		--rm \
		--net=host \
		--privileged \
		--cap-add=ALL \
		--device=/dev/loop-control:/dev/loop-control \
		--device=/dev/loop0:/dev/loop0 \
		-v /lib/modules:/lib/modules \
		-v $(CURDIR):/www \
		--name mqtt-python-led-matrix \
		-p 1883:1883 \
		slyg/mqtt-python-led-matrix

stop:
	docker stop -t 2000 mqtt-python-led-matrix

.DEFAULT_GOAL := start
.PHONY: default stop
