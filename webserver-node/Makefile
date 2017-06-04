start:
	docker build -t slyg/webserver-node .
	docker run \
		-it \
		-d \
		-p 3000:3000 \
		--name webserver-node \
		--privileged \
		--rm \
		slyg/webserver-node

stop:
	docker stop webserver-node

.DEFAULT_GOAL = start
.PHONY = default stop
