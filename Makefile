push:
	rsync -a ./ pi@rpi-01:raspberry-pi-experiments

push-zero:
	rsync -a ./ pi@raspberrypizero:raspberry-pi-experiments

.PHONY= push push-zero
