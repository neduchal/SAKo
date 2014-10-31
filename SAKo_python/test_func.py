#! /usr/bin/python
# -*- coding: utf-8 -*-
# Nacteni knihoven 
import numpy as np
import cv2

def histogram(img):
    img =  cv2.cvtColor(img, cv2.cv.CV_RGB2GRAY)
    hist = cv2.calcHist([img],[0],None,[256],[0,256])
    #hist[0] = hist[0] - 1000
    return hist        
