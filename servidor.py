import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.0.29",4444))
s.listen(5)

sc, addr = s.accept()
while True:

     recibido = sc.recv(1024)
     if recibido == "quit":
       break
     print ("Recibido:", recibido)
     sc.send(recibido)

print("chao")

sc.close()
s.close()

