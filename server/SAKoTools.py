#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
:platform: Unix, Windows
:synopsis: Server Tools Systému Automatické Kontroly (SAKo)

Závislosti
----------

* sys
* os
* json
* collection

.. moduleauthor:: Petr Neduchal <neduchal@ntis.zcu.cz>


"""
import sys
import os
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
    """
        Třída usnadňující tvorbu výstupu validátoru.

        Vytvoří, naplní a uloží soubor : result.json               

        *Ukázka použití:*

        .. code-block:: python

            import SAKoTools      
            r = SAKoTools.result('./')
            r.addText("TEST 1")
            r.addText("TEST 2")
            r.addLink("http://exampleurl.com","Link na stranky exampleurl")
            r.saveAndClose()
    """
    
    def __init__(self, dir):
        """Konstruktor třídy

           :param dir: Cesta ke složce.
           :type dir: str.
        """
        self.filename = dir
        self.values = []

    def openResultJSON(self, dir):
        """Otevře nový result.json soubor v zadané složce

           :param dir: Cesta ke složce.
           :type dir: str.
        """
        f = open(dir + 'result.json', 'w')
        return f
    
    def addText(self, text):
        """Přidá zadaný text do souboru s výsledkem

           :param text: Text k uložení do result.json.
           :type text: str.
        """
        self.values.append('text##' + text)

    def addImg(self, dir, filename):
        """Přidá obrázek do souboru s výsledkem (respektive cestu k němu)

           :param dir: Cesta ke složce / případně url (bez názvu souboru).
           :type dir: str.
           :param filename: Název obrázku.
           :type filename: str.
        """
        self.values.append('img##' + dir + filename)

    def addLink(self, url, desc):
        """Přidá odkaz do souboru s výsledkem

           :param url: url adresa.
           :type url: str.
           :param desc: popis odkazu.
           :type desc: str.
        """
        self.values.append('link##' +  url + "##" + desc)

    def addPoints(self, userPoints, maxPoints):
        """Přidá informaci o počtu bodů aktuálního pokusu

           :param userPoints: dosažené body.
           :type userPoints: uint.
           :param maxPoints: maximální počet bodů.
           :type maxPoints: str.
        """
        self.values.append('points##' + userPoints + '##' + maxPoints)

    def saveAndClose(self):
        """
            Uloží a uzavře soubor s výsledkem result.json.
            Tato funkce by se měla volat jako poslední.
        """
        f =  self.openResultJSON(self.filename)
        d = {}
        for i in range(len(self.values)):
            d.update({str(i) : str(self.values[i])})
        od = collections.OrderedDict(sorted(d.items()))
        json.dump(od,f)
        f.close()
