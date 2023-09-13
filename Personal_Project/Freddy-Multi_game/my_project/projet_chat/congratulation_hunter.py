import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import customtkinter
import subprocess
import pygame

#création de titre et définition de son titre avec l'insertion de l'icône
fenetre = tk.Tk()
fenetre.title("K'ilalao")
fenetre.iconbitmap("../Image/chat.ico")
fenetre.resizable(False, False)

canvas = tk.Canvas(fenetre, width=600, height=500) #création canvas
canvas.pack()

#initialisation de music
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
#insertion d'image
image = Image.open("../Image/congratulations.webp")
image = image.resize((600, 600))
image = ImageTk.PhotoImage(image)
fond = canvas.create_image(300, 300, anchor=tk.CENTER, image=image) #création d'image pour le fond

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

def game(): #fonction pour rejouer
    music_play1()
    subprocess.Popen(["python", "./good_hunter.py"])
    fenetre.destroy()

def back(): #fonction pour quitter
    music_play1()
    subprocess.Popen(["python", "./all_application.py"])
    fenetre.destroy()

#bouton play again
boutton_commencer = customtkinter.CTkButton(fenetre,text="PLAY AGAIN",**Button_Style, command=game)
boutton_commencer.place(relx=0.45, rely=0.8)

#bouton quitter
boutton_quitter = customtkinter.CTkButton(fenetre,text="BACK", **Button_Style, command=back)
boutton_quitter.place(relx=0.01, rely=0.8)

def Help(): #message pour aider les utilisateurs
    messagebox.showinfo("Fanampina:",
                        "Ity ary ny fomba arahana raha te-hilalao : "
                        "Misy bokotra roa ato amin'ny takelaka ity ny iray voalohany START na hoe MANOMBOKA, \nizany hoe io no tsindrina raha hilalao.\n"
                        "Faharoa ny bokotra EXIT na hoe MIALA io no tsindrina raha toa kosa ka tsy hilalao intsony. \n\n"
                        "Voici le règlement à suivre si vous voulez jouer : \n"
                        "Il y a deux bouton sur cette fenetre. \n"
                        "Premièrement le bouton START ou COMMENCER, il suffit de le presser si on veut jouer.\n"
                        "Deuxièmement le bouton EXIT ou QUITTER, il suffit de le presser si on veut quitter le jeu.\n\n"
                        "Here is the reglement that you should follow if you want to play :\n"
                        "There are two button in this window.\n"
                        "Firstly, the button START for beginning the game.\n"
                        "Secondly, the button EXIT for leaving the game.\n")

def About(): #à propos de l'application
    messagebox.showinfo("Mombamomba:\n",
                        "Ity kilalao ity dia notantarahan'i Freddy ANDRIAMANOHINIAINA Herison Jean Freddy izay pianatra mahakasika ny "
                        "Développement Mobile, izy io dia liana tamin'izany resaka kilalao izany ary ny tanjony dia ny hahavita kilalao iray"
                        "malaza eran-tany. Noho izany tanjony izany dia namorona ity kilalao ity izy. Izay mbola vao version voalohany aloha hatreto "
                        "Izy ity dia vita ny 21 jolay 2023. Ary nomeny ny anarana hoe : K'ilalao.\n\n"
                        "Cette application a été créé par Freddy ANDRIAMANOHINIAINA Herison Jean Freddy, étudiant de la Développement Mobile. "
                        "Il était très intéresé par les jeux vidéos. Il avait d'ambition de créer un jeu célébre dans tout le monde entier. Grâce à son "
                        "ambition, il a commencé déjà à créer cette jeu. Elle etait juste le premièr version."
                        "Elle est fini le 21 juillet 2023. Il donne un nom pour son jeu : K'ilalao.\n\n"
                        "This game was created by Freddy ANDRIAMANOHINIAINA Herison Jean Freddy, he was a student in Mobile Developpement, he was"
                        "interested in the video game and his aim was to create a video game famous in the world. Because of his aim that he create this game."
                        " This is a first version."
                        "This game was finished on 21 julley 2023 and her name is : K'illao.\n\n")

menu_bar = tk.Menu(fenetre) #initialisation de la création de menu
fenetre.config(menu=menu_bar)

option_menu = tk.Menu(menu_bar, tearoff=0) #création des options dans la barre de fenetre
option_menu.add_command(label="Help", command=Help)#ajout de commande dans l'option

option_menu.add_separator() #création de ligne de séparation entre le deux option
option_menu.add_command(label="About", command=About)

menu_bar.add_cascade(label="Option", menu=option_menu)#création de cascade dans la bare de fenetre en haut à gauche avec son nom option


fenetre.mainloop()