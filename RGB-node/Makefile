start:
	docker build -t slyg/rgb-node .
	docker run \
		-it \
		--cap-add=ALL \
		--name rgb-node \
		--privileged \
		--rm \
		-v /lib/modules:/lib/modules \
		-u root \
		slyg/rgb-node

stop:
	docker stop rgb-node

.DEFAULT_GOAL = start
.PHONY = default stop
