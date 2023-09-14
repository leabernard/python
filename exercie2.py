import random


def generer_nombre_aleatoire(limite):
    return random.randint(1, limite)


def jeu_devine_le_nombre():
    print("Bienvenue au jeu Devine le nombre!")
    
    limite = int(input("Entrez le nombre maximum pour la génération du nombre aléatoire : "))
    nombre_a_deviner = generer_nombre_aleatoire(limite)
    
    tentative = 0
    trouve = False
    
    while not trouve:
        tentative += 1
        proposition = int(input(f"Essayez de deviner le nombre (entre 1 et {limite}) : "))
        
        if proposition == nombre_a_deviner:
            trouve = True
        elif proposition < nombre_a_deviner:
            print("Plus grand !")
        else:
            print("Plus petit !")
    
    print(f"Bravo, vous avez gagné en {tentative} coups!")


if __name__ == "__main__":
    jeu_devine_le_nombre()
