default:
	docker build -t blink .
	docker run \
		-it \
		--rm \
		-d \
		--privileged \
		--name led-blink \
		blink

stop:
	docker stop led-blink
	docker rm led-blink
