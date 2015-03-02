#! /usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import os
import random
import sys

"""
    Načtení modulu SAKoTools
"""
path_to_script = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(path_to_script, "../"))
import SAKoTools

"""
    Vytvoření parseru parametrů
"""
parser = argparse.ArgumentParser(description='Base Validator.')
parser.add_argument('-i', '--input', default=False)
args = parser.parse_args()

"""
    Nastavení cesty k uploadovaným datům
"""
dir = SAKoTools.getPathToSubmitedData(args.input)

"""
    Nastavení odkazu na metodu v odevzdaném modulu
"""
SAKoTools.getMethodInModule(dir, 'module', 'method')

"""
    Validace odevzdane prace :

        Zalezi na konkretni uloze

"""
r = SAKoTools.result(dir)

pas = "spatne"
points = 0
for i in range(10):
    a = random.randint(1, 20)
    b = random.randint(1, 20)

    result1 = a + b
    result2 = method(a, b)

    diff = diff + int((result1 - result2) == 0)
    pas = "spatne"
    if diff == 0:
        pas = "spravne"
        points = points + 1
    print("Test " + str(i) + ": a = " + str(a) + ", b = " + str(b) +
          ", vysledek metody :" + str(result2) +
          ", spravny vysledek : " + str(result1) + " (" + pas + ")")

print "Ziskany pocet bodu : " + str(10 - diff) + "/10"
r.addPoints()
r.saveAndClose()
