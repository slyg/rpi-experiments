push:
	rsync -a ./ pi@raspberrypi:raspberry-pi-experiments

.PHONY= push
