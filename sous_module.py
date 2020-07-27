import os

# Création de mobule besoin dans le script:
def liste_valeur_site(file_site):
    valeur_site = []
    temp_file_site = open(file_site, "r")
    for ligne in temp_file_site:
        s = ligne.strip("\n")
        l = s.split(";")
        valeur_site.append(l)  # les valeurs de notre site sont dans une liste de liste
    temp_file_site.close()
    return valeur_site