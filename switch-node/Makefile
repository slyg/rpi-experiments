start:
	docker build -t slyg/switch-node .
	docker run \
		-it \
		--cap-add=ALL \
		--name switch-node \
		--privileged \
		--rm \
		-v /lib/modules:/lib/modules \
		-u root \
		slyg/switch-node

stop:
	docker stop switch-node

.DEFAULT_GOAL = start
.PHONY = default stop
