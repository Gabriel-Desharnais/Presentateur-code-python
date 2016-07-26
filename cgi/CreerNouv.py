#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
import cgitb
import datetime
from gogogadjet import *
form =cgi.FieldStorage()
cgitb.enable()
nom=form.getvalue('nom')
cible=form.getvalue('cible')
description=form.getvalue('description')
date=datetime.datetime.now()
print("Content-type: text/html; charset=utf-8\n")
page=gogocre(nom,cible,description,date)
