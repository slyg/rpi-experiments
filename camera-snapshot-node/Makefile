start:
	cp -r /opt/vc ./opt_vc
	docker build -t slyg/camera-snapshot-node .
	docker run \
		-it \
		-d \
		-p 3000:3000 \
		--name camera-snapshot-node \
		--privileged \
		--device=/dev/vchiq \
		--device=/dev/vcsm \
		--rm \
		slyg/camera-snapshot-node

stop:
	docker stop camera-snapshot-node

.DEFAULT_GOAL = start
.PHONY = start stop
