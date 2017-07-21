.MODULE_NAME := relay-module-python
.DEFAULT_GOAL := start

start:
	docker build -t slyg/$(.MODULE_NAME) .
	docker run \
		-it \
		--rm \
		--privileged \
		--name $(.MODULE_NAME) \
		-v $(CURDIR):/www \
		slyg/$(.MODULE_NAME) python3 relay.py

stop:
	docker stop -t 2000 $(.MODULE_NAME)

.PHONY: start stop
