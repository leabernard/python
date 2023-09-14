import socket
import random

# Liste des éléments du jeu
elements = ["pierre", "feuille", "ciseaux"]

# Fonction pour choisir un élément au hasard
def choisir_element():
    return random.choice(elements)

# Création du socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 12345))

for _ in range(5):
    choix_client = choisir_element()
    client_socket.send(choix_client.encode())
    resultat = client_socket.recv(1024).decode()
    print(f"Vous avez choisi : {choix_client}, Résultat : {resultat}")

score_final = client_socket.recv(1024).decode()
print(score_final)

client_socket.close()
