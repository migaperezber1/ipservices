#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
import sys
import cv2
import numpy as np
import struct
import pickle

cap = cv2.VideoCapture(0)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("localhost", 4444))

while True:
   
   #mensaje = raw_input("> ")
   #s.send(mensaje)
   #recibido = s.recv(1024)
   #print (recibido)
   #if mensaje == "quit":
    # break
#print "adios" 
    ret,frame = cap.read()
    data = pickle.dumps(frame)#serializacion del frame, prepararlo para el envio.
    s.sendall(struct.pack("L", len(data)) + data) #provee estructura de C para enviarlo en forma de bytes, provee los valores de tamado del dato, y el dato.
    
s.close()
