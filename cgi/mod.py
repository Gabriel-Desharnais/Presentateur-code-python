#!/usr/bin/python3
# -*- coding: utf-8 -*

import cgi 

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")

print("Vous êtes en train de modifier la présentation",form.getvalue("id"))