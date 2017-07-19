start:
	docker build -t slyg/rgb-python .
	docker run \
		-it \
		--rm \
		--privileged \
		--name rainbow \
		-v $(CURDIR):/www \
		slyg/rgb-python

stop:
	docker stop -t 2000 rainbow

.DEFAULT_GOAL := start
.PHONY: default stop
