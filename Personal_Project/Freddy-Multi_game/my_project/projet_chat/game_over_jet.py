import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import customtkinter
import subprocess
import pygame

fenetre = tk.Tk()
fenetre.title("K'ilalao")
fenetre.iconbitmap("../Image/chat.ico")
fenetre.resizable(False, False)
#création de canvas
canvas = tk.Canvas(fenetre, width=600, height=500)
canvas.pack()

#insertion d'image
image = Image.open("../Image/game_over.jpg") #on prend l'image dans son emplacement
image = image.resize((600, 600)) #on change sa forme si nécessaire
image = ImageTk.PhotoImage(image) #on déclare l'image dans un variable
fond = canvas.create_image(300, 200, anchor=tk.CENTER, image=image) #création de l'image et definit sa position

def music_play():
    music = pygame.mixer.Sound("../Music/toystory.mp3")
    channel.play(music)
    music.set_volume(0.50)

def music_play1():
    music = pygame.mixer.Sound("../Music/clique.mp3")
    music.set_volume(30.0)
    channel1.play(music)

pygame.init()
channel=pygame.mixer.Channel(0)
music_play()
channel1 = pygame.mixer.Channel(1)

#création de dictionnaire pour la forme de chaque bouton et sa couleur
Button_Style = {
    "text_color": "#eda850",
    "hover": True,
    "hover_color": "gray25",
    "height": 40,
    "width": 120,
    "border_width": 2,
    "corner_radius": 3,
    "border_color": "SteelBlue1",
    "bg_color": "#262626",
    "fg_color": "#262626"
}

def jet(): #fonction si on veut jouer encore
    music_play1()
    subprocess.Popen(["python", "./jet.py"])
    fenetre.destroy()

def back(): #fonciton si l'utilisateur veut quitter
    music_play1()
    subprocess.Popen(["python", "./all_application.py"])
    fenetre.destroy()

boutton_commencer = customtkinter.CTkButton(fenetre,text="PLAY AGAIN",**Button_Style, command=jet) #bouton si pour rejouer et appelle au fonction game
boutton_commencer.place(relx=0.45, rely=0.8)

boutton_quitter = customtkinter.CTkButton(fenetre,text="BACK", **Button_Style, command=back)#bouton pour quitter et appelle au fonction quitter
boutton_quitter.place(relx=0.01, rely=0.8)


def Help():
    if messagebox.askyesno("Confirmation", "Vous voulez vraiment quitter?"):
        fenetre.destroy()

def About():
    if messagebox.askyesno("Confirmation", "Vous voulez vraiment quitter?"):
        fenetre.destroy()

menu_bar = tk.Menu(fenetre) #initialisation de la création de menu
fenetre.config(menu=menu_bar)

option_menu = tk.Menu(menu_bar, tearoff=0) #création des options dans la barre de fenetre
option_menu.add_command(label="Help", command=Help) #ajout de commande dans l'option

option_menu.add_separator() #création de ligne de séparation entre le deux option
option_menu.add_command(label="About", command=About)

menu_bar.add_cascade(label="Option", menu=option_menu) #création de cascade dans la bare de fenetre en haut à gauche avec son nom option

fenetre.mainloop()
