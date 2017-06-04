start:
	docker build -t slyg/blink-node .
	docker run \
		-d \
		-it \
		--cap-add=ALL \
		--name blink-node \
		--privileged \
		--rm \
		-v /lib/modules:/lib/modules \
		-u root \
		slyg/blink-node

stop:
	docker stop blink-node

.DEFAULT_GOAL = start
.PHONY = default stop
