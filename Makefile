push:
	rsync -a ./ pi@raspberrypi:raspberry-pi-experiments

push-zero:
		rsync -a ./ pi@raspberrypizero:raspberry-pi-experiments

.PHONY= push push-zero
