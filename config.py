# Fonction pour configuration des différentes options

# import des modules
import os

# variable globale
ip_serv_ftp = "10.1.2.100" # adresse ip du serveur FTP
dir_ftp = "/home/share/"   # répertoire de base du serveur FTP
dir_site = "site/"         # répertoire pour les fichiers sites
dir_config ="config/"      # répertoire pour les fichiers des config
dir_sav ="sav/"            # répertoire pour les fichiers de backup
dir_template = "template/" # répertoire pour les templates de config
file_device = "list_device.csv"  # fichier qui liste les device existants

# Création des site
def conf_site ():
    os.system("clear")
    print (" \n CREATION D'UN SITE \n")
    # Saisir et définition du n° site
    site_number = input( "Saisir le numéro du site à créer: ")
    ip_wan_site = input( "Saisir l'adresse IP WAN du site (ex:192.168.122.10): ")
    mask_wan_site = input( "Saisir  le masque du WAN du site (ex:255.255.255.0): ")
    site = "s"+ site_number.rjust(3, '0')  # permet d'écrire le numéro du site sur 3 chiffre ex: 1 => 001
    file_site = dir_ftp+dir_site+site+ ".csv"
    
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
    
    # création du fichier CSV du site
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
    file.write("\n")   # saut de ligne
    file.write("IP;ip-wan;")
    file.write(ip_wan_site)  # ip du wan du site
    file.write(";")
    file.write(mask_wan_site)  # masque du wan du site
    # pas de saut de ligne en fin de fichier
    file.close()

    #affichage du fichier site créé
    with open(file_site, 'r') as fichier:
        for ligne in fichier:
            print (ligne)
    print ("\n Site créé.\n")
    os.system("sleep 3")

# Ecrire le fichier "liste des devices existants"
def write_list_device (exist,device_name, device_ip):
    if exist=="non":
        f_device=dir_ftp+file_device
        file = open(f_device, 'a')
        file.write(device_name)
        file.write(";")
        file.write(device_ip)
        file.write("\n")
        file.close()
        print("\nAjout de ",device_name," à la liste des devices existants.\n")
        os.system("sleep 3")
    else:
        print("Device existant, donc pas ajouter dans la liste de backup.\n\n")
        os.system("sleep 3")

# Lire et écrire la configuration d'un site dans une liste
def read_site(site):
    valeur_site=[]
    file_site = dir_ftp+dir_site+site+ ".csv"
    temp_file_site = open(file_site, "r")
    for ligne in temp_file_site:
        s = ligne.strip("\n")
        l = s.split(";")
        valeur_site.append(l)  # les valeurs de notre site sont dans une liste de liste
    temp_file_site.close()
    return valeur_site

# Ecrire le fichier de configugration d'un device
def write_config(config,file,device):
    # ecrire le fichier dans "config"
    file_generate_conf = open(file, "w")
    for li in range(len(config)):
        file_generate_conf.write(config[li])
    file_generate_conf.close()
    print("\n Fichier config du ", device ," créé.\n")
    os.system("sleep 1")


# Création des routeurs
def conf_ro ():
    # définition des listes
    config=[]
    valeur_site=[]

    os.system("clear")
    print (" \n CONFIGURATION ROUTEURS \n")
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
    file_site = dir_ftp+dir_site+site+ ".csv"
    ro_number = "ro"+site+"01"
    ro_file_config = dir_ftp+dir_config+ro_number

    try:   # en 1er test si le site existe
        open(file_site, "r")
    except FileNotFoundError:
        print ("\n  Le site n'existe pas encore.\n  Vous devez créer le site avant, merci. \n  Vous allez être redirigé vers le Menu Principal \n")
        os.system("sleep 1")
        return "site inexistant"
    else:
        print ("\n  Le site existe ! ")
        os.system("sleep 1")

    try:   # en 2 test si le fichier de config du routeur existe déjà
        open(ro_file_config, "r")
    except FileNotFoundError:
        print ("\n  Le Routeur n'existe pas encore.\n")
        exist="non"
        os.system("sleep 1")
    else:
        print("\n  Le Router ", ro_number, " existe déjà. \n  Le fichier de configuration existant sera écrasé. ")
        exist="oui" # permet de savoir si il faut ajouter le device à la liste de device existant
        os.system("sleep 1")

    temp_ro = dir_ftp+dir_template+"router.txt"
    temp_router_config = open(temp_ro, "r")
    for ligne in temp_router_config:
        config.append(ligne)  # notre template de config est dans une liste
    temp_router_config.close()

    # récupération des valeurs du sites
    valeur_site = read_site(site)
    
    # Récupération des valerus nécessaires à la modification du template
    # récupération valeur de VLAN2
    valeur_vlan2 = valeur_site[0]
    # récupération valeur de VLAN3
    valeur_vlan3 = valeur_site[1]
    # récupération valeur de VLAN99
    valeur_vlan99 = valeur_site[2]
    # récupération IP WAN du routeur
    valeur_ip_wan = valeur_site[3]

    # modification des variables du template
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
    config[24]="network "+valeur_vlan3[2]+"\n"
    config[25]="default-router "+valeur_vlan3[4]+"\n"
    config[29]="ip address "+valeur_ip_wan[2]+" "+valeur_ip_wan[3]+"\n"
    config[38]="  Connection sur "+ro_number.upper()+"\n"
    #print(config)
    
    # ecrire le fichier dans "config"
    write_config(config,ro_file_config,ro_number)
    
    #ajouter le device à la liste de devices existant pour le backup
    write_list_device(exist,ro_number, valeur_vlan99[4])

# Création des switchs

# fonctions pour le niveau des switchs.
def conf_sw_level1(site):
    # définition liste
    config=[]

    #definition nom du switch
    #création du numero de switch ex: sws001101
    sw_number = "sw"+site+"101"
    sw_file_config = dir_ftp+dir_config+sw_number

    # définition du template du switch niveau1
    temp_sw1 = dir_ftp+dir_template+"switch_1.txt"
    temp_switch_config = open(temp_sw1, "r")
    for ligne in temp_switch_config:
        config.append(ligne)  # notre template de config est dans une liste
    temp_switch_config.close()

    # récupération des valeurs du sites
    valeur_site = read_site(site)

    # générer fichier de config
    # récupération valeur de VLAN99
    valeur_vlan99 = valeur_site[2]
    #adresse ip du switch dans le VLAN99 suivant niveau et numéro de switch
    ip_lan_vlan99 = valeur_vlan99[2]  # retour ok adresse ip du lan

    ip_sw_vlan99=ip_lan_vlan99.split(".") # découpage de l'adresse IP dans une liste
    ip_sw_vlan99[3]="1"
    
    #reconstitution adresse IP du switch
    ip_sw = ip_sw_vlan99[0]+"."+ip_sw_vlan99[1]+"."+ip_sw_vlan99[2]+"."+ip_sw_vlan99[3]

    # modification des variables $ du template
    # hostane en ligne 2
    config[1]="hostame "+sw_number+"\n"
    # config IP dans vlan99 management
    config[53]="ip default-gateway "+valeur_vlan99[4]+"\n"
    config[54]="ip route 0.0.0.0 0.0.0.0 "+valeur_vlan99[4]+"\n"
    config[56]="ip address "+ip_sw+" "+valeur_vlan99[3]+"\n"
    # config bannière
    config[90]="  Connection sur "+sw_number.upper()+"\n"

    try:   # test si le fichier de config du switch existe déjà
        open(sw_file_config, 'r')
    except FileNotFoundError:
        print ("\n  Le Switch n'existe pas encore.\n", sw_number ,"va être générer.\n")
        exist = "non"
        os.system("sleep 1")
    else:
        print("\n  Le Switch ", sw_number ," existe déjà. \n  Le fichier de configuration existant sera écrasé.")
        exist = "oui"
        os.system("sleep 1")

    # ecrire le fichier dans "config"
    write_config(config,sw_file_config,sw_number)
    #sw_generate_conf = open(sw_file_config, "w")
    #for li in range(len(config)):
    #    sw_generate_conf.write(config[li])
        #config[ligne]
    #sw_generate_conf.close()
    #print("\n Fichier config du switch ", sw_number, " créé.\n")
    #os.system("sleep 1")

    #ajouter le device à la liste de devices existant pour le backup
    write_list_device(exist,sw_number, ip_sw)
    #if exist=="non":
    #    write_list_device(sw_number, ip_sw)
    #    print("\nAjout de ",sw_number," à la liste des devices existants.\n")
    #    os.system("sleep 3")
    #else:
    #    print("Device existant, donc pas ajouter dans la liste de backup.\n\n")
    #    os.system("sleep 3")

def conf_sw_level2(site,numero_sw):
    # définition liste, variable
    config=[]
    num_sw = int(numero_sw)
    sw_number = "sw"+site+"2"+numero_sw.rjust(2,'0')
    sw_file_config = dir_ftp+dir_config+sw_number

    # définition du template du switch niveau1
    temp_sw2 = dir_ftp+dir_template+"switch_2.txt"
    temp_switch_config = open(temp_sw2, "r")
    for ligne in temp_switch_config:
        config.append(ligne)  # notre template de config est dans une liste
    temp_switch_config.close()

    # récupération des valeurs du sites
    valeur_site = read_site(site)

    # générer fichier de config
    # récupération valeur de VLAN99
    valeur_vlan99 = valeur_site[2]
    #adresse ip du switch dans le VLAN99 suivant niveau et numéro de switch
    ip_lan_vlan99 = valeur_vlan99[2]  # retour ok adresse ip du lan

    ip_sw_vlan99=ip_lan_vlan99.split(".") # découpage de l'adresse IP dans une liste
    ip_sw_vlan99[3]=num_sw+1
    ip_sw_vlan99[3]=str(ip_sw_vlan99[3])
    
    #reconstitution adresse IP du switch
    ip_sw = ip_sw_vlan99[0]+"."+ip_sw_vlan99[1]+"."+ip_sw_vlan99[2]+"."+ip_sw_vlan99[3]

    # modification des variables $ du template
    # hostane en ligne 2
    config[1]="hostame "+sw_number+"\n"
    # config IP dans vlan99 management
    config[87]="ip default-gateway "+valeur_vlan99[4]+"\n"
    config[88]="ip route 0.0.0.0 0.0.0.0 "+valeur_vlan99[4]+"\n"
    config[90]="ip address "+ip_sw+" "+valeur_vlan99[3]+"\n"
    # config bannière
    config[99]="  Connection sur "+sw_number.upper()+"\n"

    try:   # test si le fichier de config du switch existe déjà
        open(sw_file_config, 'r')
    except FileNotFoundError:
        print ("\n  Le Switch n'existe pas encore.\n", sw_number ,"va être générer.\n")
        exist = "non"
        os.system("sleep 1")
    else:
        print("\n  Le Switch ", sw_number ," existe déjà. \n  Le fichier de configuration existant sera écrasé.")
        exist = "oui"
        os.system("sleep 1")

    # ecrire le fichier dans "config"
    write_config(config,sw_file_config,sw_number)
    #sw_generate_conf = open(sw_file_config, "w")
    #for li in range(len(config)):
    #    sw_generate_conf.write(config[li])
    #    #config[ligne]
    #sw_generate_conf.close()
    #print("\n Fichier config du switch ", sw_number, " créé.\n")
    #os.system("sleep 1")

    #ajouter le device à la liste de devices existant pour le backup
    write_list_device(exist,sw_number, ip_sw)
    #if exist=="non":
    #    write_list_device(sw_number, ip_sw)
    #    print("\nAjout de ",sw_number," à la liste des devices existants.\n")
    #    os.system("sleep 3")
    #else:
    #    print("Device existant, donc pas ajouter dans la liste de backup.\n\n")
    #    os.system("sleep 3")

# Création des config des switchs
def conf_sw ():
    # définition des listes
    #valeur_site=[]

    os.system("clear")
    print ("\n CONFIGURATION SWITCHS \n")
    site_num = 0
    while site_num < 1 and site_num <= 255:
        site_number = input( "Dans quel site vous voulez-créer le switch ?\n Veuillez saisir un numéro de site entre 1 et 255.\n Saisir le n° du site: ")
        site_num = int(site_number)
        if site_num > 255:
            print("\n Merci de saisir un numéro de site entre 1 et 255.\n")
        else:
            print("\n Le fichier de config va être généré.\n")
    
    site = "s"+ site_number.rjust(3, '0')  # permet d'écrire le numéro du site sur 3 chiffre ex: 1 => 001
    file_site = dir_ftp+dir_site+site+ ".csv"

    try:   # en 1er test si le site existe
        open(file_site, "r")
    except FileNotFoundError:
        print ("\n  Le site n'existe pas encore.\n  Vous devez créer le site avant, merci. \n  Vous allez être redirigé vers le Menu Principal \n")
        os.system("sleep 1")
        return "site inexistant"
    else:
        print ("\n  Le site existe ! ")
        os.system("sleep 1")
    
    # quel niveau de switch doit être créé
    niv_sw = 0
    while niv_sw < 1 or niv_sw > 2:
        niveau_sw = input(" Saisir le niveau du switch 1 ou 2: ")
        niv_sw = int(niveau_sw)

    # quel numéro de switch doit être créé
    if niv_sw == 2:
        num_sw = 0
        while num_sw < 1 or num_sw > 20:
            numero_sw = input(" Saisir le numéro du switch de niveau 2 (entre 1 et 20): ")
            num_sw = int(numero_sw)
            conf_sw_level2(site,numero_sw)
    else:
        numero_sw="1"
        print(" Le switch de niveau 1 va etre généré.\n")
        conf_sw_level1(site)
