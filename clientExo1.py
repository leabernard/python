import socket
import time

host = "localhost"
port = 1335

var=65

s = socket.socket()
s.connect((host, port))
print("connection on {}".format(port))
nb=str(var)
s.send(nb.encode())
#data = s.recv(128)
#print(data.decode())

print("close")
s.close()