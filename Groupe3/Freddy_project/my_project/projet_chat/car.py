import tkinter as tk
from PIL import ImageTk, Image
import subprocess
import pygame
import customtkinter
import random

class BackgroundMovement:
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.x=100
        self.y=400
        self.score=0
        #création canvas
        self.canvas = tk.Canvas(self.fenetre, width=600, height=500)
        self.canvas.pack()

        self.background_image1 = Image.open("../Image/main_route.PNG")
        self.background_image1 = self.background_image1.resize((600, 500))
        self.background_image1 = ImageTk.PhotoImage(self.background_image1)

        self.car_volvo_image = Image.open("../Image/Car___Volvo.png")
        self.car_volvo_image = self.car_volvo_image.resize((70, 100))
        self.car_volvo_image = ImageTk.PhotoImage(self.car_volvo_image)

        self.car_Stola_image = Image.open("../Image/car_Stola.png")
        self.car_Stola_image = self.car_Stola_image.resize((70, 100))
        self.car_Stola_image = ImageTk.PhotoImage(self.car_Stola_image)

        self.car_red_image = Image.open("../Image/car_red.png")
        self.car_red_image = self.car_red_image.resize((70, 130))
        self.car_red_image = ImageTk.PhotoImage(self.car_red_image)

        self.car_coin_image = Image.open("../Image/argentpng.png")
        self.car_coin_image = self.car_coin_image.resize((70, 70))
        self.car_coin_image = ImageTk.PhotoImage(self.car_coin_image)

        self.car_user_image = Image.open("../Image/car_user.png")
        self.car_user_image = self.car_user_image.resize((70, 100))
        self.car_user_image = ImageTk.PhotoImage(self.car_user_image)

        self.car_exploison_image = Image.open("../Image/explosion.png")
        self.car_exploison_image = self.car_exploison_image.resize((70, 100))
        self.car_exploison_image = ImageTk.PhotoImage(self.car_exploison_image)

        #création de l'image de l'arrière plan
        self.background1 = self.canvas.create_image(0, -1000, anchor="nw", image=self.background_image1)
        self.background2 = self.canvas.create_image(0, -500, anchor="nw", image=self.background_image1)
        self.background3 = self.canvas.create_image(0, 0, anchor="nw", image=self.background_image1)

        self.car_volvo = self.canvas.create_image(self.x, 100, anchor="nw", image=self.car_volvo_image)
        self.car_Stola = self.canvas.create_image(self.x + 320, 100, anchor="nw", image=self.car_Stola_image)
        self.car_red = self.canvas.create_image(self.x + 160, -500, anchor="nw", image=self.car_red_image)
        self.car_Stola_1 = self.canvas.create_image(self.x, -500, anchor="nw", image=self.car_Stola_image)
        self.car_volvo_1 = self.canvas.create_image(self.x + 320, -1500, anchor="nw", image=self.car_volvo_image)
        self.car_coin = self.canvas.create_image(self.x + 320, -500, anchor="nw", image=self.car_coin_image)
        self.car_user = self.canvas.create_image(self.x, self.y, anchor="nw", image=self.car_user_image)

        #affichage de score
        self.label_score = tk.Label(self.canvas, text="Score : {}".format(self.score))
        self.label_score.place(rely=0.05, relx=0.05)

        self.canvas.bind("<KeyPress>", self.move_car_user)
        self.canvas.bind("<Left>", self.move_car_user)
        self.canvas.bind("<Right>", self.move_car_user)
        self.canvas.focus_set()

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
        self.channel2=pygame.mixer.Channel(2)
        self.start_movement()

    def music_play1(self):
        self.music = pygame.mixer.Sound("../Music/coin.mp3")
        self.music.set_volume(30.0)
        self.channel1.play(self.music)

    def music_play_explosion(self):
        self.music = pygame.mixer.Sound("../Music/explosion.mp3")
        self.music.set_volume(30.0)
        self.channel1.play(self.music)
        subprocess.Popen(["python", "game_over_car.py"])
        self.fenetre.destroy()

    def back(self): #fonction pour pour revenir à la fenetre de liste de l'application
        self.music_play1()
        subprocess.Popen(["python", "./all_application.py"])
        self.fenetre.destroy()

        #fonction pour appeler les deux fonctions pour bouger les rectangles et l'arrière plan
    def start_movement(self):
        self.move_background()
        self.move_car()



        #fonction pour faire bouger l'arrière plan
    def move_background(self):
        self.canvas.move(self.background1, 0, 1) #on bouge l'arrière plan suivant x avec une vitesse 2
        self.canvas.move(self.background2, 0, 1)
        self.canvas.move(self.background3, 0, 1)

        if self.canvas.coords(self.background1)[1] >= 500: #condition si la valeur de x est inferieur ou égal à -500 en on retourne à 1000 le valeur de x
            self.canvas.move(self.background1, 0, -1000)

        if self.canvas.coords(self.background2)[1] >= 500:
            self.canvas.move(self.background2, 0, -1000)

        if self.canvas.coords(self.background3)[1] >= 500:
            self.canvas.move(self.background3, 0, -1000)

        self.fenetre.after(10, self.move_background)


    def move_car(self):
        self.canvas.move(self.car_Stola, 0, 2)
        self.x_stola = self.canvas.coords(self.car_Stola)[0]
        self.y_stola = self.canvas.coords(self.car_Stola)[1]
        if self.y_stola+70 >= self.y and self.y_stola-70 <= self.y and self.x == self.x_stola:
            self.music_play_explosion()
            self.car_explosion = self.canvas.create_image(self.x , self.y-40, anchor="nw", image=self.car_exploison_image)
            subprocess.Popen(["python", "game_over_car.py"])
            self.fenetre.canvas.after_cancel(self.id)

        self.canvas.move(self.car_Stola_1, 0, 2)
        self.x_stola_1 = self.canvas.coords(self.car_Stola_1)[0]
        self.y_stola_1 = self.canvas.coords(self.car_Stola_1)[1]
        if self.y_stola_1 + 70 >= self.y and self.y_stola_1 - 70 <= self.y and self.x == self.x_stola_1:
            self.music_play_explosion()
            self.car_explosion = self.canvas.create_image(self.x, self.y - 40, anchor="nw",
                                                          image=self.car_exploison_image)
            self.fenetre.canvas.after_cancel(self.id)

        self.canvas.move(self.car_volvo, 0, 2)
        self.x_volvo = self.canvas.coords(self.car_volvo)[0]
        self.y_volvo = self.canvas.coords(self.car_volvo)[1]
        if self.y_volvo+70 >= self.y and self.y_volvo-70 <= self.y and self.x == self.x_volvo:
            self.music_play_explosion()
            self.car_explosion = self.canvas.create_image(self.x , self.y-40, anchor="nw", image=self.car_exploison_image)
            self.fenetre.canvas.after_cancel(self.id)

        self.canvas.move(self.car_volvo_1, 0, 2)
        self.x_volvo_1 = self.canvas.coords(self.car_volvo_1)[0]
        self.y_volvo_1 = self.canvas.coords(self.car_volvo_1)[1]
        if self.y_volvo_1 + 70 >= self.y and self.y_volvo_1 - 70 <= self.y and self.x == self.x_volvo_1:
            self.music_play_explosion()
            self.car_explosion = self.canvas.create_image(self.x, self.y - 40, anchor="nw",
                                                          image=self.car_exploison_image)
            self.fenetre.canvas.after_cancel(self.id)

        self.canvas.move(self.car_red, 0, 2)
        self.x_red = self.canvas.coords(self.car_red)[0]
        self.y_red = self.canvas.coords(self.car_red)[1]
        if self.y_red+130 >= self.y and self.y_red-70 <= self.y and self.x == self.x_red:
            self.music_play_explosion()
            self.car_explosion = self.canvas.create_image(self.x , self.y-40, anchor="nw", image=self.car_exploison_image)
            self.fenetre.canvas.after_cancel(self.id)



        self.canvas.move(self.car_coin, 0, 2)
        self.x_coin = self.canvas.coords(self.car_coin)[0]
        self.y_coin = self.canvas.coords(self.car_coin)[1]
        if self.y_coin+70 >= self.y and self.y_coin-70 <= self.y and self.x == self.x_coin:
            self.score+=1
            self.music_play1()
            self.label_score = tk.Label(self.canvas, text="Score : {}".format(self.score))
            self.label_score.place(rely=0.05, relx=0.05)


        if self.canvas.coords(self.car_Stola)[1] >= 500:
            self.canvas.move(self.car_Stola, 0, -1000)
        if self.canvas.coords(self.car_volvo)[1] >= 500:
            self.canvas.move(self.car_volvo, 0, -1000)
        if self.canvas.coords(self.car_red)[1] >= 500:
            self.canvas.move(self.car_red, 0, -1000)
        if self.canvas.coords(self.car_coin)[1] >= 500:
            self.canvas.move(self.car_coin, 0, -1000)
        if self.canvas.coords(self.car_Stola_1)[1] >= 500:
            self.canvas.move(self.car_Stola_1, 0, -2000)
        if self.canvas.coords(self.car_volvo_1)[1] >= 500:
            self.canvas.move(self.car_volvo_1, 0, -2000)

        if self.score >= 100:
            self.canvas.move(self.car_Stola, 0, 3)
            self.canvas.move(self.car_red, 0, 3)
            self.canvas.move(self.car_volvo, 0, 3)
            self.canvas.move(self.car_volvo_1, 0, 3)
            self.canvas.move(self.car_Stola_1, 0, 3)


        self.id = self.fenetre.after(5, self.move_car)

    def move_car_user(self,event):
        if event.keysym=="Left":
            if self.x <= 200:
                self.x = self.x
            else:
                self.x -= 160
        if event.keysym=="Right":
            if self.x >= 400:
                self.x = self.x
            else:
                self.x += 160

        self.canvas.coords(self.car_user, self.x, self.y)


fenetre = tk.Tk()
background_movement = BackgroundMovement(fenetre)

#création de fenetre
fenetre.geometry("600x500")
fenetre.title("K'ilalao")
fenetre.iconbitmap("../Image/chat.ico")
fenetre.resizable(False, False)
fenetre.mainloop()

