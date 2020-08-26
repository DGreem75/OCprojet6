# -*-coding: utf-8 -*
import os
import netmiko
from subprocess import *
from time import strftime, gmtime

os.chdir("/home/david/OCprojet6")

# Définition des variables globales
ip_serv_ftp = "10.1.2.100" # adresse ip du serveur FTP
dir_ftp = "/home/share/"   # répertoire de base du serveur FTP
dir_sav ="sav/"            # répertoire pour les fichiers de backup
dir_log ="log/"            # répertoire pour les fichiers de log

file_device = "list_device.csv"  # fichier qui liste les device existants


#Définition fonction

# TEST PING SI DEVICE ONLINE
def test_ping(device_ip):
    command="ping -c 2 "+device_ip
    ping_test = call(command, shell=True)
    if ping_test == 0:
        print("device ping\n")
        return 0
    else:
        print("device ping pas\n")
        return 1

# COMMANDE CISCO A EXECUTER
def executer_commande_cisco(address_ip, user, passwd, commande):
    # Définition paramètre connexion Cisco
    cisco = {
            'device_type': 'cisco_ios', 'ip':address_ip,
            'username':user, 'password':passwd,
        }

    # Test et envoie de la commande Cisco
    try:
        net_connect = netmiko.ConnectHandler(**cisco)
        net_connect.enable()
        result = net_connect.send_command(commande)
        print(result, "\n")
    except:
        return "nok"
    else:
        return "ok"


# SCRIPT DE BACKUP DES SWITCHS ET ROUTEURS INSTALLES"

# Lister les devices pour backup
devices=[]

# Créer la liste des devices à backuper
list_file=dir_ftp+file_device
liste_device = open(list_file, 'r')
for ligne in liste_device:
    s = ligne.strip("\n")
    l = s.split(";")
    devices.append(l)
liste_device.close()

# Récupérer l'heure
heure = strftime("%Y-%m-%d_%Hh%M", gmtime())
print("\n")
print(heure)
print("\n")

# Définition du nom de fichier de log
log =dir_ftp+dir_log+"backup_"+heure+".log"
print(log)

# Pour chaque devices faire un backup FTP / SSH
for n_device in range(len(devices)):
    device = devices[n_device]
    name_device = device[0]
    ip_device = device[1]

    # test si device ping => si ok alors on backup sinon log erreur
    if test_ping(ip_device)==0:
        print("Ma commande peut etre ok! \n")
        
        # commande via ssh et show running vers un fichier
        # cmd= "sshpass -p Azerty@39 ssh -o HostKeyAlgorithms=ssh-rsa,ssh-dss -o KexAlgorithms=diffie-hellman-group1-sha1 -o Ciphers=aes128-cbc,3des-cbc -o MACs=hmac-md5,hmac-sha1 field@"+ip_device+" \"show running-config\""+" > "+dir_sav+name_device+".conf"

        # commande via show runnig vers serveur FTP
        # cmd= "sshpass -p Azerty@39 ssh -o HostKeyAlgorithms=ssh-rsa,ssh-dss -o KexAlgorithms=diffie-hellman-group1-sha1 -o Ciphers=aes128-cbc,3des-cbc -o MACs=hmac-md5,hmac-sha1 field@"+ip_device+" \"show running-config | redirect ftp://field:Azerty@39@10.1.2.100/"+dir_sav+name_device+".conf\""
        
        # executer la commande via SSH
        #retour = call(cmd, shell=True)

        # Commande Cisco via NETMIKO
        cmd= "show running-config | redirect ftp://field:Azerty@39@"+ip_serv_ftp+"/"+dir_sav+name_device
        retour = executer_commande_cisco(ip_device,"field","Azerty@39",cmd)

        print(retour)
        print("\n")
    else:
        retour = 100

    if retour == 100:  # retour ping NOK
        file_log = open(log , 'a')
        file_log.write(name_device)
        file_log.write(" : save NOK - ping NOK\n")  # si erreur alors noté backup pas ok
        file_log.close()
    elif retour =="nok":  # retour ping ok, mais commande pas OK
        file_log = open(log , 'a')
        file_log.write(name_device)
        file_log.write(" : save NOK - erreur commande\n")
        file_log.close()
    elif retour =="ok":  # retour ping ok, commande OK
        file_log = open(log , 'a')
        file_log.write(name_device)
        file_log.write(" : save OK !!!\n")
        file_log.close()
    else:          # autre erreur non gérée
        file_log = open(log , 'a')
        file_log.write(name_device)
        file_log.write(" : save NOK - erreur inconnue\n")
        file_log.close()


#  recuperer la configuration d'un switch ou routeur Cisco
#sshpass -p Azerty@39 ssh -o HostKeyAlgorithms=ssh-rsa,ssh-dss -o KexAlgorithms=diffie-hellman-group1-sha1 -o Ciphers=aes128-cbc,3des-cbc -o MACs=hmac-md5,hmac-sha1 field@10.1.2.254 "show running-config" > ros00101.conf
