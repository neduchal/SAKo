#! /usr/bin/python
# -*- coding: utf-8 -*-
# Nacteni knihoven

import os.path
import sys
import SAKoTools

SAKoTools.getPathToSubmitedData("./")

r = SAKoTools.result('./')
r.addText("TEST 1")
r.addText("TEST 2")
r.addText("TEST 3")
r.addText("TEST 4")
r.addText("TEST 5")
r.addImg("neduchal/test/", "aaa.jpg")

r.saveAndClose()
