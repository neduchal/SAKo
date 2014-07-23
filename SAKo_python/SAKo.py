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

def serialize( result ):
  resStr = '';
  for i in range(len(result)):
    if i == 0:
      resStr = resStr + result[i]['name'] + '#'
    else:
      resStr = resStr + '%' +result[i]['name'] + '#'
    if result[i]['type'] == 's':
      resStr = resStr + result[i]['value']
    elif result[i]['type'] == 'i':
      resStr = resStr + str(result[i]['value'])
    elif result[i]['type'] == 'm':
      rows = result[i]['value'].shape[0]
      cols = result[i]['value'].shape[1]
      for j in range(rows):
        for k in range(cols):
          resStr = resStr + str(result[i]['value'][j,k])
          if k!= cols-1:
            resStr = resStr + ','
        if j!= rows-1:
          resStr = resStr + ';'
  return resStr
          
def submit(login, passwd, taskStr, result, filename):
  
  with open(filename, 'r') as content_file:
    content = content_file.read();
  
  resultStr = serialize( result )
  #Vytvoreni parametru http pozadavku
  params = urllib.urlencode({'login': login,'passwd': passwd, 'taskStr': taskStr, 'result': resultStr})
  # Hlavicky http pozadavku
  headers = {"Content-type": "application/x-www-form-urlencoded",
             "Accept": "text/plain"}
  # Server pro pripojeni
  conn = httplib.HTTPConnection("neduchal.cz:80")
  # Konkretni pozadavek 
  conn.request("POST", "/zdo/index.php", params, headers)
  # Provedeni pozadavku
  response = conn.getresponse()
  print response.status, response.reason
  # Zpracovani vysledku
  data = response.read()
  # Vypsani delky vracenych dat
  print data
  # Ukonceni spojeni 
  conn.close()
  pass
