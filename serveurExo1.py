import random
import socket

host = ""
port = 1335
s = socket.socket()
s.bind((host, port))
s.listen(5)
client, address = s.accept()
print("{} connected".format(address))
rep=client.recv(128)
print(rep.decode())
#s.send(b"test\r\n")



#while True:
    #s.listen(5)
    #client, address = s.accept()
    #print("{} connected".format(address))

    #response = client.recv(128)
    #if response !="":
        #print(response.decode())
print("close")
client.close()
s.close()