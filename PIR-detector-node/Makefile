start:
	docker build -t slyg/pir-detector .
	docker run \
		-it \
		--cap-add=ALL \
		--name pir-detector \
		--privileged \
		--rm \
		-v /lib/modules:/lib/modules \
		-u root \
		slyg/pir-detector

stop:
	docker stop pir-detector

.DEFAULT_GOAL = start
.PHONY = default stop
