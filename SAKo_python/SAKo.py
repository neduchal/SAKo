#! /usr/bin/python
# -*- coding: utf-8 -*-
# Nacteni knihoven 
import httplib, urllib
import numpy as np
import cv2
from skimage import io

version = 0 * 1000000 + 3 * 1000 + 0 * 1

def serialize( result ):
  resStr = '';
  for i in xrange(1,len(result)+1):
    if i == 1:
      resStr = resStr + result[i]['name'] + '##'
    else:
      resStr = resStr + '%' + result[i]['name'] + '##'
    if type(result[i]['value']) == str:
      resStr = resStr + result[i]['value']
    elif  ((type(result[i]['value']) == int) or (type(result[i]['value']) == float) or (type(result[i]['value']) == long)):
      resStr = resStr + str(result[i]['value'])
    elif type(result[i]['value']) == np.ndarray:
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
  
def getTestData(login, passwd, taskStr):
  #Vytvoreni parametru http pozadavku
  params = urllib.urlencode({'login': login,'passwd': passwd, 'taskStr': taskStr, 'version' : version})
  # Hlavicky http pozadavku
  headers = {"Content-type": "application/x-www-form-urlencoded",
             "Accept": "text/plain"}
  # Server pro pripojeni
  conn = httplib.HTTPConnection("neduchal.cz", 80)
  # Konkretni pozadavek 
  conn.request("POST", "/sako/loadData.php", params, headers)
  # Provedeni pozadavku
  response = conn.getresponse()
  # Zpracovani vysledku
  data = response.read()   
  conn.close()   
  return data.lstrip('\r\n')  
  
def handleTestData(data):
  data_arr = data.split('##')
  if(data_arr[0] == 'actualize'):
    data = urllib.urlretrieve(data_arr[1], "SAKo.py")
    print "Klient systemu SAKo byl aktualizovan. Prosim provedte novy pokus o odevzdani"
    return ''
  else:
    return data_arr
    
def sendResults(login, passwd, taskStr, resultStr):
  #Vytvoreni parametru http pozadavku
  params = urllib.urlencode({'login': login,'passwd': passwd, 'taskStr': taskStr, 'result': resultStr, 'version' : version})
  # Hlavicky http pozadavku
  headers = {"Content-type": "application/x-www-form-urlencoded",
             "Accept": "text/plain"}
  # Server pro pripojeni
  conn = httplib.HTTPConnection("neduchal.cz", 80)
  # Konkretni pozadavek 
  conn.request("POST", "/sako/index.php", params, headers)
  # Provedeni pozadavku
  response = conn.getresponse()  
  # Zpracovani vysledku
  data = response.read()
  # Ukonceni spojeni 
  conn.close() 
  # Vypsani odpovedi
  print 'Stav pripojeni : '
  print response.status, response.reason
  print data.lstrip('\r\n')  
      
  
def submit(login, passwd, taskStr, filename, func_name):  
  # Nastaveni promennych
  result = {}
  m = __import__(taskStr + '_func')
  method = getattr(m, func_name)  
  # Stazeni a zpracovani testovacich dat
  data = getTestData(login, passwd, taskStr)  
  data_arr = handleTestData(data)  
  if(type(data_arr) != str):
    # Ziskani odezev metody na testovaci data
    for i in range(len(data_arr)):
      if i == 0:
        continue;
      data_split = data_arr[i].split('&')  
      if len(data_split) == 1:  
        image = io.imread(data_arr[i])
        if (len(image.shape) == 3):
          if(image.shape[2] == 3):
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        res = {}    
        res['value'] = method(image)
        res['name'] = 'r'+ str(i)
      else:
        image = io.imread(data_split[0])
        if (len(image.shape) == 3):
          if(image.shape[2] == 3):
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        res = {}    
        res['value'] = method(image, float(data_split[1]))
        res['name'] = 'r'+ str(i)     
      result[i] = res  
    # Pridani nekolika promennych do posilanych dat  
    lang = {}
    lang['name']  = 'language'
    lang['value'] = 'python'     
    result[len(result)+1] = lang;
    pack = {}  
    pack['name']  = 'test_package'
    pack['value'] = data_arr[0]    
    result[len(result)+1] = pack;  
    # Nacteni uzivatelskeho skriptu a pripojeni k posilanym datum
    with open(filename, 'r') as content_file:
      content = content_file.read()    
    cont = {}  
    cont['name']  = 'script'
    cont['value'] = content  
    result[len(result)+1] = cont;     
    # Vztvoreni tzv result stringu  
    resultStr = serialize( result )
    sendResults(login, passwd, taskStr, resultStr)    
  pass
