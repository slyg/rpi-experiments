blink:
	cd blink && make

blink-stop:
	cd blink && make stop

push:
	rsync -a ./ pi@raspberrypi:raspberry-pi-experiments

.PHONY = blink blink-stop push
