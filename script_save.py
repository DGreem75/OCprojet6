# -*-coding: utf-8 -*
import os
#import paramiko
os.chdir("/home/david/OCprojet6")

# SCRIPT DE BACKUP DES SWITCHS ET ROUTEURS INSTALLES"

# Lister les devices pour backup
#path=input("Saisir un chemin :")
path_device="config/"
path_sav="sav/"

liste_device= os.listdir(path_device)
print(liste_device)

# Pour chaque devices faire un backup FTP / SSH ??
for device in range(len(liste_device)):
    
    cmd= "sshpass -p Azerty@39 ssh -o HostKeyAlgorithms=ssh-rsa,ssh-dss -o KexAlgorithms=diffie-hellman-group1-sha1 -o Ciphers=aes128-cbc,3des-cbc -o MACs=hmac-md5,hmac-sha1 field@"+liste_device[device]+" \"show running-config\""+" > "+path_sav+liste_device[device]+".conf"
    #os.system("sshpass -p Azerty@39 ssh -o HostKeyAlgorithms=ssh-rsa,ssh-dss -o KexAlgorithms=diffie-hellman-group1-sha1 -o Ciphers=aes128-cbc,3des-cbc -o MACs=hmac-md5,hmac-sha1 field@10.1.2.254 "show running-config" > ros00101.conf")
    print(cmd)
    os.system(cmd)

# Si pas OK => renseigner log pas ok



#  recuperer la configuration d'un switch ou routeur Cisco
#sshpass -p Azerty@39 ssh -o HostKeyAlgorithms=ssh-rsa,ssh-dss -o KexAlgorithms=diffie-hellman-group1-sha1 -o Ciphers=aes128-cbc,3des-cbc -o MACs=hmac-md5,hmac-sha1 field@10.1.2.254 "show running-config" > ros00101.conf

