#! /usr/bin/python
# -*- coding: utf-8 -*-
# Nacteni knihoven 

import os.path
import sys

#path_to_script = os.path.dirname(os.path.abspath(__file__))
#sys.path.append(os.path.join(path_to_script, "../"))

#import SAKo

#sys.path.append(os.path.join(path_to_script, "../../server/"))

import SAKoTools


# SAKo.submit(ZDO/MPV, SLOZKA, LOGIN, PASSWORD, TASK)
# SAKo.submit("sako_dev", "./", "neduchal", "testing", 'test')

print __file__

SAKoTools.getPathToSubmitedData("./")

r = SAKoTools.result('./')
r.addText("TEST 1")
r.addText("TEST 2")
r.addText("TEST 3")
r.addText("TEST 4")
r.addText("TEST 5")
r.addImg("neduchal/test/", "aaa.jpg")

r.saveAndClose()


