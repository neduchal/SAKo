#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
:platform: Unix, Windows
:synopsis: Klient Systému Automatické Kontroly (SAKo)

.. moduleauthor:: Petr Neduchal <neduchal@ntis.zcu.cz>


"""





# Nacteni knihoven 
import os
import os.path
import urllib


version = 1 * 1000000 + 0 * 1000 + 0 * 1

# KONSTANTY
DES_MATRIX = 0

class directory:
    """
        Třída pro práci se složkou
    """
    # construktor
    def __init__(self, dirname): 
        """Konstruktor třídy
            
           :param dirname: Cesta ke složce.
           :type dirname: str.
        """
        self.filelist = []
        for root, directories, files in os.walk(dirname):
            for filename in files:
                filepath = os.path.join(root, filename)
                self.filelist.append(filepath)
        self.filelist.sort()
        self.position = 0
        self.count = len(self.filelist)

    def getNext(self):
        """
            Vrátí další položku v otevřené složce.
            
            :returns: str -- cesta k souboru
        """
        self.position = self.position + 1
        return self.filelist[self.position - 1]

    def getPrevious(self):
        """
            Vrátí předchozí položku v otevřené složce.
            
            :returns: str -- cesta k souboru
        """        
        self.position = self.position - 1
        return self.filelist[self.position + 1]

    def getFirst(self):
        """
            Vrátí první položku v otevřené složce.
            
            :returns: str -- cesta k souboru
        """        
        return self.filelist[0]

    def getLast(self):
        """
            Vrátí poslední položku v otevřené složce.
            
            :returns: str -- cesta k souboru
        """        
        return self.filelist[self.count-1]

    def getCount(self):
        """
            Vrátí počet položek v otevřené složce.
            
            :returns: int -- pocet položek
        """        
        return self.count

    pass

def submit(app, dirname, login, passwd, task):
    """Funkce pro odevzdání úlohy na server.

       :param app: Aplikace do které je kód odevzdáván.
       :type app: str.
       
       :param dirname:  Složka s odevzdávanými soubory.
       :type dirname: str.   
       :param login:  Login do systému SAKo.
       :type login: str.
       :param passwd:  Heslo do systému SAKo.
       :type passwd: str. 
       :param task:  Název odevzdávané úlohy.
       :type task: str.        
       
    """    
    url = "http://147.228.124.51/" + app + "/index.php"

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
