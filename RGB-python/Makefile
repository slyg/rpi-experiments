start:
	docker build -t slyg/rgb-python .
	docker run \
		-it \
		--rm \
		-d \
		--privileged \
		--name rainbow \
		slyg/rgb-python

stop:
	docker stop -t 2000 rainbow

.DEFAULT_GOAL := start
.PHONY: default stop
