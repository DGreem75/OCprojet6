# -*-coding: utf-8 -*
import os
os.chdir("D:/script cours/OCprojet6")

# SCRIPT DE BACKUP DES SWITCHS ET ROUTEURS INSTALLES"
# Lister les devices pour backup
# Pour chaque devices faire un backup FTP / SSH ??
# Si pas OK => renseigner log pas ok

# faire une connexion SSH qui envoie une commande au routeur ou switch
# pour faire un 'copy running-config tftp://'.$server.'/',"\n".$host."-".$now."-confg\n")

# faire une boucle qui liste les fichiers dans config pour faire les backups du matériel existant