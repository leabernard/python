import socket
import time
import threading

host = '127.0.0.1'
port = 12345


class Service(threading.Thread):
    def __init__(self, client_socket, client_address):
        super().__init__()
        self.client_socket = client_socket
        self.client_address = client_address

    def run(self):
        print(f"Connexion établie avec {self.client_address}")
        data = self.client_socket.recv(1024).decode()

        # Simuler un ralentissement de 5 secondes
        time.sleep(5)

        if data == "ping":
            self.client_socket.send("pong".encode())

        self.client_socket.close()


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)

print(f"Attente d'une connexion sur {host}:{port}...")

while True:
    client_socket, client_address = server_socket.accept()
    service = Service(client_socket, client_address)
    service.start()
