#AUTOR: KEYTEL PUMAYLLE RAMIREZ 
#Librerias
import socket
import ftplib
from os import system
from time import sleep

#Detalles del servidor
hostname = socket.gethostname()
ip_servidor = socket.gethostbyname(hostname)
print("http://<ip_servidor>/<puerto>/archivo_descargar>")
print("Ip_servidor: "+ip_servidor)

#Direccionandonos al directorio del archivo
print("Ingrese el disco (C:, G:, E:, ...): ")
letra_disco = str(input())

print("Ingrese la ruta de la carpeta: ")
ruta_archivo = input()




#Levantando servidor
print("IDesea levantar el servidor: ")
condicion = input()

if condicion == 's':
    print("Levantando servidor...")
    system(letra_disco)
    sleep(1)
    system("cd "+ ruta_archivo)
    sleep(5)
    system("python -m http.server")
else:
    print("Servidor caido")