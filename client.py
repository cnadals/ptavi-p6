#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente que abre un socket a un servidor
"""
import sys
import socket

# Cliente UDP simple.

# Dirección IP del servidor.
metodo = sys.argv[1]
direccion = sys.argv[2]
port = int(direccion.split(':')[-1])
direccion = direccion.split(':')[0]
print(metodo)
print(port)
print(direccion)

#EXCEPCION ESTAN BIEN/NO LOS ARGUMENTOS
if not len(sys.argv) == 3:
    sys.exit("Usage: python3 client.py method receiver@IP:SIPport")
_, metodo, direccion = sys.argv

if metodo == 'INVITE':
	line = metodo + ' sip:' + direccion + ' SIP/2.0'
	print("Enviando: " + line)
if metodo == 'BYE':
	line = metodo + ' sip:' + direccion + ' SIP/2.0'
	print("Enviando: " + line)
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.connect(('127.0.0.1', port))
my_socket.send(bytes(line, 'utf-8') + b'\r\n')
data = my_socket.recv(1024)

print('Recibido -- ', data.decode('utf-8'))
print("Terminando socket...")

# Cerramos todo
my_socket.close()
print("Fin.")