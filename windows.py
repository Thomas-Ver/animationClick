#!/bin/python3.10 
import tkinter as tk
from PIL import Image, ImageTk
import cv2 as cv
import numpy as np

# Création de la fenêtre principale
root = tk.Tk()
root.title("Fenêtre d'Interaction avec l'Image")

# Charger l'image avec Pillow
image_path = "mandel.jpg"  # Remplace par le chemin de ton image
imageio = cv.imread(image_path)
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)

# Créer un canvas et afficher l'image
canvas = tk.Canvas(root, width=image.width, height=image.height)
canvas.pack()
image_container = canvas.create_image(0, 0, anchor="nw", image=photo)

# Conserver une référence à l'image pour éviter qu'elle soit supprimée par le garbage collector
canvas.image = photo

# Fonction pour restaurer l'image originale
def restore_image():
    canvas.itemconfig(image_container, image=photo)
    canvas.image = photo

# Fonction appelée lors d'un clic sur l'image
def on_click(event):
    imodif = imageio.copy()
    x, y = event.x, event.y
    print(f"Clic détecté aux coordonnées : {x}, {y}")
    
    # Noircir un carré de 100x100 pixels autour du clic
    x_start = max(0, x - 50)
    y_start = max(0, y - 50)
    x_end = min(imageio.shape[1], x + 50)
    y_end = min(imageio.shape[0], y + 50)
    
    ### MULTIPLICATION AVEC  matrice random: ###

    #M=np.random.rand(y_end - y_start, x_end - x_start)
    #imodif[y_start:y_end, x_start:x_end] = imodif[y_start:y_end, x_start:x_end]*M

    ### JUSTE 0 PARTOUR NULL: ###
    #imodif[y_start:y_end, x_start:x_end] = np.zeros((y_end - y_start, x_end - x_start))
    
    ### TENTATIVE DEFORMATION ### : https://stackoverflow.com/questions/58237736/how-to-do-deformations-in-opencv
    input_pts = np.array([[x_start, y_start], [x_end, y_start], [x_end, y_end], [x_start, y_end]])
    output_pts = np.array([[x_start, y_end],[x_start, y_start], [x_end, y_start], [x_end, y_end]])
    M=cv.getPerspectiveTransform(input_pts, output_pts)
    imodif = cv.warpPerspective(imodif, M, (imodif.shape[1], imodif.shape[0]))
    

    imagem = Image.fromarray(imodif)
    photom = ImageTk.PhotoImage(imagem)
    
    # Mettre à jour l'image sur le canvas
    canvas.itemconfig(image_container, image=photom)
    
    # Conserver une référence à l'image pour éviter qu'elle soit supprimée par le garbage collector
    canvas.image = photom

    # Restaurer l'image originale après 2 secondes (2000 millisecondes)
    root.after(2000, restore_image)

# Associer l'événement de clic au canvas
canvas.bind("<Button-1>", on_click)

# Lancer la boucle principale de la fenêtre
root.mainloop()

