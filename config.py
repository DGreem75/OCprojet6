# Fonction pour configuration des différentes options

# import des modules
import os
from sous_module import *

#définition de listes pour la configuration

# Création des site
def conf_site ():
    os.system("cls")
    print (" \n CREATION D'UN SITE \n")
    # Saisir et définition du n° site
    site_number = input( "Saisir le numéro du site à créer: ")
    site = "s"+ site_number.rjust(3, '0')  # permet d'écrire le numéro du site sur 3 chiffre ex: 1 => 001
    file_site = "site/"+ site + ".csv"
    
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
    file.write("vlan2;vlan2;")  # nom du vlan + description
    file.write(vlan2_site)   # ip du vlan
    file.write(";255.255.255.0;")   # masque du vlan
    file.write(vlan2_site_gw)  # gw du vlan
    file.write("\n")   # saut de ligne
    file.write("vlan3;vlan3;")  # nom du vlan + description
    file.write(vlan3_site)   # ip du vlan
    file.write(";255.255.255.0;")   # masque du vlan
    file.write(vlan3_site_gw)  # gw du vlan
    file.write("\n")   # saut de ligne
    file.write("vlan99;management;")  # nom du vlan + description
    file.write(vlan99_site)   # ip du vlan
    file.write(";255.255.255.224;")   # masque du vlan
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
    # définition des listes
    config=[]
    valeur_site=[]

    os.system("cls")
    print (" \n CONFIGURATION ROUTEURS \n")
    #site_number = input( "Dans quel site vous voulez-créer le routeur ? saisir le n° du site: ")
    site_num = 0
    while site_num <= 1 and site_num <= 255:
        site_number = input( "Dans quel site vous voulez-créer le routeur ?\n Veuillez saisir un numéro de site entre 2 et 255.\n Saisir le n° du site: ")
        site_num = int(site_number)
        if site_num == 1:
            print("\nLe site '1' ne peut pas être généré ici.\n")
            print("\n Merci de saisir un numéro de site entre 2 et 255.\n")
        elif site_num > 255:
            print("\nLe numério de site ne peut pas être plus de 255.\n")
            print("\n Merci de saisir un numéro de site entre 2 et 255.\n")
        else:
            print("\n Le fichier de config va être généré.\n")
    
    site = "s"+ site_number.rjust(3, '0')  # permet d'écrire le numéro du site sur 3 chiffre ex: 1 => 001
    file_site = "site/"+ site + ".csv"
    ro_number = "ro"+site+"01"
    ro_file_config = "config/"+ro_number

    try:   # en 1er test si le site existe
        open(file_site, "r")
    except FileNotFoundError:
        print ("\n  Le site n'existe pas encore.\n  Vous devez créer le site avant, merci. \n  Vous allez être redirigé vers le Menu Principal \n")
        os.system("pause")
        return "site inexistant"
    else:
        print ("\n  Le site existe ! ")
        os.system("pause")


    try:   # en 2 test si le fichier de config du routeur existe déjà
        open(ro_file_config, "r")   
    except FileNotFoundError:
        print ("\n  Le Routeur {} n'existe pas encore.\n",ro_number)
        os.system("pause")
    else:
        print("\n  Le Router {0} existe déjà. \n  Le fichier de configuration existant sera écrasé. ",ro_number)
        os.system("pause")

    temp_router_config = open("template/router.txt", "r")
    for ligne in temp_router_config:
        config.append(ligne)  # notre template de config est dans une liste
    temp_router_config.close()

    temp_file_site = open(file_site, "r")
    for ligne in temp_file_site:
        s = ligne.strip("\n")
        l = s.split(";")
        valeur_site.append(l)  # les valeurs de notre site sont dans une liste de liste
    temp_file_site.close()
    
    # récupération valeur de VLAN2
    valeur_vlan2 = valeur_site[0]
    # récupération valeur de VLAN3
    valeur_vlan3 = valeur_site[1]
    # récupération valeur de VLAN99
    valeur_vlan99 = valeur_site[2]
    

    # modification des variables $ du template
    # hostane en ligne 2
    config[1]="hostane "+ro_number+"\n"
    # ip de la gw du vlan2 en ligne 7
    config[6]="ip add "+valeur_vlan2[4]+" "+valeur_vlan2[3]+"\n"
    # ip de la gw du vlan3 en ligne 11
    config[10]="ip add "+valeur_vlan3[4]+" "+valeur_vlan3[3]+"\n"
    # ip de la gw du vlan99 en ligne 15
    config[14]="ip add "+valeur_vlan99[4]+" "+valeur_vlan99[3]+"\n"
    # ip dhcp et gw du vlan2 en ligne 19-20
    config[18]="network "+valeur_vlan2[2]+"\n"
    config[19]="default-router "+valeur_vlan2[4]+"\n"
    # ip dhcp et gw du vlan3 en ligne 24-25
    config[23]="network "+valeur_vlan3[2]+"\n"
    config[24]="default-router "+valeur_vlan3[4]+"\n"
    print(config)
    
    # ecrire le fichier dans "config"
    ro_generate_conf = open(ro_file_config, "w")
    for li in range(len(config)):
        ro_generate_conf.write(config[li])
        #config[ligne]
    ro_generate_conf.close()
    os.system("pause")


# Création des switchs
def conf_sw ():
    # définition des listes
    config=[]
    valeur_site=[]

    os.system("cls")
    print ("\n CONFIGURATION SWITCHS \n")

    # dans quel site le switch doit être créé
    site_num = -1
    while site_num < 0 and site_num <= 255:
        site_number = input( "Dans quel site vous voulez-créer le switch ?\n Veuillez saisir un numéro de site entre 1 et 255.\n Saisir le n° du site: ")
        site_num = int(site_number)
        if site_num == 0:
            print("\nLe site '0' n'existe pas.\n")
            print("\n Merci de saisir un numéro de site entre 1 et 255.\n")
        elif site_num > 255:
            print("\nLe numério de site ne peut pas être plus de 255.\n")
            print("\n Merci de saisir un numéro de site entre 1 et 255.\n")
        else:
            print("\n Le fichier de config va être généré.\n")
    
    try:   # en 1er test si le site existe
        open(file_site, "r")
        print ("\n  Le site existe ! ")
        os.system("pause")
    except FileNotFoundError:
        print ("\n  Le site n'existe pas encore.\n  Vous devez créer le site avant, merci. \n  Vous allez être redirigé vers le Menu Principal \n")
        os.system("pause")
        return "site inexistant"
    
    # quel niveau de switch doit être créé
    niveau_sw = -1
    while niveau_sw < 1 or niveau_sw > 2:
        niveau_sw = input(" Saisir le niveau du switch 1 ou 2: ")
        niveau_sw = int(niveau_sw)
    

    site = "s"+ site_number.rjust(3, '0')  # permet d'écrire le numéro du site sur 3 chiffre ex: 1 => 001
    file_site = "site/"+ site + ".csv"
    sw_number = "sw"+site+niveau_sw+"01"
    sw_file_config = "config/"+sw_number

    

    try:   # en 2 test si le fichier de config du switch existe déjà
        open(sw_file_config, "r")
        print("\n  Le Switch ", sw_number ," existe déjà. \n  Le fichier de configuration existant sera écrasé.")
        os.system("pause")
    except FileNotFoundError:
        print ("\n  Le Switch n'existe pas encore.\n", sw_number ,"va être générer.\n")
        os.system("pause")

    temp_switch_config = open("template/switch_1.txt", "r")
    for ligne in temp_switch_config:
        config.append(ligne)  # notre template de config est dans une liste
    temp_switch_config.close()

    temp_file_site = open(file_site, "r")
    for ligne in temp_file_site:
        s = ligne.strip("\n")
        l = s.split(";")
        valeur_site.append(l)  # les valeurs de notre site sont dans une liste de liste
    temp_file_site.close()