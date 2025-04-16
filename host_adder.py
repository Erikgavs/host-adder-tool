# SCRIPT DISEÑADO CON EL OBJETIVO DE AÑADIR IP'S A LA CARPETA DE HOSTS DEL SISTEMA DE UNA MANERA FÁCIL Y RÁPIDA
# TENDREMOS QUE EJECUTAR EL SCRIPT CON EL COMANDO SUDO
# <USO> sudo python3 host_adder.py

import os 
import subprocess
import sys

if os.getuid() !=0:
    print("El script debe ejecutarse con sudo")
    sys.exit(1)

ips = input("Específica la ip que añadir a los hosts: ")
dom = input("Específica el dominio que añadir con la ip: ")
ip_dom = f"{ips} {dom}"
 
print(f"Añadiendo la ip y el dominio a /etc/hosts: {ip_dom}")
subprocess.run (f'echo "{ip_dom}" | tee -a /etc/hosts', shell=True) 