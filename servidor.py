#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
import sys
import cv2
import pickle
import numpy as np
import struct


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost",4444))
s.listen(1)

sc, addr = s.accept()
print "conexion aceptada"
data = ""
payload_size = struct.calcsize("L") #devuelve el tamaño de la cadena en ese formato.

while True:
    while len(data)< payload_size:
        data += sc.recv(4096)
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("L", packed_msg_size)[0]
    
    while len(data) < msg_size:
        data += sc.recv(4096)
    frame_data = data[:msg_size]
    data = data[msg_size:]

    frame = pickle.loads(frame_data)
    print frame.size


#     recibido = sc.recv(1024)
 #    if recibido == "quit":
  #     break
   #  print ("Recibido:", recibido)
    
    # mensaje = raw_input("> ")
     #sc.send(mensaje)

#print("chao")

sc.close()

