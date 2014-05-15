#!/bin/env python

import time
import datetime
import subprocess
import serial

def get_temp():
        output = subprocess.check_output("cat /sys/bus/iio/devices/iio:device0/in_voltage0_raw", shell=True)
        voltage = (float(output)*1.8)/4096.0
        temperature = (voltage*100)
        temperature = "{:3.4f}".format(temperature)
        return str(temperature)

def check_serial(sample):
        byte = ser.read()
        if byte == "1":
                print "\nUltimo valor:"
                print sample
        elif byte == "2":
                print "\nOs valores armazenados sao:"
                file.seek(0, 0)
                for line in file:
                        print line,
        elif len(byte) != 0:
                print "\nComando invalido!"

def get_date():
        return str(datetime.datetime.now())

def store_sample(sample):
        file.seek(0, 2)
        file.write(sample + '\n')

if __name__ == "__main__":
        ser = serial.Serial('/dev/ttyO4', 115200, timeout=0.01)
        file = open('log.txt', 'w+')
        while True:
                temp = get_temp()
                date = get_date()
                sample = "Temp = " + temp + " -> Date = " + date
                store_sample(sample)
                check_serial(sample)
                time.sleep(1)
