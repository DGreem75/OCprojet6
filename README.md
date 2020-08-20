# "Création et backup config Cisco"
_(OC PROJET6 Participez à la communauté)_

![Python 3.8](https://img.shields.io/badge/Python-3.8-blue) ![test](https://img.shields.io/badge/tests-100%25-brightgreen)

## Description

Permet de créer la configuration de routeurs et de switchs Cisco pour la gestion de plusieurs sites.
La configuration des routeurs sera la même pour tous les sites, et il y a 2 niveau de switchs.
Le backup est manuel, mais peut être automatisé.

## Pour commencer

Il faudra adapter les môdèles "routeur et switchs" suivant vos besoins et donc adapter la création des sites,
ainsi que modifier la partie "configuration" pour changer les variables des môdèles.

### Pré-requis

Ce qu'il est requis pour commencer avec votre projet...

- Pour Windows 10: installation de la focntion avancé "serveur FTP" ou un programme "serveur FTP
- Pour Linux : un serveur FTP
- Python 3
- Créer un utilisateur commun entre le serveur FTP et l'utilisateur des routeurs et switchs
- Installation de !["PIP"](https://linuxize.com/post/how-to-install-pip-on-ubuntu-18.04/) pour Python.

### Installation

Les étapes pour utiliser les scripts:

_ Récupérer les scripts sur votre PC / Serveur.

_ Modifier les variables globales pour les chemins des diférents dossiers (serveur FTP, fichiers configurations, backup ...)

_exemple pour le fichier config.py et script_save.py :_

**\# variable globale**
* ip_serv_ftp = "10.1.2.100" # adresse ip du serveur FTP
* dir_ftp = "/home/share/"   # répertoire de base du serveur FTP
* dir_site = "site/"         # répertoire pour les fichiers sites
* dir_config ="config/"      # répertoire pour les fichiers des config
* dir_sav ="sav/"            # répertoire pour les fichiers de backup
* dir_template = "template/" # répertoire pour les templates de config
* file_device = "list_device.csv"  # fichier qui liste les device existants


## Démarrage

Il faut simplement, depuis l'invite de commande exécuter le script "generate_config.py"

exemple Linux:

$ python3 generate_config.py

## Fabriqué avec

Entrez les programmes/logiciels/ressources que vous avez utilisé pour développer votre projet

_exemples :_
* [Materialize.css](http://materializecss.com) - Framework CSS (front-end)
* [Atom](https://atom.io/) - Editeur de textes

## Versions

Suivant les "branch":

Master : pour Windows

LinuxVersion : pour Linux

Windowstest : version testé dans GNS3


## Auteurs

_(pour le lien mettez simplement l'URL de votre projet suivi de ``/contirubors``)_
