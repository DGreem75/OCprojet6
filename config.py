# Fonction pour configuration des différentes options

# Création des site
def conf_site ():
    print (" \n CREATION D'UN SITE \n")
    site_number = input( "Saisir le numéro du site ")
    site = "s"+ site_number.rjust(3, '0')  # permet d'écrire le numéro du site sur 3 chiffre ex: 1 => 001
    file_site = site + ".txt"
    print(site)
    print (file_site)

    file = open(file_site, "w")
    file.write(site)
    file.close()

# Création des routeurs
def conf_ro ():
    print (" \n CONFIGURATION ROUTEURS \n")
    print (" Créer un site           :   1")
    print (" Créer un routeur        :   2")
    print (" Créer un switch         :   3")
    # print (" Créer .....           :   4")
    print (" Quitter                 :   Q")

# Création des switchs
def conf_sw ():
    print ("\n CONFIGURATION SWITCHS \n")
    print (" Créer un site           :   1")
    print (" Créer un routeur        :   2")
    print (" Créer un switch         :   3")
    # print (" Créer .....           :   4")
    print (" Quitter                 :   Q")