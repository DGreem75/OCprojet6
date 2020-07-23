# Fonction pour configuration des différentes options

# import des modules
import os

# Création des site
def conf_site ():
    os.system("cls")
    print (" \n CREATION D'UN SITE \n")
    # Saisir et définition du n° site
    site_number = input( "Saisir le numéro du site à créer: ")
    site = "s"+ site_number.rjust(3, '0')  # permet d'écrire le numéro du site sur 3 chiffre ex: 1 => 001
    file_site = "site/"+ site + ".txt"
    
    # définition des VLANs du site
    #     vlan2
    vlan2_site = "10."+site_number+".2.0"  # définition du lan du VLAN
    vlan2_site_gw = "10."+site_number+".2.254"  # définition de la gw du VLAN
    #     vlan3
    vlan3_site = "10."+site_number+".3.0"  # définition du lan du VLAN
    vlan3_site_gw = "10."+site_number+".3.254"  # définition de la gw du VLAN
    #     vlan99
    vlan99_site = "10."+site_number+".99.0"  # définition du lan du VLAN
    vlan99_site_gw = "10."+site_number+".99.30"  # définition de la gw du VLAN
    
    file = open(file_site, "w")
    file.write("vlan2 vlan2 ")  # nom du vlan + description
    file.write(vlan2_site)   # ip du vlan
    file.write(" 255.255.255.0 ")   # masque du vlan
    file.write(vlan2_site_gw)  # gw du vlan
    file.write("\n")   # saut de ligne
    file.write("vlan3 vlan3 ")  # nom du vlan + description
    file.write(vlan3_site)   # ip du vlan
    file.write(" 255.255.255.0 ")   # masque du vlan
    file.write(vlan3_site_gw)  # gw du vlan
    file.write("\n")   # saut de ligne
    file.write("vlan99 management ")  # nom du vlan + description
    file.write(vlan99_site)   # ip du vlan
    file.write(" 255.255.255.224 ")   # masque du vlan
    file.write(vlan99_site_gw)  # gw du vlan
    # pas de saut de ligne en fin de fichier
    file.close()

    #affichage du fichier site créé
    with open(file_site, "r") as fichier:
        for ligne in fichier:
            print (ligne)
    os.system("pause")

# Création des routeurs
def conf_ro ():
    os.system("cls")
    print (" \n CONFIGURATION ROUTEURS \n")
    site_number = input( "Dans quel site vous voulez-créer le routeur ? saisir le n° du site: ")
    site = "s"+ site_number.rjust(3, '0')  # permet d'écrire le numéro du site sur 3 chiffre ex: 1 => 001
    file_site = "site/"+ site + ".txt"

    try:   # test si le site existe
        fichier = open(file_site, "r")
        print ("\n  Le site existe ! ")
        os.system("pause")
    except FileNotFoundError:
        print ("\n  Le site n'existe pas encore.\n  Vous devez créer le site avant, merci. \n  Vous allez être redirigé vers le Menu Principal \n")
        os.system("pause")
        return "site inexistant"

    router_config = open("template/router.txt")
    for ligne in router_config:
        print (ligne)
    router_config.close()
    os.system("pause")


# Création des switchs
def conf_sw ():
    print ("\n CONFIGURATION SWITCHS \n")
    print (" Créer un site           :   1")
    print (" Créer un routeur        :   2")
    print (" Créer un switch         :   3")
    # print (" Créer .....           :   4")
    print (" Quitter                 :   Q")