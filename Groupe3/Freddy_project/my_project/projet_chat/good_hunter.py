import tkinter as tk
from PIL import ImageTk, Image
import random
import subprocess
import pygame
import customtkinter
from tkinter import messagebox

class fish(object):
    def __init__(self,can,x,y,x1,y1):
        #initialisation de tous les variables nécesssaires
        self.window=window
        self.canvas = can
        self.x = x
        self.y = y
        self.x1 = x1
        self.y1 = y1
        self.rect_mouv_y = 10
        self.rect_mouv_x = 10
        self.line = 50
        self.score = 0
        self.score1 = 0
        self.dt = 1000
        self.deltay = 10
        self.deltax=20
        self.canvas_width =  600
        self.canvas_height = 500
        self.create =0

        #dictionnaire pour la création de la forme du bouton
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

        # initialisation de music
        pygame.init()
        self.channel1 = pygame.mixer.Channel(1)
        self.channel2 = pygame.mixer.Channel(2)

        ##insertion d'image
        self.image_rat = Image.open("../Image/Rat1.PNG")#on prend l'image dans son emplacement
        self.image_rat = self.image_rat.resize((50, 50))#on change sa forme si nécessaire
        self.image_rat = ImageTk.PhotoImage(self.image_rat)#on déclare l'image dans un variable


        self.image_chat1 = Image.open("../Image/chat2.png")
        self.image_chat1 = self.image_chat1.resize((100, 100))
        self.image_chat1 = ImageTk.PhotoImage(self.image_chat1)
        self.rectangle = self.canvas.create_image(self.x, self.y, image=self.image_chat1)#création de l'image et definit sa position

        self.image_chat = Image.open("../Image/chat1.PNG")
        self.image_chat = self.image_chat.resize((100, 100))
        self.image_chat = ImageTk.PhotoImage(self.image_chat)
        self.rectangle1 = self.canvas.create_image(self.x, self.y, image=self.image_chat)


        #affichage de score et sa position
        self.label = tk.Label(can, text="Kuki: {}".format(self.score))
        self.label.place(rely=0.05, relx=0.05)

        self.label = tk.Label(can, text="Keke: {}".format(self.score1))
        self.label.place(rely=0.05, relx=0.25)

        #commande pour la déplacement de chat1
        can.bind("<KeyPress>", self.chat_0)
        can.bind("<z>", self.chat_0)
        can.bind("<s>", self.chat_0)
        can.bind("<q>", self.chat_0)
        can.bind("<d>", self.chat_0)

        #commande pour le déplacement de la deuxième chat
        can.bind("<KeyPress>", self.chat_1)
        can.bind("<Up>", self.chat_1)
        can.bind("<Down>", self.chat_1)
        can.bind("<Left>", self.chat_1)
        can.bind("<Right>", self.chat_1)

        #commande pour le petit souris
        can.bind("<KeyPress>", self.rat_0)
        can.bind("<space>",self.rat_0)
        can.focus_set()

        #bouton pour quitter et sa position
        self.boutton_quitter = customtkinter.CTkButton(can, text="BACK", **self.Button_Style, command=self.back)
        self.boutton_quitter.place(relx=0.75, rely=0.03)

        self.rat_0()

    def music_play1(self):
        self.music = pygame.mixer.Sound("../Music/coin.mp3")
        self.music.set_volume(30.0)
        self.channel1.play(self.music)

    def music_play2(self):
        self.music = pygame.mixer.Sound("../Music/clique.mp3")
        self.music.set_volume(30.0)
        self.channel2.play(self.music)

    def back(self): #fonction retour à la fenetre tout les applications
        self.music_play2()
        subprocess.Popen(["python", "./all_application.py"])
        self.window.destroy()

    def rat_0(self): #fonction pour le faire apparaître
        self.y_rat = random.randint(100,400)
        self.x_rat = random.randint(100, 400)
        self.rat = self.canvas.create_image(self.x_rat +50, self.y_rat, anchor=tk.CENTER, image=self.image_rat)
        self.rat_mouve() #appel de fonction de mouvement de souris

    def rat_mouve(self): #fonction pour la mouvement de souris
        self.canvas.moveto(self.rat, self.x_rat, self.y_rat) #on donne le mouvement du souris
        self.y_rat -= self.deltay  #on diminue la valeur de z suivant
        self.x_rat -= self.deltax #on diminue la valeur de x
        if not 130 < self.y_rat < 500: #condition pour la mouvemnent de souris, pour qu'il revient
            self.deltay = -self.deltay
            self.x_rat = -self.deltax
        if not 50 < self.x_rat < 550:
            self.deltax = -self.deltax


        self.canvas.after(self.dt, self.rat_mouve) #appel au fonction pour qu'il continue le mouvement


    def chat_0(self, event): #fonction de commande pour le premier chat
        if event.keysym == "q": #déplacement à gauche
            self.x -= self.rect_mouv_x
            if self.x < 100:
                self.x = 100
        elif event.keysym == "d": #déplacement à droite
            self.x += self.rect_mouv_x
            if self.x > self.canvas_width - 50:
                self.x = self.canvas_width - 50

        if event.keysym == "z": #déplacement vers le haut
            self.y = self.y - self.rect_mouv_y
            if self.y < 130:
                self.y = 130
        elif event.keysym == "s": #déplacement vers le bas
            self.y = self.y + self.rect_mouv_y
            if self.y > self.canvas_height - 50:
                self.y = self.canvas_height - 50
        if (self.x) >= (self.x_rat) and (self.x-100) <= (self.x_rat): #condition pour avoir de score et pour quitter le jeu si le score max est atteint
            if (self.y) >= (self.y_rat) and (self.y-100) <= (self.y_rat):
                self.canvas.delete(self.rat)
                self.score += 1
                self.label = tk.Label(self.canvas, text="Kuki: {}".format(self.score))
                self.label.place(rely=0.05, relx=0.05)
                self.music_play1()
                self.rat_0()
                if self.score>=99:
                    subprocess.Popen(["python", "./congratulation_hunter.py"])
                    window.destroy()


        canvas.coords(self.rectangle, self.x-25, self.y-25) #on donne une nouvelle cordonné au chat

    def chat_1(self, event):  # mouvement de la tank
        if event.keysym == "Left":
            self.x1 = self.x1 - self.rect_mouv_x
            if self.x1 < 100:
                self.x1 = 100
        elif event.keysym == "Right":
            self.x1 = self.x1 + self.rect_mouv_x
            if self.x1 > self.canvas_width - 50:
                self.x1 = self.canvas_width - 50

        canvas.coords(self.rectangle1, self.x1-25, self.y1-25)

        if event.keysym == "Up":
            self.y1 = self.y1 - self.rect_mouv_y
            if self.y1 < 130:
                self.y1 = 130
        elif event.keysym == "Down":
            self.y1 = self.y1 + self.rect_mouv_y
            if self.y1 > self.canvas_height - 50:
                self.y1 = self.canvas_height - 50
        if (self.x1) >= (self.x_rat) and (self.x1-100) <= (self.x_rat):
            if (self.y1) >= (self.y_rat) and (self.y1-100) < (self.y_rat):
                self.canvas.delete(self.rat)
                self.score1 += 1
                self.label = tk.Label(self.canvas, text="Keke: {}".format(self.score1))
                self.label.place(rely=0.05, relx=0.25)
                self.music_play1()
                self.rat_0()
                if self.score1>=99:
                    subprocess.Popen(["python", "./congratulation_hunter.py"])
                    window.destroy()

        canvas.coords(self.rectangle1, self.x1-25, self.y1-25)

if __name__ == '__main__':
    window= tk.Tk() #création de fenetre
    window.title("K'ilalao") #initialisation de titre
    window.geometry("600x500") #intialisation de sa taille
    window.iconbitmap("../Image/chat.ico") #insertion d'icon
    window.resizable(False, False)

    canvas_width = 600
    canvas_height = 500
    x = 25
    y = canvas_height - 50
    x1 = 25
    y1 = canvas_height - 50

    #création de canvas
    canvas = tk.Canvas(window, width=canvas_width, height=canvas_height)
    canvas.pack()

    #insertion de photo
    image = tk.PhotoImage(file="../Image/laberinte.PNG")
    image = image.zoom(2) #zoom por l'arrière plan
    canvas.create_image(0, 0, anchor=tk.NW, image=image)

    objet = fish(canvas, x, y,x1,y1)

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