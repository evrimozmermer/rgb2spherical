# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 09:53:14 2018

@author: evrozm
"""

import math

def vectorsComponent(r,g,b):
    if b==0:
        teta = 0
    else:
        teta = (math.atan(r/b)*360)/(math.pi*2)
    if g==0:
        fi = 90
    else:
        fi = (math.atan(math.sqrt((r^2)+(b^2))/g)*360)/(math.pi*2)
    p = math.sqrt((r^2)+(g^2)+(b^2))
    return p, teta, fi

def rgb2hsvAllColors():
    p = []
    teta = []
    fi = []
    for d in range(256):
        print(d)
        for g in range(256):
            for b in range(256):
                pv, tetav, fiv = vectorsComponent(r,g,b)
                p.append(pv)
                teta.append(tetav)
                fi.append(fiv)
    return p,teta,fi

def rgb2hsv(rgb):
    p = []
    teta = []
    fi = []
    for cnt in range(len(rgb[0])):
        r = rgb[0][cnt]
        g = rgb[1][cnt]
        b = rgb[2][cnt]
        pv, tetav, fiv = vectorsComponent(r,g,b)
        p.append(pv)
        teta.append(tetav)
        fi.append(fiv)
    return p,teta,fi

def rgb2hsvSpecial(rgb):
    p = []
    teta = []
    fi = []
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]
    pv, tetav, fiv = vectorsComponent(r,g,b)
    p.append(pv)
    teta.append(tetav)
    fi.append(fiv)
    return p,teta,fi