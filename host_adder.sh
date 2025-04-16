# SCRIPT DISEÑADO CON EL OBJETIVO DE AÑADIR IP'S A LA CARPETA DE HOSTS DEL SISTEMA DE UNA MANERA FÁCIL Y RÁPIDA
# TENDREMOS QUE EJECUTAR EL SCRIPT CON EL COMANDO SUDO
# <USO> chmod +x host_adder.sh
# <USO> ./host_adder.sh

if [ "$EUID" -ne 0 ]; then
    echo "Este script se tiene que ejecutar con sudo"
    exit 1
fi

read -p "Específica la IP que quieres añadir a hosts" ip
read -p "Específica el dominio para la IP que has específicado antes" dominio

ip_dom="$ip $dominio"
echo "Añadiendo ip y dominio a /etc/hosts: $ip_dom"

echo "$ip_dom" | sudo tee -a /etc/hosts > /dev/null