# -*-coding: utf-8 -*
import os
from subprocess import *
from time import strftime, gmtime

os.chdir("/home/david/OCprojet6")

#Définition fonction
def test_ping(device_ip):
    command="ping -c 2 "+device_ip
    ping_test = call(command, shell=True)
    if ping_test == 0:
        print("device ping\n")
        return 0
    else:
        print("device ping pas\n")
        return 1

# SCRIPT DE BACKUP DES SWITCHS ET ROUTEURS INSTALLES"

# Lister les devices pour backup
path_device="config/"
path_sav="sav/"
list_file="list_device.csv"
devices=[]

# créer la liste des devices à backuper
liste_device = open(list_file, 'r')
for ligne in liste_device:
    s = ligne.strip("\n")
    l = s.split(";")
    devices.append(l)
liste_device.close()

# récupérer l'heure
heure = strftime("%Y-%m-%d_%Hh%M", gmtime())
print("\n")
print(heure)
print("\n")

# définition du nom de fichier de log
log ="backup_"+heure+".log"
print(log)

# Pour chaque devices faire un backup FTP / SSH
for n_device in range(len(devices)):
    device = devices[n_device]
    name_device = device[0]
    ip_device = device[1]

    # test si device ping => si ok alors on backup sinon log erreur
    if test_ping(ip_device)==0:
        print("Ma commande peut etre ok! \n")
        # commande via show running vers un fichier
        # cmd= "sshpass -p Azerty@39 ssh -o HostKeyAlgorithms=ssh-rsa,ssh-dss -o KexAlgorithms=diffie-hellman-group1-sha1 -o Ciphers=aes128-cbc,3des-cbc -o MACs=hmac-md5,hmac-sha1 field@"+ip_device+" \"show running-config\""+" > "+path_sav+name_device+".conf"
        # commande via show runnig vers serveur FTP
        cmd= "sshpass -p Azerty@39 ssh -o HostKeyAlgorithms=ssh-rsa,ssh-dss -o KexAlgorithms=diffie-hellman-group1-sha1 -o Ciphers=aes128-cbc,3des-cbc -o MACs=hmac-md5,hmac-sha1 field@"+ip_device+" \"show running-config | redirect ftp://field:Azerty@39@10.1.2.100/"+path_sav+name_device+".conf\""
    #os.system("sshpass -p Azerty@39 ssh -o HostKeyAlgorithms=ssh-rsa,ssh-dss -o KexAlgorithms=diffie-hellman-group1-sha1 -o Ciphers=aes128-cbc,3des-cbc -o MACs=hmac-md5,hmac-sha1 field@10.1.2.254 "show running-config" > ros00101.conf")
    # print(cmd)
        retour = call(cmd, shell=True)
        print(retour)
        print("\n")
    else:
        retour = 255

    if retour == 255:
        file_log = open(log , 'a')
        file_log.write(name_device)
        file_log.write(" : save NOK\n")  # si erreur alors noté backup pas ok
        file_log.close()
    else:
        file_log = open(log , 'a')
        file_log.write(name_device)     # tout c'est bien passé - backup OK
        file_log.write(" : save OK\n")
        file_log.close()

#  recuperer la configuration d'un switch ou routeur Cisco
#sshpass -p Azerty@39 ssh -o HostKeyAlgorithms=ssh-rsa,ssh-dss -o KexAlgorithms=diffie-hellman-group1-sha1 -o Ciphers=aes128-cbc,3des-cbc -o MACs=hmac-md5,hmac-sha1 field@10.1.2.254 "show running-config" > ros00101.conf
