import socket

host = '127.0.0.1'
port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)

print(f"Attente d'une connexion sur {host}:{port}...")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connexion établie avec {client_address}")

    data = client_socket.recv(1024).decode()
    if data == "ping":
        client_socket.send("pong".encode())

    client_socket.close()
