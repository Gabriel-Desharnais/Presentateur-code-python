#!/usr/bin/python3
# coding: utf8
""" ---------------------------------
Ce petit programme est écrit en python 3.
Il à pour but de permettre de créer des pésentations
style <<PowerPoint>> mais qui peut inclure des sections
de codes python et de pouvoir les exécuter.
---------------------------------------"""
nomCool="À trouver"
version = "0.0.0.0.0.0.0.0.0"
ok="[OK]"
#import sys
print(nomCool,"version",version)
print("Importation du module serveur web",end="\t\t")
try:
	from Serveur import *
	print(ok)
except ImportError:
	ok="[OUPS]"
	print(ok)
	ok="[OK]"
	#On devrait faire de quoi par rapport à ça...
print("Importation du multitâches",end="\t\t")
try:
	from threading import Thread
	print(ok)
except ImportError:
	ok="[OUPS]"
	print(ok)
	ok="[OK]"
	#On devrait faire de quoi par rapport à ça...
print("Démarage du serveur web",end="\t\t")
try:
	Tserveur=LanceLeServeur()
	Tserveur.start()
	print(ok)
except :
	ok="[OUPS]"
	print(ok)
	ok="[OK]"
	#On devrait faire de quoi par rapport à ça...
print("Importation du gestionnaire de commandes",end="\t\t")

try:
	from communicateur import *
	print(ok)
except ImportError:
	ok="[OUPS]"
	print(ok)
	ok="[OK]"
	#On devrait faire de quoi par rapport à ça...
print("Lancement du gestionnaire de commandes",end="\t\t")

try:
	comServ=LanceLeComServeur()
	comServ.start()
	print(ok)
except ImportError:
	ok="[OUPS]"
	print(ok)
	ok="[OK]"
	#On devrait faire de quoi par rapport à ça...

print("Importation du navigateur web",end="\t\t")
try:
	import webbrowser 
	print(ok)
except ImportError:
	ok="[OUPS]"
	print(ok)
	ok="[OK]"
	#On devrait faire de quoi par rapport à ça...
print("Ouverture de l'application web",end="\t\t")
try:
	import os
	from time import sleep
	savout = os.dup(2)
	os.close(2)
	os.open(os.devnull, os.O_RDWR)
	try:
    		webbrowser.open("http://localhost:8888/cgi/presentateur.py")#On devrait rendre ça plus universel
	finally:
		os.dup2(savout,1)
	
	print(ok)
except ImportError:
	ok="[OUPS]"
	print(ok)
	ok="[OK]"
	#On devrait faire de quoi par rapport à ça...
input("")
