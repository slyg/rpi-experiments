start:
	docker build -t slyg/mqtt-python-pir-detector .
	docker run \
		-d \
		--rm \
		--privileged \
		--name mqtt-python-pir-detector \
		-v /lib/modules:/lib/modules \
		-v $(CURDIR):/www \
		slyg/mqtt-python-pir-detector

stop:
	docker stop -t 2000 mqtt-python-pir-detector

.DEFAULT_GOAL := start
.PHONY: default stop
