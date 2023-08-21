import tkinter as tk
from PIL import ImageTk, Image
import subprocess
from tkinter import messagebox
import customtkinter
import pygame

fenetre = tk.Tk() #création de fenetre
fenetre.title("K'ilalao") #initialisation de titre
fenetre.iconbitmap("../Image/chat.ico") #insertion d'icon
fenetre.geometry("600x500") #initialisation de taille de la fenetre
fenetre.resizable(False, False)

image = Image.open("../Image/main_fond.jpg") #on prend l'image depuis le dossier
image_resized = image.resize((600,500)) #on configure la taille de l'image en suivant la taille de la fenetre
photo = ImageTk.PhotoImage(image_resized) #on met l'image dans un variable

label_main= tk.Label(fenetre, image=photo)
label_main.pack()

canvas=tk.Canvas(fenetre, width=600, height=500)
canvas.pack()

#on crée une dictionnaire pour la forme du bouton
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


pygame.init()
channel1 = pygame.mixer.Channel(1)

def music_play1():
    music = pygame.mixer.Sound("../Music/clique.mp3")
    music.set_volume(30.0)
    channel1.play(music)

#fonction pour retourner à la fenetre precedente
def back():
    music_play1()
    subprocess.Popen(["python", "./main_hunter.py"])
    fenetre.withdraw()

#fonction pour aller vers la fenetre de jeu chat
def good_hunter():
    music_play1()
    subprocess.Popen(["python", "./good_hunter.py"])
    fenetre.withdraw()

#fonction pour aller vers la fenetre de jeu jump
def escape():
    music_play1()
    subprocess.Popen(["python", "./jump.py"])
    fenetre.destroy()

#fonction pour ouvrir la fenetre de jeu jet
def jet():
    music_play1()
    subprocess.Popen(["python", "./jet.py"])
    fenetre.withdraw()

#fonction pour aller vers la fenetre de jeu jump
def car():
    music_play1()
    subprocess.Popen(["python", "./car.py"])
    fenetre.withdraw()


def Help():
    messagebox.showinfo("Fanampina :",
                        "Eto amin'ity takelaka ity ianao dia mahita bokotra maromaro : "
                        "1- Kcat = io no tsindrina raha hilalao ilay kilalao saka kely manenjika voalavo. \nCliquer ça si on veut jour le chat qui attrape le souris. \n"
                        "Push this if you want to play the cat who catch the mouse.\n\n"
                        "2- Kjump= io no tsindrina raha hilalao ilay baolina kely mitsambikina. \nCliquer ça si on veut jouer le petit ballon. \n"
                        "Push this if you want to play the small ball."
                        )

def about():
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

option_menu.add_separator()#création de ligne de séparation entre le deux option
option_menu.add_command(label="About", command=about)

menu_bar.add_cascade(label="Option", menu=option_menu)#création de cascade dans la bare de fenetre en haut à gauche avec son nom option


boutton_jump = customtkinter.CTkButton(fenetre,text="Kjump",**Button_Style, command=escape)#création de bouton kjump
boutton_jump.place(relx=0.2, rely=0.25)

boutton_jump = customtkinter.CTkButton(fenetre,text="Kjet",**Button_Style, command=jet)#création de bouton kjump
boutton_jump.place(relx=0.6, rely=0.25)

boutton_chasseur = customtkinter.CTkButton(fenetre,text="Kcar",**Button_Style, command=car) #création de bouton kcat
boutton_chasseur.place(relx=0.2, rely=0.45)

boutton_chasseur = customtkinter.CTkButton(fenetre,text="Kcat",**Button_Style, command=good_hunter) #création de bouton kcat
boutton_chasseur.place(relx=0.6, rely=0.45)

boutton_back = customtkinter.CTkButton(fenetre,text="BACK",**Button_Style, command=back) #création de bouton back
boutton_back.place(relx=0.39, rely=0.85)

fenetre.mainloop()