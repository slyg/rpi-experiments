start:
	docker build -t slyg/pir-detector-python .
	docker run \
		-it \
		--rm \
		--privileged \
		--name pir-detector-python \
		-v $(CURDIR):/www \
		slyg/pir-detector-python

stop:
	docker stop -t 2000 pir-detector-python

.DEFAULT_GOAL := start
.PHONY: default stop
