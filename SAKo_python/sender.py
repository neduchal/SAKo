#! /usr/bin/python
# -*- coding: utf-8 -*-
# Nacteni knihoven 
import httplib, urllib
import numpy as np

"""
# Převod matice na string
string = ''
for i in range(512):
  for j in range(512):
    string = string + str(A[i,j])
    if j < 511: 
      string = string + ','
  string = string + ';'
"""

def submit(login, passwd, taskStr, result):
  #Vytvoření parametrů http požadavku
  params = urllib.urlencode({'login': login,'passwd': passwd, 'taskStr': taskStr, 'result': result})
  # Hlavičky http požadavku
  headers = {"Content-type": "application/x-www-form-urlencoded",
             "Accept": "text/plain"}
  # Server pro připojení
  conn = httplib.HTTPConnection("neduchal.cz:80")
  # Konkrétní požadavek 
  conn.request("POST", "/zdo/index.php", params, headers)
  # Provedení požadavku
  response = conn.getresponse()
  print response.status, response.reason
  # Zpracování výsledků
  data = response.read()
  # Vypsání délky vrácených dat
  print data
  # Ukončení spojení 
  conn.close()
  pass
