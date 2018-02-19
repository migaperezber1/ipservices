#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("192.168.0.29", 4444))

while True:
   mensaje = raw_input("> ")
   s.send(mensaje)
   if mensaje == "quit":
     break

print "adios"

s.close()
