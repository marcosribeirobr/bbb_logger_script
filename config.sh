#!/bin/bash

echo BB-ADC > /sys/devices/bone_capemgr.*/slots
echo BB-UART4 > /sys/devices/bone_capemgr.*/slots
python logger.py
