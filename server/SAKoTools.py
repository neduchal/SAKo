#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
:platform: Unix, Windows
:synopsis: Server Tools Systému Automatické Kontroly (SAKo)

.. moduleauthor:: Petr Neduchal <neduchal@ntis.zcu.cz>


"""
import sys
import os
import cv2
import json
import collections

def getPathToSubmitedData(idString):
    """
        Vrátí cestu k nahraným datům
        
        :param idString: Retezec s casti cesty
        :type idString: str
    """
    dir = "../" + os.path.dirname(idString[2:]) + "/"
    return dir

def getMethodInModule(dir, module, method):
    """
        Vrátí odkaz na metodu.
        
        :param dir: cesta do složky
        :type dir: str    
        :param module: název modulu
        :type module: str  
        :param method: název metody
        :type method: str          
    """
    path_to_script = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.join(path_to_script, dir))
    m = __import__(module)
    method = getattr(m, method)
    return method


class result:
    def __init__(self, dir): 
        """Konstruktor třídy
            
           :param dirname: Cesta ke složce.
           :type dirname: str.
        """
        self.filename = dir          
        self.values = []

    def openResultJSON(self, dir):
        f = open(dir + 'result.json', 'w')
        return f
    
    def addText(self, text):
        self.values.append('text##' + text)
     
    def addImg(self, dir, filename):
        self.values.append('img##' + dir + filename)
        
    def addLink(self, url, desc):
        self.values.append('link##' +  url + "##" + filename)    
        
    def addPoints(self, userPoints, maxPoints):
        self.values.append('points##' + userPoints + '##' + maxPoints)
        
    def saveAndClose(self):
        f =  self.openResultJSON(self.filename) 
        d = {}
        for i in range(len(self.values)):
            d.update({str(i) : str(self.values[i])})
        od = collections.OrderedDict(sorted(d.items()))
        json.dump(od,f)
        f.close()