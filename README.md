# host-adder-tool
host_adder es un pequeño script que tiene como objetivo automatizar la tarea de asignar una ip a un dominio en la carpetanas a/etc/hosts, el script nos pedirá la ip y el dominio y lo escribirá en la carpeta de los hosts

## Guía de host_adder.py y host_adder.sh
Para que este script funcione tendremos que ejecutarlo como sudo, si no lo hacemos no nos dejará escribir en la carpeta /etc/hosts

Este script está diseñado con la finalidad de implementarlo en CTF'S, Máquinas de hack the box y en cualquier situación que necesitemos asignar una ip a un dominio

---


### Uso de host_adder.py
para usar host_adder.py tendremos que tener instalado python3 en nuestra máquina
```
python3 host_adder.py
```
### Uso de host_adder.sh
Para usarlo tendremos que asignarle permisos de ejecucción
```
chmod +x host_adder.sh
./host.adder.sh
```

