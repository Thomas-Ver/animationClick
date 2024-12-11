#!/bin/python3.10 
# -*- coding: utf-8 -*-
import tkinter as tk
from PIL import Image, ImageTk
import cv2 as cv
import numpy as np
import modif_image as modif

def restore_image():
    """
    Fonction pour restaurer l'image originale sur le canvas.
    """
    canvas.itemconfig(image_container, image=photo)
    canvas.image = photo

def on_click(event):
    """
    Fonction appelée lors d'un clic sur l'image. Modifie l'image en fonction du type d'animation choisi.

    Args:
        event (tkinter.Event): L'événement de clic contenant les coordonnées du clic.
    """
    imodif = imageCV.copy()
    x, y = event.x, event.y
    print(f"Clic détecté aux coordonnées : {x}, {y}")

    imodif = funmodif(imodif, x, y)

    imagem = Image.fromarray(imodif)
    photom = ImageTk.PhotoImage(imagem)

    canvas.itemconfig(image_container, image=photom) # Mettre à jour l'image sur le canvas
    canvas.image = photom # Conserver une référence à l'image pour éviter qu'elle soit supprimée par le garbage collector
 
    root.after(2000, restore_image)    # Restaurer l'image originale après 2 secondes

### ---- Main ---- ###

print("Choisir le type d'animation à appliquer sur l'image en cliquant dessus :")
print("1 - Déformation")
print("2 - Noircir")
print("3 - Multiplier par une matrice aléatoire")

choix = input(">")
if choix == "1":
    funmodif = modif.deform
elif choix == "2":
    funmodif = modif.carre_noir
elif choix == "3":
    funmodif = modif.random_mult
else:
    print("Choix invalide")
    exit()

root = tk.Tk() # Création de la fenêtre principale
root.title("Fenêtre principale") 

image_path = "assets/mandel.jpg"  
imageCV = cv.imread(image_path)[:,:,0] #on lit l'image avec opencv pour pouvoir la modifier 
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image) #charge l'image pour la print dans la fenêtre

canvas = tk.Canvas(root, width=image.width, height=image.height)
canvas.pack()
image_container = canvas.create_image(0, 0, anchor="nw", image=photo)

canvas.image = photo # Conservation de l'image 

canvas.bind("<Button-1>", on_click) # Associer l'événement de clic au canvas

root.mainloop() # Lancer la boucle principale de la fenêtre