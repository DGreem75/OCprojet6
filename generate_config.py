# -*-coding: utf-8 -*

# Import des différents modules
import os
import pickle
from menu import *
from config import *
import subprocess

# Se placer dans notre dossier de travail
os.chdir("/home/david/OCprojet6")


# Ouvrir le menu principale
choix = "a"
while choix != "Q":
    os.system("cls")
    menu_principal()
    choix = input ("Que voulez-vous faire : ")
    if choix == "1":   # Créer un site
        conf_site()
    elif choix =="2":  # Créer un routeur
        conf_ro()
    elif choix =="3":  # Créer un switch
        conf_sw()
    elif choix =="4":  # Lancer le backup
        os.system("python3 script_save.py")
    elif choix == "Q":
        print ("\n\n    -- MERCI A BIENTOT -- \n\n\n")        
    else:
        print ("\n\n -- Mauvais choix ;-) -- \n\n")
