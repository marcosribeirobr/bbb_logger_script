#!/bin/bash

echo ""
echo "Sistemas Operacionais I: Linux"
echo "Marcos Ribeiro"
echo "Gustavo Grossklauss Neto"
echo ""
echo "            Logger de temperatura."
echo ""
echo "Configurando perifericos..."
# Adiciona periferico AD
echo BB-ADC > /sys/devices/bone_capemgr.*/slots
# Adiciona periferico UART
echo BB-UART4 > /sys/devices/bone_capemgr.*/slots
echo "Perifericos configurados..."
echo ""
echo "Deseja configurar data e hora? (sim/nao)"
case $selection in
        "sim" )
                echo "Entre com o data (YYYY-MM-DD):"
                read data
                # Armazena a data informada em date (-s seta)
                date -s $data
                echo "Entre com a hora (HH:MM:SS):"
                read hora
                # Armazena a hora informada em data
                date -s $hora
                break
                ;;
        "nao" ) break ;;
        * ) echo "Entrada invalida."
esac
done
echo ""
echo "Chamando script Python..."
echo ""
echo "            MENU SERIAL:"
echo "1 - Faz Leitura atual."
echo "2 - Envia o log pela serial."
echo "3 - Encerra script Python."
echo ""
# Chama script python
python logger.py
echo "Script Python finalizado"
echo ""
echo "Saindo..."
echo ""
