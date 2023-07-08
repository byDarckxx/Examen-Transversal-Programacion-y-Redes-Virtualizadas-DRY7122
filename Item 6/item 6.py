import requests
import netmiko
import json
from netmiko import ConnectHandler

#Equipo csr1000v
csr1000v = { "ip": "192.168.56.3",
"device_type": "cisco_ios",
"username": "cisco",
"password": "cisco123!",
}


 # Respaldo del comando SHOW.
def running_config():
    command = "show run"
    with ConnectHandler(**csr1000v) as net_connect:
        output = net_connect.send_command(command)

    #Guardar la configuración.
    with open('Show_Run_CSR1000V.txt', 'w') as f:
        f.write(output)

    # Automatically cleans-up the output so that only the show output is returned
    print()
    print(output)
    print()


 # Respaldo del comando SHOW-IP-INTERFACE-BRIEF.
def ip_int_brief():
    # Respaldo del comando SHOW.
    command = "show ip int brief"
    with ConnectHandler(**csr1000v) as net_connect:
        output = net_connect.send_command(command)

    #Guardar la configuración.
    with open('Show_Ip_Int_Brief_CSR1000V.txt', 'w') as f:
        f.write(output)

    # Automatically cleans-up the output so that only the show output is returned
    print()
    print(output)
    print()

# Respaldo del comando SHOW version
def version():
    command = "show version"
    with ConnectHandler(**csr1000v) as net_connect:
        output = net_connect.send_command(command)

    #Guardar la configuración.
    with open('Show_Version_CSR1000V.txt', 'w') as f:
        f.write(output)

    # Automatically cleans-up the output so that only the show output is returned
    print()
    print(output)
    print()


#Menú redundante para que sea mas intuitivo
while True:
    op1=int(input('Bienvenido al Script de Respaldo, ¿Qué acción desea realizar?\n1.- Respaldo de IP y estado de interfaces.\n2.- Respaldo de Running-confing.\n3.- Respaldo de show version.\n\n9.- Salir\n\nOpción: '))
    if op1 == 1:
        ip_int_brief()
    elif op1 == 2:
        running_config()
    elif op1 == 3:
        version()
    elif op1 == 9:
        break
    else:
        print("Opción Incorrecta")