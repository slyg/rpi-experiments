push:
	rsync -a ./ pi@rpi-01:raspberry-pi-experiments

push-zero:
	rsync -a ./ pi@rpi-02:raspberry-pi-experiments

.PHONY= push push-zero
