import tkinter as tk
import imageio
import numpy as np
from PIL import Image, ImageTk
import subprocess
import pygame
import customtkinter as ctk

def executer_script():
    subprocess.Popen(["python", "./Tank/principal.py"])
    fenetre.destroy()

def update_image():
    global gif_index
    gif_index += 1
    if gif_index >= gif_length:
        gif_index = 0
    img = Image.fromarray(gif[gif_index])
    photo = ImageTk.PhotoImage(img)
    label_image.configure(image=photo)
    label_image.image = photo
    fenetre.after(100, update_image) 

fenetre = ctk.CTk()
fenetre.geometry("400x300")
fenetre.title("Tank game")

pygame.mixer.init()
pygame.mixer.music.load("./images/honor.mp3")
pygame.mixer.music.play(-1)

reader = imageio.get_reader("./images/drible_tank.gif")
#ouvrir l'image
gif = []#creation de liste gif
#Ajout de chaque partie de l'image dans une liste qui s'appelle gif
for frame in reader:
    gif.append(frame)#ajouter l'image dans le liste par le boucle
gif_length = len(gif)#Affecter la taille du liste gif dans le variable gif_length
gif_index = -1  #initialisation des indice



# redimensionner l'image
nouvelle_largeur = 400
nouvelle_hauteur = 300


# Parcourir chaque image du liste GIF
for i in range(gif_length):
    # Ouvrir l'image avec Pillow
    image = Image.fromarray(gif[i])
    
    # Redimensionner l'image
    image_redimensionnee = image.resize((nouvelle_largeur, nouvelle_hauteur),  Image.BILINEAR)
    
    # Enregistrer l'image redimensionnée dans la liste gif
    gif[i] = np.array(image_redimensionnee)



"""Création des boutons et label"""
#Création du bouton et des labels
label_image = tk.Label(fenetre)
label_image.place(x=0, y=0)

label_texte = tk.Label(fenetre, text="TANK GAME", bg='light grey', font=('ds-digital', 26), fg='navy')
label_texte.place(x=120, y=60)

bouton_jouer = tk.Button(fenetre, text="Jouer", command=executer_script)
bouton_jouer.place(x=180, y=210)

bouton_quitter = tk.Button(fenetre, text="Quitter", command=fenetre.quit)
bouton_quitter.place(x=180, y=240)

update_image()
fenetre.protocol("WM_DELETE_WINDOW", pygame.mixer.music.stop)
fenetre.mainloop()
