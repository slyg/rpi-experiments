start:
	docker build -t slyg/4-relay-module .
	docker run \
		-it \
		--cap-add=ALL \
		--name 4-relay-module \
		--privileged \
		--rm \
		-v /lib/modules:/lib/modules \
		-u root \
		slyg/4-relay-module

stop:
	docker stop 4-relay-module

.DEFAULT_GOAL = start
.PHONY = default stop
