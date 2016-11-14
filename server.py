#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys

##EXCEPCION ESTAN BIEN/NO LOS ARGUMENTOS
if not len(sys.argv) == 5:
    sys.exit("Usage: python3 server.py IP puerto fichero_audio")
python3, _, ip, port, audio_file = sys.argv
port = int(port)

class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        datos = self.rfile.read().decode('utf-8').split(' ')
        if datos[0] == 'INVITE':
            metodo = datos[1].split(':')[1]
            print('SIP/2.0 100 Trying' + '\r\n' + 'SIP/2.0 180 Ring')
        else datos[0] == 'ACK':
            metodo = datos[1].split(':')[1]
            print('SIP/2.0 200 OK')
        else datos[0] == 'BYE':
            metodo = datos[1].split(':')[1]
            print('SIP/2.0 400 Bad Request')
        elif
            print('SIP/2.0 405 Method Not Allowed')

        # Escribe dirección y puerto del cliente (de tupla client_address)
        self.wfile.write(b"Hemos recibido tu peticion")
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            line = self.rfile.read()
            print("El cliente nos manda " + line.decode('utf-8'))

            # Si no hay más líneas salimos del bucle infinito
            if not line:
                break

if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos
    serv = socketserver.UDPServer(('', 6001), EchoHandler)
    print("Listening...")
    serv.serve_forever()
