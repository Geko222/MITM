#!/bin/bash
cat bannerinstall.txt

sleep 2s

sudo apt install -y bettercap
sudo apt install -y apache2

if command -v bettercap &> /dev/null; then
    echo -e "\e[1;32mBettercap está instalado correctamente\e[0m"
else
    echo -e "\e[1;31mBettercap no se pudo isntalar\e[0m"
fi

if command -v apache2 &> /dev/null; then
    echo -e "\e[1;32mApache2 está instalado correctamente\e[0m"
else
    echo -e "\e[1;31mApache2 no se pudo isntalar\e[0m"
fi
