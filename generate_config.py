# -*-coding: utf-8 -*

# Import des différents modules
import os
import pickle
from menu import *
from config import *

# Se placer dans notre dossier de travail
os.chdir("D:/script cours/OCprojet6")


# Ouvrir le menu principale
choix = "a"
while choix != "Q":
    os.system("cls")
    menu_principal()
    choix = input ("Que voulez-vous faire : ")
    # os.system("pause")
    if choix == "1":   # Créer un site
        conf_site()
    elif choix =="2":  # Créer un routeur
        conf_ro()
    elif choix =="3":  # Créer un switch
        conf_sw()
    elif choix == "Q":
        print ("\n\n    -- MERCI A BIENTOT -- \n\n\n")        
    else:
        print ("\n\n -- Mauvais choix ;-) -- \n\n")






## CREATION SITE

# Afficher VLAN2
# Afficher VLAN3
# Afficher VLAN99
# Creation fichier sxxx.txt  xxx = n° du site

# Création routeur
# Saisir le n° du site
# => vérifier si site existe et différent du site 1 (site mère)
# => vérifier si routeur à créer n'existe pas (test ping par exemple)
# => genérer configuration routeur du site n° saisi

# Creation SWITCH
# Saisir le n° du site
# => vérifier si site existe
# Saisir si switch niveau 1 ou 2
# => vérifier si switch à créer n'existe pas (test ping par exemple)
# => genérer configuration switch du site n° saisi
