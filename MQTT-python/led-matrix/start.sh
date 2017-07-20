#!/usr/bin/env bash
modprobe i2c-dev

python3 motion-status.py
