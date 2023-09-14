def DeterminationJour(date, mois, annee):
    Jours = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
    Nbr_j = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    jour_actuel = 0
    for i in range(mois - 1):
        jour_actuel += Nbr_j[i]
    
    jour_actuel += date
    jour_semaine = Jours[(jour_actuel + 4) % 7]  
    
    return jour_semaine
