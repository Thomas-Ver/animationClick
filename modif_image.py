#!/bin/python3.10 
# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

def get_carre_coords(img, x, y):
    """
    Prend l'image et les coordonnées du clic, et retourne les coordonnées du carré autour du clic si possible.

    Args:
        img (numpy.ndarray): L'image sur laquelle opérer.
        x (int): Coordonnée x du clic.
        y (int): Coordonnée y du clic.

    Returns:
        tuple: Coordonnées de début et de fin du carré (x_start, y_start, x_end, y_end).
    """
    x_start = max(0, x - 50)
    y_start = max(0, y - 50) 
    x_end = min(img.shape[1], x + 50)
    y_end = min(img.shape[0], y + 50)
    return x_start, y_start, x_end, y_end

def carre_noir(img, x, y):
    """
    Prend l'image et les coordonnées du clic, et retourne l'image avec un carré noir autour du clic.

    Args:
        img (numpy.ndarray): L'image sur laquelle opérer.
        x (int): Coordonnée x du clic.
        y (int): Coordonnée y du clic.

    Returns:
        numpy.ndarray: L'image modifiée.
    """
    x_start, y_start, x_end, y_end = get_carre_coords(img, x, y)
    img[y_start:y_end, x_start:x_end] = np.zeros((y_end - y_start, x_end - x_start))
    return img

def random_mult(img, x, y):
    """
    Prend l'image et les coordonnées du clic, et retourne l'image avec une multiplication aléatoire autour du clic.

    Args:
        img (numpy.ndarray): L'image sur laquelle opérer.
        x (int): Coordonnée x du clic.
        y (int): Coordonnée y du clic.

    Returns:
        numpy.ndarray: L'image modifiée.
    """
    x_start, y_start, x_end, y_end = get_carre_coords(img, x, y)
    M = np.random.rand(y_end - y_start, x_end - x_start)
    img[y_start:y_end, x_start:x_end] = img[y_start:y_end, x_start:x_end] * M
    return img