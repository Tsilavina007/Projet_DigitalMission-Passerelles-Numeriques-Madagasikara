import tkinter as tk
from PIL import ImageTk, Image
import subprocess
from tkinter import messagebox
import customtkinter
import pygame

fenetre = tk.Tk() #création de fenetre
fenetre.title("K'ilalao") #initialisation de titre pour la fenetre
fenetre.iconbitmap("../Image/chat.ico") #insertion d'icon
fenetre.geometry("600x500")
fenetre.resizable(False, False)

#insertion d'image
image_main = Image.open("../Image/main_fond.jpg")
image_resized = image_main.resize((600,500))
photo_main = ImageTk.PhotoImage(image_resized)

label_main= tk.Label(fenetre, image=photo_main)
label_main.pack()

canvas=tk.Canvas(fenetre, width=600, height=500)
canvas.pack()

def music_play():
    music = pygame.mixer.Sound("../Music/ditsdit.mp3")
    channel.play(music)
    music.set_volume(0.10)
    canvas.after(20000, music_play)

def music_play1():
    music = pygame.mixer.Sound("../Music/clique.mp3")
    music.set_volume(30.0)
    channel1.play(music)

pygame.init()
channel=pygame.mixer.Channel(0)
music_play()
channel1 = pygame.mixer.Channel(1)

#création de dictionnaire pour la forme de bouton
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

menu_bar = tk.Menu(fenetre) ##initialisation de la création de menu
fenetre.config(menu=menu_bar)

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


def about(): #message concernant l'application et la créateur
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
                        "This game was finished on 21 julley 2023 and her name is : K'illao.\n\n"
                        )

option_menu = tk.Menu(menu_bar, tearoff=0)  #création des options dans la barre de fenetre
option_menu.add_command(label="Help", command=Help)#ajout de commande dans l'option

option_menu.add_separator()#création de ligne de séparation entre le deux option
option_menu.add_command(label="About", command=about)

menu_bar.add_cascade(label="Option", menu=option_menu)#création de cascade dans la bare de fenetre en haut à gauche avec son nom option


def game(): #fonction pour aller vers tout les applications
    music_play1()
    subprocess.Popen(["python", "./all_application.py"])
    fenetre.withdraw()

def quitter(): #fonction pour quitter
    music_play1()
    if messagebox.askyesno("Comfirmation!", "Vous voulez vraiment quitter?"):
        fenetre.destroy()

boutton_commencer = customtkinter.CTkButton(fenetre,text="START",**Button_Style, command=game) #création de bouton pour le fonction game
boutton_commencer.place(relx=0.39, rely=0.75)

boutton_quitter = customtkinter.CTkButton(fenetre,text="EXIT", **Button_Style, command=quitter) #création de bouton pour le fonction quitter
boutton_quitter.place(relx=0.39, rely=0.85)

fenetre.mainloop()