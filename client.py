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

#EXCEPCION ESTAN BIEN/NO LOS ARGUMENTOS
if not len(sys.argv) == 3:
    sys.exit('Usage: python3 client.py method receiver@IP:SIPport')
_, metodo, direccion = sys.argv

if metodo == 'INVITE':
    line = metodo + ' sip:' + direccion + ' SIP/2.0'
    print('Enviando: ' + line)
if metodo == 'BYE':
    line = metodo + ' sip:' + direccion + ' SIP/2.0'
    print('Enviando: ' + line)

my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.connect(('127.0.0.1', port))
my_socket.send(bytes(line, 'utf-8') + b'\r\n\r\n')
data = my_socket.recv(1024)

data = data.decode('utf-8').split(' ')
if (data[2] == 'Trying' and data[5] == 'Ring' and data[8] == 'OK'):
    line = 'ACK sip:' + direccion + ' SIP/2.0'
    my_socket.send(bytes(line, 'utf-8') + b'\r\n\r\n')

print('Terminando socket...')

# Cerramos todo
my_socket.close()
print('Fin.')
