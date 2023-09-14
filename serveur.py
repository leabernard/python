import socket
import random

# Liste des éléments du jeu
elements = ["pierre", "feuille", "ciseaux"]


# Fonction pour choisir un élément au hasard
def choisir_element():
    return random.choice(elements)


# Fonction pour déterminer le gagnant d'un tour
def determiner_gagnant(choix_client, choix_serveur):
    if choix_client == choix_serveur:
        return "Égalité"
    elif (choix_client == "pierre" and choix_serveur == "ciseaux") or \
            (choix_client == "feuille" and choix_serveur == "pierre") or \
            (choix_client == "ciseaux" and choix_serveur == "feuille"):
        return "Client gagne"
    else:
        return "Serveur gagne"


# Création du socket serveur
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 12345))
server_socket.listen(1)

print("Attente de la connexion du client...")
client_socket, client_address = server_socket.accept()
print("Client connecté :", client_address)

score_client = 0
score_serveur = 0

for _ in range(5):
    choix_serveur = choisir_element()
    choix_client = client_socket.recv(1024).decode()
    resultat = determiner_gagnant(choix_client, choix_serveur)

    if resultat == "Client gagne":
        score_client += 1
    elif resultat == "Serveur gagne":
        score_serveur += 1

    print(f"Client choisit : {choix_client}, Serveur choisit : {choix_serveur}, Résultat : {resultat}")

client_socket.send(f"Score final - Client : {score_client}, Serveur : {score_serveur}".encode())
client_socket.close()
server_socket.close()

if score_client > score_serveur:
    print("Le client gagne la partie !")
elif score_serveur > score_client:
    print("Le serveur gagne la partie !")
else:
    print("Match nul !")
