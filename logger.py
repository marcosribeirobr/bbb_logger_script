#!/bin/env python

import time
import datetime
import subprocess
import serial

def get_temp():
        # le o valor do A/D
        output = subprocess.check_output("cat /sys/bus/iio/devices/iio:device0/in_voltage0_raw", shell=True)
        # Converte para tensao
        voltage = (float(output)*1.8)/4096.0
        # Converte para temperatura
        temperature = (voltage*100)
        # Formata a casas decimais
        temperature = "{:3.4f}".format(temperature)
        # Converte para string e retorna a temperatura
        return str(temperature)

def check_serial(sample):
        # Le a serial
        byte = ser.read()
        if byte == "1":
                # Apresenta o ultimo amostra
                ser.write("\n\rUltimo valor:\n\r");
                ser.write("\r"+sample+"\n\r")
        elif byte == "2":
                # Apresenta todas amostras armazenadas no log
                ser.write("\n\rOs valores armazenados sao:"+"\n\r")
                # Aponta para o comeco do arquivo
                file.seek(0, 0)
                # Faz varredura das linhas imprimindo
                for line in file:
                        ser.write("\r"+line+"\r")
        elif byte == "3":
                # Sair do script
                ser.write("\n\rSaindo..."+"\n\r")
                file.close()
                exit()
        elif len(byte) != 0:
                # Verifica se chegou comando invalido
                ser.write("\n\rComando invalido!"+"\n\r")

def get_date():
        # Verifica a data atual
        return str(datetime.datetime.now())

def store_sample(sample):
        # Aponta para o final do arquivo
        file.seek(0, 2)
        # Armazena a amostra
        file.write(sample + '\n')

        #main
if __name__ == "__main__":
        # Inicializa a serial 115200 @ tty04
        ser = serial.Serial('/dev/ttyO4', 115200, timeout=0.01)
        # Abre arquivo de log
        file = open('log.txt', 'w+')
        while True:
                temp = get_temp()
                date = get_date()
                sample = "Temp = " + temp + " -> Date = " + date
                store_sample(sample)
                check_serial(sample)
                time.sleep(1)
