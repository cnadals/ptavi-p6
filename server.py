#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys
import os

##EXCEPCION ESTAN BIEN/NO LOS ARGUMENTOS
if not len(sys.argv) == 4:
    sys.exit('Usage: python3 server.py IP puerto fichero_audio')
_, ip, port, audio_file = sys.argv
port = int(port)


class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):

        # Escribe dirección y puerto del cliente (de tupla client_address)
        self.wfile.write(b'Hemos recibido tu peticion \r\n\r\n')
        line = self.rfile.read()
        print('El cliente nos manda ', line.decode('utf-8'))
        datos = line.decode('utf-8').split()
        if datos[0] == 'INVITE':
            metodo = datos[1].split(':')[1]
            self.wfile.write(b'SIP/2.0 100 Trying \r\n\r\n')
            self.wfile.write(b'SIP/2.0 180 Ring \r\n\r\n')
            self.wfile.write(b'SIP/2.0 200 OK \r\n\r\n')
        elif datos[0] == 'BYE':
            metodo = datos[1].split(':')[1]
            self.wfile.write(b'SIP/2.0 200 OK')
        elif datos[0] == 'ACK':
            metodo = datos[1].split(':')[1]
            self.wfile.write(b'SIP/2.0 200 OK')
            # aEjecutar es un string con lo que se ha de ejecutar en la shell
            aEjecutar = 'mp32rtp -i 127.0.0.1 -p 23032 < ' + audio_file
            print('Vamos a ejecutar', aEjecutar)
            os.system(aEjecutar)
        elif datos[0] != ('INVITE' and 'BYE' and 'ACK'):
            metodo = datos[1].split(':')[1]
            self.wfile.write(b'SIP/2.0 405 Method Not Allowed')
        else:
            self.wfile.write(b'SIP/2.0 400 Bad Request')

if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos
    if not os.path.exists(audio_file):
        sys.exit('El archivo ' + audio_file + ' no existe')
    serv = socketserver.UDPServer(('', port), EchoHandler)
    print("Listening...")
    serv.serve_forever()
