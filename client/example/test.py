#! /usr/bin/python
# -*- coding: utf-8 -*-
# Nacteni knihoven

import os.path
import sys

path_to_script = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(path_to_script, "../"))

import SAKo

# SAKo.submit(ZDO/MPV, SLOZKA, LOGIN, PASSWORD, TASK)
SAKo.submit("zdo", "./src/", "test", "test", 'copy')
