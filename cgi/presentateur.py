#!/usr/bin/python3
# -*- coding: utf-8 -*
import cgi
import cgitb
from gogogadjet import *
cgitb.enable()
print("Content-type: text/html; charset=utf-8\n")
page_acueil=gogogadjet("accueil.html")
gogoReListe()
print(page_acueil)