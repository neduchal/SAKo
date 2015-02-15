#! /usr/bin/python
# -*- coding: utf-8 -*-
# Nacteni knihoven 
import os
import os.path
import urllib


version = 1 * 1000000 + 0 * 1000 + 0 * 1

# KONSTANTY
DES_MATRIX = 0

class directory:

    # construktor
    def __init__(self, dirname): #
        self.filelist = []
        for root, directories, files in os.walk(dirname):
            for filename in files:
                filepath = os.path.join(root, filename)
                self.filelist.append(filepath)
        self.filelist.sort()
        self.position = 0
        self.count = len(self.filelist)

    def getNext(self):
        self.position = self.position + 1
        return self.filelist[self.position - 1]

    def getPrevious(self):
        self.position = self.position - 1
        return self.filelist[self.position + 1]

    def getFirst(self):
        return self.filelist[0]

    def getLast(self):
        return self.filelist[self.count-1]

    def getCount(self):
        return self.count

    pass

def submit(app_url, dirname, login, passwd, task):
    url = "http://147.228.124.51/" + app_url + "/index.php"

    dir = directory(dirname)
    data = {}
    data['login'] = login
    data['password'] = passwd
    data['task'] = task
    data['version'] = version
        
    for i in range(dir.getCount()):
        filename = dir.getNext();
        print "Oteviram soubor : " + filename
        f = open(filename, 'rb')
        filebody = f.read()    
        data['name' + str(i)] = filename
        data['file' + str(i)] = filebody
    print "Komunikace se serverem..."
    u = urllib.urlopen(url, urllib.urlencode(data))
    print "Vysledek :"         
    print u.read()
    f.close()  
