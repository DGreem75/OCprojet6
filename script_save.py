# -*-coding: utf-8 -*
import os
from subprocess import *
import netmiko
from time import strftime, gmtime

os.chdir("C:/Script/OCprojet6")

#Définition fonction
def test_ping(device_ip):
    command="ping -n 2 "+device_ip
    ping_test = call(command, shell=True)
    if ping_test == 0:
        print("device ping\n")
        return 0
    else:
        print("device ping pas\n")
        return 1

def executer_commande_cisco(address_ip, user, passwd, commande):
    #définition parametre connection Cisco
    cisco = {
        'device_type': 'cisco_ios', 'ip':address_ip,
        'username':user, 'password':passwd,
    }
    print(cisco,"\n")
    print(commande,"\n")
    try:
        net_connect = netmiko.ConnectHandler(**cisco)
        net_connect.enable()
        result = net_connect.send_command(commande)
        print(result,"\n")
    except:
        return "nok"
    else:
        return "ok"

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
        cmd ="show running-config | redirect ftp://field:Azerty@39@10.1.2.100/sav/"+name_device
        retour = executer_commande_cisco(ip_device,"field","Azerty@39",cmd)
        #cmd= "echo \"show running\" | putty.exe -ssh field@"+ip_device+" -pw Azerty@39 > "+path_sav+name_device+".conf"
    #os.system("putty.exe -ssh field@10.1.2.254 -pw Azerty@39 "show running-config" > ros00101.conf")
        #print(cmd)
        #retour = call(cmd, shell=True)
        print(retour ,"\n")
    else:
        retour = 100

    if retour == 100:   # retour pink nok
        file_log = open(log , 'a')
        file_log.write(name_device)
        file_log.write(" : save NOK - ping nok\n")  # si erreur alors noté backup pas ok
        file_log.close()
    elif retour == "nok":    # retour ping OK, mais commande pas ok
        file_log = open(log , 'a')
        file_log.write(name_device)
        file_log.write(" : save NOK - erreur commande\n")  # si erreur alors noté backup pas ok
        file_log.close()
    elif retour == "ok":     # retour ping OK et caommande ssh OK
        file_log = open(log , 'a')
        file_log.write(name_device)
        file_log.write(" : save OK !!!\n")  # si erreur alors noté backup pas ok
        file_log.close()
    else:                # une erreur non gérée
        file_log = open(log , 'a')
        file_log.write(name_device)
        file_log.write(" : save NOK - erreur inconnue\n")
        file_log.close()

#  recuperer la configuration d'un switch ou routeur Cisco
#sshpass -p Azerty@39 ssh -o HostKeyAlgorithms=ssh-rsa,ssh-dss -o KexAlgorithms=diffie-hellman-group1-sha1 -o Ciphers=aes128-cbc,3des-cbc -o MACs=hmac-md5,hmac-sha1 field@10.1.2.254 "show running-config" > ros00101.conf
