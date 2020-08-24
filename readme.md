# "Création et backup config Cisco"
_(OC PROJET6 Participez à la communauté)_

![Python 3.8](https://img.shields.io/badge/Python-3.8-blue) ![test](https://img.shields.io/badge/tests-100%25-brightgreen)

___
## Description

Permet de créer la configuration de routeurs et de switchs Cisco pour la gestion de plusieurs sites.
La configuration des routeurs sera la même pour tous les sites, et il y a 2 niveau de switchs.

Le backup est manuel, mais peut être automatisé.

___
## Pour commencer

Identique à la version "master", il faut adapter uniquement les variables globales (chemins Windows différent de Linux)

___
### Pré-requis

Identique à "master"

___
### Installation

Identique à "master"

Sauf chemin du serveur FTP.

Donc:

**\# variable globale**

* dir_ftp = "c:/temp/FTPWIN/"   # répertoire de base du serveur FTP

___
## Démarrage

Il faut simplement, depuis l'invite de commande exécuter le script "generate_config.py"

_exemple :_

Se placer dans le dossier contenant les scripts, puis executer la commande:

C:\Script\OCprojet6\python generate_config.py

___
## Fabriqué avec

[Visual Studio](https://visualstudio.microsoft.com/fr/).
