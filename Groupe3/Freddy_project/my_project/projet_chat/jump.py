import tkinter as tk
from PIL import ImageTk, Image
import subprocess
import pygame
import customtkinter
import random

class BackgroundMovement:
    def __init__(self, fenetre):
        self.fenetre = fenetre
        #création canvas
        self.canvas = tk.Canvas(self.fenetre, width=600, height=500)
        self.canvas.pack()

        #entrer l'image de l'arrière plan
        self.image = Image.open("../Image/Space.jpg")
        self.image = self.image.resize((600, 750))
        self.image = ImageTk.PhotoImage(self.image)
        self.fond = self.canvas.create_image(300, 200, anchor=tk.CENTER, image=self.image)

        self.background_image1 = Image.open("../Image/pink_space.jpg")
        self.background_image1 = self.background_image1.resize((600, 350))
        self.background_image1 = ImageTk.PhotoImage(self.background_image1)

        self.background_image2 = Image.open("../Image/pink_space.jpg")
        self.background_image2 = self.background_image2.resize((600, 350))
        self.background_image2 = ImageTk.PhotoImage(self.background_image2)

        #création de l'image de l'arrière plan
        self.background1 = self.canvas.create_image(0, 70, anchor="nw", image=self.background_image1)
        self.background2 = self.canvas.create_image(480, 70, anchor="nw", image=self.background_image2)
        self.background3 = self.canvas.create_image(900, 70, anchor="nw", image=self.background_image2)

        #initialisation de tous les variables nécessaires
        self.x = 520
        self.y = 385
        self.x_player = 100
        self.y_player = 400
        self.player_speed = 80
        self.player_speed_down = 80
        self.score = 0

        #création de l'oval pour les utilisateurs
        self.user = Image.open("../Image/robot.png")
        self.user_resize = self.user.resize((50, 50))
        self.user_final = ImageTk.PhotoImage(self.user_resize)
        self.user = self.canvas.create_image(self.x_player, self.y_player, image=self.user_final)

        #affichage de score
        self.label_score = tk.Label(self.canvas, text="Score : {}".format(self.score))
        self.label_score.place(rely=0.05, relx=0.05)

        #appel au fonction pour lancer automatique le mouvement de l'arrière plan et les rectanglees
        self.canvas.bind("<Configure>", self.start_movement)

        #appel au fonction pour le mouvement de l'oval de l'utilisateur, on utilise la touche "espace" et la touche "v"
        self.canvas.bind("<KeyPress>", self.move_player)
        self.canvas.bind("<space>", self.move_player)
        self.canvas.focus_set()

        self.create_obs()

        #dictionnaire pour la forme de bouton
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

        #création de bouton retour et sa position
        self.boutton_quitter = customtkinter.CTkButton(self.canvas, text="BACK", **self.Button_Style, command=self.back)
        self.boutton_quitter.place(relx=0.75, rely=0.05)
        # initialisation de music
        pygame.init()
        self.channel1=pygame.mixer.Channel(1)

    def music_play1(self):
        self.music = pygame.mixer.Sound("../Music/coin.mp3")
        self.music.set_volume(30.0)
        self.channel1.play(self.music)

    def back(self): #fonction pour pour revenir à la fenetre de liste de l'application
        self.music_play1()
        subprocess.Popen(["python", "./all_application.py"])
        self.fenetre.destroy()

        #fonction pour appeler les deux fonctions pour bouger les rectangles et l'arrière plan
    def start_movement(self, event):
        self.move_background()
        self.move_rectangle()

        #fonction pour faire bouger l'arrière plan
    def move_background(self):
        try:
            self.canvas.move(self.background1, -2, 0) #on bouge l'arrière plan suivant x avec une vitesse 2
            self.canvas.move(self.background2, -2, 0)
            self.canvas.move(self.background3, -2, 0)

            if self.canvas.coords(self.background1)[0] <= -500: #condition si la valeur de x est inferieur ou égal à -500 en on retourne à 1000 le valeur de x
                self.canvas.move(self.background1, 1000, 0)

            if self.canvas.coords(self.background2)[0] <= -500:
                self.canvas.move(self.background2, 1000, 0)

            if self.canvas.coords(self.background3)[0] <= -500:
                self.canvas.move(self.background3, 1000, 0)

            self.fenetre.after(10, self.move_background) #on donne la durée du mouvement et on appelle la fonction pour qu'il fonctionne inéfiniment
        except:
            pass

    #fonction pour le commande de l'oval et les touches nécessaires
    def move_player(self, event): #ici on met une condition si on presse la touche espace il monte et il tombe après
        try:
            if event.keysym == "space": #on utilise la touche espace si l'obstacle est courte
                self.move_up()
                self.music_play1()
                self.canvas.after(500, self.move_down)
                self.score += 1
                self.label_score = tk.Label(self.canvas, text="Score : {}".format(self.score))
                self.label_score.place(rely=0.05, relx=0.05)

        except:
            pass

    def move_up(self): #fonction pour monter pour la touche espace
        self.y_player -= self.player_speed
        self.canvas.coords(self.user, self.x_player, self.y_player)

    def move_down(self): #fonction pour tomber pour la touche espace
        self.y_player += self.player_speed_down
        self.canvas.coords(self.user, self.x_player, self.y_player)

    def move_up_up(self): #fonction pour monter pour la touche v
        self.y_player += self.player_speed+50
        self.canvas.coords(self.user, self.x_player, self.y_player)

    def move_down_down(self): #fonction pour tomber pour la touche v
        self.y_player -= self.player_speed+50
        self.canvas.coords(self.user, self.x_player, self.y_player)

    def create_obs(self):
        # création de la rectangle pour les obstacles
        self.obstacle1 = Image.open("../Image/bouche_incendie.png")
        self.obstacle1_resize = self.obstacle1.resize((30, 70))
        self.obstacle1_final = ImageTk.PhotoImage(self.obstacle1_resize)
        self.obs1 = self.canvas.create_image(self.x + 200, self.y, image=self.obstacle1_final)

        self.obstacle2 = Image.open("../Image/bouche_incendie.png")
        self.obstacle2_resize = self.obstacle2.resize((30, 70))
        self.obstacle2_final = ImageTk.PhotoImage(self.obstacle2_resize)
        self.obs2 = self.canvas.create_image(self.x + 500, self.y, image=self.obstacle2_final)

        self.obstacle3 = Image.open("../Image/bouche_incendie.png")
        self.obstacle3_resize = self.obstacle3.resize((30, 70))
        self.obstacle3_final = ImageTk.PhotoImage(self.obstacle3_resize)
        self.obs3 = self.canvas.create_image(self.x + 900, self.y, image=self.obstacle3_final)

    def move_rectangle(self): #fonction pour la mouvement du rectangle
        try:
            if self.score<=10:
                self.canvas.move(self.obs1, -2, 0)
                self.canvas.move(self.obs2, -2, 0)
                self.canvas.move(self.obs3, -2, 0)
            else:
                self.canvas.move(self.obs1, -3, 0)
                self.canvas.move(self.obs2, -3, 0)
                self.canvas.move(self.obs3, -3, 0)

            self.x1 = self.canvas.coords(self.obs1)[0] #on reprend la valeur de la rectangle selon ça déplacement
            self.x2 = self.canvas.coords(self.obs2)[0]
            self.x3 = self.canvas.coords(self.obs3)[0]

            if (self.x_player+20>=self.x1 and self.x_player<=self.x1+20) and self.y_player>=self.y: #condition pour la collision
                subprocess.Popen(["python ", "./game_over.py"]) #ouverture de nouvelle fenetre s'il l'oval rencontre une obstacle
                self.fenetre.destroy() #on detruit la fenetre
            elif self.x1 <= -50:
                self.canvas.move(self.obs1, 520, 0)



            if (self.x_player+2>=self.x2 and self.x_player<=self.x2+20) and self.y_player>=self.y: #condition pour la collision
                subprocess.Popen(["python ", "./game_over.py"]) #ouverture de nouvelle fenetre s'il l'oval rencontre une obstacle
                self.fenetre.destroy() #on detruit la fenetre
            elif self.x2 <= -50:
                self.canvas.move(self.obs2, 520, 0)


            if (self.x_player+20>=self.x3 and self.x_player<=self.x3+20) and self.y_player>=self.y: #condition pour la collision
                subprocess.Popen(["python ", "./game_over.py"]) #ouverture de nouvelle fenetre s'il l'oval rencontre une obstacle
                self.fenetre.destroy() #on detruit la fenetre
            elif self.x3 <= -50:
                self.canvas.move(self.obs3, 520, 0)

            self.fenetre.after(10, self.move_rectangle)
        except:
            pass

fenetre = tk.Tk()
background_movement = BackgroundMovement(fenetre)

#création de fenetre
fenetre.geometry("600x500")
fenetre.title("K'ilalao")
fenetre.iconbitmap("../Image/chat.ico")
fenetre.resizable(False, False)
fenetre.mainloop()

