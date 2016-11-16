#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys

##EXCEPCION ESTAN BIEN/NO LOS ARGUMENTOS
if not len(sys.argv) == 4:
    sys.exit("Usage: python3 server.py IP puerto fichero_audio")
_, ip, port, audio_file = sys.argv
port = int(port)

class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        
        trying = 'SIP/2.0 100 Trying'
        ring = 'SIP/2.0 180 Ring'
        ack = 'SIP/2.0 200 OK'
        # Escribe dirección y puerto del cliente (de tupla client_address)
        self.wfile.write(b"Hemos recibido tu peticion")
        line = self.rfile.read()
        print("El cliente nos manda ", line.decode('utf-8'))
        datos = line.decode('utf-8').split()
        if datos[0] == 'INVITE':
            metodo = datos[1].split(':')[1]
            print(trying + '\r\n' + ring + '\r\n' + ack)
        elif datos[0] == 'BYE':
            metodo = datos[1].split(':')[1]
            print('SIP/2.0 400 Bad Request')
        else:
            print('SIP/2.0 405 Method Not Allowed')

if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos
    serv = socketserver.UDPServer(('', port), EchoHandler)
    print("Listening...")
    serv.serve_forever()
