push-01:
	rsync -a ./ pi@rpi-01:raspberry-pi-experiments

push-02:
	rsync -a ./ pi@rpi-02:raspberry-pi-experiments

push-03:
	rsync -a ./ pi@rpi-03:raspberry-pi-experiments

.PHONY: push-01 push-02 push-03
