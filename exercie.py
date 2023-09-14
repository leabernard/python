
sexe = input("Entrez le sexe du client (Homme/Femme) : ").lower()
age = int(input("Entrez l'âge du client : "))
poids_en_kilos = float(input("Entrez le poids du client en kilogrammes : "))
hauteur_en_cm = float(input("Entrez la taille du client en centimètres : "))


if sexe == "homme":
    BRM = 66 + (13.7 * poids_en_kilos) + (5 * hauteur_en_cm) - (6.8 * age)
elif sexe == "femme":
    BRM = 655 + (9.6 * poids_en_kilos) + (1.7 * hauteur_en_cm) - (4.7 * age)
else:
    print("Sexe non reconnu. Veuillez entrer 'homme' ou 'femme'.")


print("Niveaux d'activité :")
print("1. Sédentaire")
print("2. Très faible activité")
print("3. Activité légère")
print("4. Activité modérée")
print("5. Haute activité")
print("6. Activité extrême")
niveau_activite = int(input("Entrez le numéro correspondant au niveau d'activité du client : "))


multiplicateurs = [1, 1.2, 1.4, 1.6, 1.8, 2]


if niveau_activite < 1 or niveau_activite > 6:
    print("Niveau d'activité non valide. Veuillez choisir un numéro de 1 à 6.")
else:
 
    BRMa = BRM * multiplicateurs[niveau_activite - 1]

   
    objectif = input("Souhaitez-vous maigrir ou grossir ? (maigrir/grossir) : ").lower()


    if objectif == "maigrir":
        BRMa *= 0.9  
    elif objectif == "grossir":
        BRMa *= 1.1 
    else:
        print("Objectif non reconnu. Veuillez entrer 'maigrir' ou 'grossir'.")

  
    print(f"Le nombre de calories par jour pour garder un poids constant (BRMa) est de : {BRMa:.2f} calories.")