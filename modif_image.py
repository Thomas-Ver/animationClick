#!/bin/python3.10 
# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

def get_carre_coords(img,x,y):
    # Renvoie les coordonnées du carré de 100x100 pixels autour du clic
    x_start = max(0, x - 50)
    y_start = max(0, y - 50)
    x_end = min(img.shape[1], x + 50)
    y_end = min(img.shape[0], y + 50)
    return x_start, y_start, x_end, y_end

def carre_noir(img,x,y):
    # Noircir un carré de 100x100 pixels autour du clic
    x_start, y_start, x_end, y_end = get_carre_coords(img,x,y)
    img[y_start:y_end, x_start:x_end] = np.zeros((y_end - y_start, x_end - x_start,3))
    return img

def random_mult(img,x,y):
    # Multiplier un carré de 100x100 pixels autour du clic par une matrice aléatoire
    x_start, y_start, x_end, y_end = get_carre_coords(img,x,y)
    M=np.random.rand(y_end - y_start, x_end - x_start)
    img[y_start:y_end, x_start:x_end] = img[y_start:y_end, x_start:x_end]*M
    return img

def deform(img,x,y): # https://stackoverflow.com/questions/58237736/how-to-do-deformations-in-opencv
    radius = 30
    power = 1.6 # >1.0 for expansion, <1.0 for shrinkage
    height, width, _ = img.shape
    map_y = np.zeros((height,width),dtype=np.float32)
    map_x = np.zeros((height,width),dtype=np.float32)

    # create index map
    for i in range(height):
        for j in range(width):
            map_y[i][j]=i
            map_x[i][j]=j  
    # deform around the right eye
    for i in range (-radius, radius):
        for j in range(-radius, radius):
            if (i**2 + j**2 > radius ** 2):
                continue

            if i > 0:
                map_y[y + i][x + j] = y + (i/radius)**power * radius
            if i < 0:
                map_y[y + i][x + j] = y - (-i/radius)**power * radius
            if j > 0:
                map_x[y + i][x + j] = x + (j/radius)**power * radius
            if j < 0:
                map_x[y + i][x + j] = x - (-j/radius)**power * radius

    warped=cv.remap(img,map_x,map_y,cv.INTER_LINEAR)
    return warped
    