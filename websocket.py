import socket

host=""
ports= 1337
s=socket.socket()
s.bind((host,ports))
s.listen()
s_Client,adresse=s.accept()
print(adresse)
s_Client.send(b"bonjour client")
data=s_Client.recv(32)
print(data.decode())



s_Client.close()
s.close()