#cette fonction permet de saisir les notes pour chaque étudiant dans la liste fournie
def saisieNotes(liste_etudiants):
    for etudiant in liste_etudiants:
        note = int(input(f"Entrez la note de {etudiant['prenom']} {etudiant['nom']} : "))
        etudiant['note'] = note

#cette fonction permet de trouver l'etudiant ayant obtenu la meilleure notre dans la liste donnée
def meilleur(liste_etudiants):
    meilleur_etudiant = max(liste_etudiants, key=lambda x: x['note'])
    return (meilleur_etudiant['note'], f"{meilleur_etudiant['prenom']} {meilleur_etudiant['nom']}")

#la fonction principale du programme
def progPrincipal():
    #liste initiale d'édutiants avec leur nom et prénom
    d = [
        {"nom": "Ebel", "prenom": "Franck"},
        {"nom": "Spriet", "prenom": "Hugues"},
        {"nom": "Burel", "prenom": "Romain"},
        {"nom": "De Montalivet", "prenom": "Paul"}
    ]
    #appel a la fonction saisiNotes pour entrer les notes pour chaque étudiants

    saisieNotes(d)
    #afficher la liste mise a jours avec les notes
    print(d)
#appel à la fonction meilleur pour trouver et afficher la meilleur note de l'étudiant correspondant
    resu = meilleur(d)
    print("La meilleure note est : ", resu[0], " et appartient à ", resu[1])

#vérification si le script est exécuté directement
if __name__ == "__main__":
    progPrincipal()
