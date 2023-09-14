import tkinter as tk
import customtkinter
import subprocess
import pygame
from PIL import Image, ImageTk

# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Morpion")


def executer_multiplayer():
    button_song()
    subprocess.Popen(["python", "./Morpion/twoplayer.py"])
    fenetre.destroy()

def executer_morpionia():
    button_song()
    subprocess.Popen(["python", "./Morpion/morpionIA.py"])
    fenetre.destroy()
    
def main_song():
    # Charger le fichier audio
    sound = pygame.mixer.Sound("./images/swing.mp3")

    # Jouer le fichier audio sur le deuxième canal
    channel.play(sound)
def button_song():
    # Charger le fichier audio
    sound = pygame.mixer.Sound("./images/interface.mp3")

    # Jouer le fichier audio sur le deuxième canal
    channel1.play(sound)
    
main_font = customtkinter.CTkFont(family="Helvetica", size=12)
params1 = {
    'font' : main_font,
    'text_color' : "#68aec9",
    'hover' : True,
    'hover_color' : "black",
    'height' : 40,
    'width' : 120,
    'border_width' : 1,
    'corner_radius' : 10,
    'border_color' : "#68aec9",
    'bg_color' : "#262626",
    'fg_color' : "#262626"
    }


# Créer le canevas à l'intérieur de la fenêtre
canvas = tk.Canvas(fenetre, width=600, height=500, bg="white")
canvas.pack()
pygame.mixer.init()
channel = pygame.mixer.Channel(0)
channel1 = pygame.mixer.Channel(1)
main_song()
# Charger l'image
image_fond = Image.open("./images/Ajo.png")

# Redimensionner l'image de fond à la taille souhaitée
new_size_fond = (600, 500)  # Remplacez width et height par les dimensions désirées
resized_image_fond = image_fond.resize(new_size_fond)

# Créer un objet PhotoImage à partir de l'image redimensionnée de fond
photo_fond = ImageTk.PhotoImage(resized_image_fond)

# Créer l'image de fond dans le canevas
fond = canvas.create_image(0, 0, image=photo_fond, anchor=tk.NW)

boutons = customtkinter.CTkButton(canvas, text="DEUX JOUEURS", **params1,command=executer_multiplayer)
boutons.place(x=250,y=255)
bouton1 = customtkinter.CTkButton(canvas, text="DEBUTANT", **params1)
bouton1.place(x=250,y=350)
bouton2 = customtkinter.CTkButton(canvas, text="EXPERT", **params1,command=executer_morpionia)
bouton2.place(x=250,y=420)

# Exécuter la boucle principale de la fenêtre
fenetre.mainloop()
