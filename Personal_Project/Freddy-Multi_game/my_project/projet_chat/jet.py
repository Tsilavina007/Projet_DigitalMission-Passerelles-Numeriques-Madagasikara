import tkinter as tk
from PIL import ImageTk, Image
import random
import subprocess
import pygame
import customtkinter
from tkinter import messagebox

class fish(object):
    def __init__(self,can):
        self.window=window
        #initialisation de tous les variables nécesssaires
        self.canvas = can
        self.canvas_width=600
        self.canvas_height=500
        # dictionnaire pour la création de la forme du bouton
        self.x=100
        self.y=0
        self.x1 = 500
        self.y1 = 0
        self.x2 = 250
        self.y2 = 0
        self.x3 = 470
        self.y3 = 0
        self.x_player=200
        self.y_player=450
        self.speed=10
        self.score=0

        #insertion image
        self.user = Image.open("../Image/robot.png")
        self.user_resize = self.user.resize((50, 50))
        self.user_final = ImageTk.PhotoImage(self.user_resize)
        self.user=self.canvas.create_image(self.x_player, self.y_player, image=self.user_final)


        self.argent = Image.open("../Image/argentpng.png")
        self.argent_resize = self.argent.resize((70, 70))
        self.argent_final = ImageTk.PhotoImage(self.argent_resize)
        self.argent = self.canvas.create_image(self.x, self.y, image=self.argent_final)

        self.dynamite1 = Image.open("../Image/dynamite1.png")
        self.dynamite1_resize = self.dynamite1.resize((70, 70))
        self.dynamite1_final = ImageTk.PhotoImage(self.dynamite1_resize)
        self.dyna1 = self.canvas.create_image(self.x+200, self.y, image=self.dynamite1_final)

        self.dynamite2 = Image.open("../Image/dynamite2.png")
        self.dynamite2_resize = self.dynamite2.resize((70, 70))
        self.dynamite2_final = ImageTk.PhotoImage(self.dynamite2_resize)
        self.dyna2 = self.canvas.create_image(self.x+300, self.y, image=self.dynamite2_final)

        self.dynamite3 = Image.open("../Image/dynamite1.png")
        self.dynamite3_resize = self.dynamite3.resize((70, 70))
        self.dynamite3_final = ImageTk.PhotoImage(self.dynamite1_resize)
        self.dyna3 = self.canvas.create_image(self.x + 400, self.y, image=self.dynamite3_final)


        self.label_score = tk.Label(self.canvas, text="Score : {}".format(self.score))
        self.label_score.place(rely=0.05, relx=0.05)

        can.bind("<Motion>", self.move_player)
        can.focus_set()

        self.move_bombe()

        pygame.init()
        self.channel1= pygame.mixer.Channel(1)

        self.Button_Style = {
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

        # bouton pour quitter et sa position
        self.boutton_quitter = customtkinter.CTkButton(self.canvas, text="BACK", **self.Button_Style, command=self.back)
        self.boutton_quitter.place(relx=0.75, rely=0.03)

    def boom(self):
        self.explosion = Image.open("../Image/explosion.png")
        self.explosion_resize = self.explosion.resize((100, 100))
        self.explosion_final = ImageTk.PhotoImage(self.explosion_resize)
        self.boom = self.canvas.create_image(self.x_player, self.y_player, image=self.explosion_final)
        subprocess.Popen(["python", "./game_over_jet.py"])
        self.canvas.after(5000, self.window.destroy())

    def music_play1(self):
        self.music = pygame.mixer.Sound("../Music/coin.mp3")
        self.music.set_volume(30.0)
        self.channel1.play(self.music)

    def move_player(self,event):
        self.x_player = event.x  # Déplacer le rectangle vers la position horizontale de la souris
        # Assurer que le rectangle ne dépasse pas les limites du canvas
        if self.x_player < 50:
            self.x_player = 50
        elif self.x_player > self.canvas_width - 50:
            self.x_player = self.canvas_width - 50

        canvas.coords(self.user, self.x_player, self.y_player)

    def create_bombe(self):
        self.x_min, self.x_max = 70, 570
        self.y=-70
        self.x = random.randint(self.x_min, self.x_max)
        self.argent= self.canvas.create_image(self.x, self.y, image=self.argent_final)

        self.x1_min, self.x1_max = 70, 200
        self.y1=0
        self.x1 = random.randint(self.x1_min, self.x1_max)
        self.dyna1 = self.canvas.create_image(self.x1, self.y1, image=self.dynamite1_final)

        self.x2_min, self.x2_max = 230, 370
        self.y2_min, self.y2_max = -80, -70
        self.x2 = random.randint(self.x2_min, self.x2_max)
        self.y2 = random.randint(self.y2_min, self.y2_max) + 120
        self.dyna2= self.canvas.create_image(self.x2, self.y2, image=self.dynamite2_final)

        self.x3_min, self.x3_max = 430, 570
        self.y3_min, self.y3_max = -80, -70
        self.x3 = random.randint(self.x3_min, self.x3_max)
        self.y3 = random.randint(self.y3_min, self.y3_max)
        self.dyna3= self.canvas.create_image(self.x3, self.y3, image=self.dynamite3_final)

    def move_bombe(self):
        self.canvas.move(self.argent, 0, +1)
        self.y = self.canvas.coords(self.argent)[1]
        self.x = self.canvas.coords(self.argent)[0]
        if self.x_player+20 > self.x-20 and self.x_player < self.x+50 and self.y_player >= self.y and self.y_player <= self.y+20:
            self.score += 1
            self.label_score = tk.Label(self.canvas, text="Score : {}".format(self.score))
            self.label_score.place(rely=0.05, relx=0.05)
            self.music_play1()

        self.canvas.move(self.dyna1, 0, +1)
        self.y1 = self.canvas.coords(self.dyna1)[1]
        self.x1 = self.canvas.coords(self.dyna1)[0]
        if self.y1 >= 800:
            self.create_bombe()
        if self.score >= 100:
            self.canvas.move(self.argent, 0, +2)
            self.canvas.move(self.dyna1, 0, +2)
            self.canvas.move(self.dyna2, 0, +2)
            self.canvas.move(self.dyna3, 0, +2)
        elif self.score>=200:
            self.canvas.move(self.argent, 0, +3)
            self.canvas.move(self.dyna1, 0, +3)
            self.canvas.move(self.dyna2, 0, +3)
            self.canvas.move(self.dyna3, 0, +3)
        if self.x_player+20 > self.x1-20 and self.x_player < self.x1+50 and self.y_player >= self.y1 and self.y_player <= self.y1+20:
            self.boom()


        self.canvas.move(self.dyna2, 0, +1)
        self.y2 = self.canvas.coords(self.dyna2)[1]
        self.x2 = self.canvas.coords(self.dyna2)[0]
        if self.x_player+20 > self.x2-20 and self.x_player < self.x2+50 and self.y_player >= self.y2 and self.y_player <= self.y2+20:
            self.boom()

        self.canvas.move(self.dyna3, 0, +1)
        self.y3 = self.canvas.coords(self.dyna3)[1]
        self.x3 = self.canvas.coords(self.dyna3)[0]
        if self.x_player+20 > self.x3 and self.x_player < self.x3+50 and self.y_player >= self.y3 and self.y_player <= self.y3+20:
            self.boom()



        self.canvas.after(5, self.move_bombe)

    def back(self):  # fonction retour à la fenetre tout les applications
        subprocess.Popen(["python", "./all_application.py"])
        window.destroy()

if __name__ == '__main__':
    window= tk.Tk() #création de fenetre
    window.title("K'ilalao") #initialisation de titre
    window.geometry("600x500") #intialisation de sa taille
    window.iconbitmap("../Image/chat.ico") #insertion d'icon
    window.resizable(False, False)

    canvas_width = 600
    canvas_height = 500

    #création de canvas
    canvas = tk.Canvas(window, width=canvas_width, height=canvas_height)
    canvas.pack()

    #insertion de photo
    image=Image.open("../Image/ciel.jpg")
    image = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor=tk.NW, image=image)



    objet = fish(canvas)

    menu_bar = tk.Menu(window)#initialisation de la création de menu
    window.config(menu=menu_bar)


    def Help(): #message d'aide pour les utilisateurs
        messagebox.showinfo("Toromarika : ",
                            "Sakakely voalohany \ Premier chat \ First cat :"
                            "Up = miakatra, monter, up \ Down = midina, descendre, down \ Left = miakavy, à gauche, left \ Right = ankavana \ à droite \ right \n"
                            "Sakakely faharoa \ Deuxième chat \ Second cat :"
                            "z = miakatra, monter, up \ s = midina, descendre, down \ q = miakavy, à gauche, left \ d = ankavanana \ à droite \ right \n"
                            "Space = mampiseho ilay voalavo \ faire apparaître le petit souris \ to show the small mouse"
                            )


    def about(): #message concernant l'applicaiton et sa créateur
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


    option_menu = tk.Menu(menu_bar, tearoff=0) #création des options dans la barre de fenetre
    option_menu.add_command(label="Help", command=Help)#ajout de commande dans l'option

    option_menu.add_separator()#création de ligne de séparation entre le deux option
    option_menu.add_command(label="About", command=about)

    menu_bar.add_cascade(label="Option", menu=option_menu)#création de cascade dans la bare de fenetre en haut à gauche avec son nom option

    window.mainloop()