import tkinter as tk                       # Importation du module tkinter pour l'interface graphique
from tkinter import CENTER                  # Importation de la constante CENTER pour l'alignement
from PIL import Image, ImageTk              # Importation des modules PIL pour la manipulation d'images
import math                                # Importation du module math pour les calculs mathématiques
import time                                # Importation du module time pour la gestion du temps
import random                              # Importation du module random pour les valeurs aléatoires
import pygame                              # Importation du module pygame pour la lecture de musique et les effets sonores
import tkinter.messagebox                  # Importation du module tkinter.messagebox pour les boîtes de dialogue

class Tank:
    def __init__(self, root, canvas):         # Définition de la classe Tank avec son constructeur
        global image0, image, resized_image1  # Déclaration des variables globales

        self.explosion = None                 # Variable pour stocker l'explosion (initialement vide)
        self.root = root                       # Référence à la fenêtre principale
        self.canvas = canvas                   # Référence au canevas de dessin
        self.score = 0                         # Score initial à 0
        self.nb_score = self.canvas.create_text(749, 50, text=f"Score = {self.score}", font=("Lucida Console", 12))
                                              # Création d'un texte pour afficher le score

        self.tire = 0                          # Nombre de tires initial à 0
        self.nb_tire = self.canvas.create_text(700, 20, text=f"Nombre de tires = {self.tire}",
                                               font=("Lucida Console", 12))
                                              # Création d'un texte pour afficher le nombre de tires

        self.angle = 90                        # Angle initial à 90 degrés
        self.nb_angle = self.canvas.create_text(70, 20, text=f"{self.angle}°", font=("Lucida Console", 12))
                                              # Création d'un texte pour afficher l'angle

        self.x = random.randint(10, 790)       # Position aléatoire en x
        self.y = random.randint(200, 400)       # Position aléatoire en y

        self.stick_length = 50                 # Longueur du bâton

        self.tank_length = 100                 # Longueur du tank
        self.tank_width = 50                   # Largeur du tank
        self.tank_x = 430                      # Position x du tank
        self.tank_y = 410                      # Position y du tank

        self.xm = 0                            # Variable pour le mouvement du ballon

        self.is_shooting = False               # Variable pour indiquer si le tir est en cours

        self.caneau_y = self.tank_y - self.tank_width / 2
                                              # Position y du canon du tank

        self.stick = self.canvas.create_line(self.tank_x, self.caneau_y, self.tank_x, self.caneau_y - 50,
                                             width=7, fill="blue")
                                              # Création du bâton initial

        tank0 = tk.PhotoImage(file="img/tank.png")  # Chargement de l'image du tank
        resized_image1 = tank0.subsample(4, 4)  # Redimensionnement de l'image
        self.tank = self.canvas.create_image(self.tank_x, self.tank_y, image=resized_image1)
                                              # Création de l'image du tank sur le canevas

        tk.Button(self.root, text='Reset', command=self.reset).pack()
                                              # Création d'un bouton de réinitialisation

        self.text = canvas.create_text(440, 200, text="Kitio eto raha anomboka!", font=("Arial", 24), fill="black", anchor=CENTER)
                                              # Création d'un texte au centre du canevas

        self.canvas.tag_bind(self.text, "<Button-1>", self.on_text_click)
                                              # Association de l'événement de clic gauche sur le texte à la méthode on_text_click

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
                                              # Gestion de la fermeture de la fenêtre principale

    def on_text_click(self, event):
        self.canvas.delete(self.text)         # Suppression du texte lors du clic
        self.create_balloon()                  # Création d'un ballon après le clic

    def reset(self):
        try:
            self.score = 0                     # Réinitialisation du score à 0
            self.tire = 0                      # Réinitialisation du nombre de tires à 0
            self.canvas.delete(ballon)         # Suppression du ballon existant
            self.is_shooting = False           # Réinitialisation de la variable de tir
            self.canvas.delete(self.text)      # Suppression du texte
            self.text = self.canvas.create_text(440, 200, text="Kitio eto raha anomboka!", font=("Arial", 24), fill="black", anchor=CENTER)
                                              # Recréation du texte initial
            self.canvas.tag_bind(self.text, "<Button-1>", self.on_text_click)
                                              # Association de l'événement de clic gauche sur le texte
            self.canvas.unbind("<Button-1>")   # Désassociation de l'événement de clic gauche de la souris

        except:
            pass

    def shoot(self, event):
        global ballon, text, score, ball_x, ball_y, new_tank_x, ov, av, boom_resize
                                              # Déclaration des variables globales
        if self.is_shooting:                   # Vérification si le tir est en cours
            return

        pygame.init()                          # Initialisation de Pygame

        sound1 = pygame.mixer.Sound("song/canoon+4.mp3")
        sound1.play()                          # Lecture du son de tir

        self.tire += 1                         # Incrémentation du nombre de tires
        self.angle_rotate = 0

        print(f"Nombre de tire = {self.tire}")
        self.canvas.delete(self.nb_tire)
        self.nb_tire = self.canvas.create_text(700, 20, text=f"Nombre de tires = {self.tire}",
                                               font=("Lucida Console", 12))
                                              # Mise à jour de l'affichage du nombre de tires

        try:
            self.canvas.delete(ov)
            self.canvas.delete(text)
        except:
            pass

        try:
            ball_x = new_tank_x + self.stick_length * math.cos(math.radians(self.angle))
            ball_y = self.caneau_y - self.stick_length * math.sin(math.radians(self.angle))
        except:
            ball_x = self.tank_x + self.stick_length * math.cos(math.radians(self.angle))
            ball_y = self.caneau_y - self.stick_length * math.sin(math.radians(self.angle))
                                              # Calcul des coordonnées du ballon en fonction de l'angle et de la position du canon

        ball_radius = 3                          # Rayon du ballon
        velocity = 15                            # Vitesse initiale du ballon
        angle = self.angle                       # Angle du bâton
        angle_radians = math.radians(angle)      # Conversion de l'angle en radians

        time_interval = 0.083                    # Intervalle de temps entre les mises à jour de la position du ballon
        gravity = 9.8                            # Accélération due à la gravité en m/s^2
        time1 = 0                                # Temps initial
        self.is_shooting = True                  # Définition de la variable de tir à True

        boom = tk.PhotoImage(file="img/blast.png")   # Chargement de l'image de l'explosion
        boom_resize = boom.subsample(20, 20)     # Redimensionnement de l'image
        self.boom = self.canvas.create_image(ball_x, ball_y - 8, image=boom_resize)
                                              # Création de l'image de l'explosion à la position du ballon

        list_color_ball = ['red', 'black']       # Liste des couleurs disponibles pour le ballon
        i = 0

        while ball_y <= 450 and ball_x <= 800 and self.is_shooting == True:
                                              # Boucle tant que le ballon est dans les limites et le tir est en cours
            i += 1
            if i > 5:
                self.canvas.delete(self.boom)   # Suppression de l'explosion après un certain nombre d'itérations
            color_ball = random.choice(list_color_ball)
            ball_x += velocity * math.cos(angle_radians) * time1
            ball_y -= velocity * math.sin(angle_radians) * time1 - 0.5 * gravity * time1 ** 2
                                              # Calcul des nouvelles coordonnées du ballon
            self.ov = self.canvas.create_oval(ball_x - ball_radius, ball_y - ball_radius, ball_x + ball_radius,
                                              ball_y + ball_radius, fill=color_ball, outline="")
                                              # Création du ballon avec la couleur choisie
            time1 += time_interval
            self.canvas.update()
            time.sleep(time_interval)           # Pause pour ralentir le mouvement du ballon
            self.canvas.delete(self.ov)          # Suppression du ballon après la mise à jour

            if (self.x < ball_x and (self.x + 50) > ball_x) and (self.y + 15 < ball_y and (self.y + 45) > ball_y):
                print("boom")
                sound3 = pygame.mixer.Sound("song/Explosion+7.mp3")
                sound3.set_volume(3.0)
                sound3.play()                    # Lecture du son d'explosion

                self.score += 1                    # Incrémentation du score
                self.canvas.delete(ballon)         # Suppression du ballon touché
                self.ov = self.canvas.create_oval(ball_x - ball_radius, ball_y - ball_radius, ball_x + ball_radius,
                                                  ball_y + ball_radius, fill="red", outline="")
                                                  # Création d'un ballon rouge à la position touchée
                self.canvas.delete(self.ov)         # Suppression du ballon après un court instant
                self.explode_balloon(ball_x, ball_y)   # Animation d'explosion
                text = self.canvas.create_text(400, 200, text="Boom!", font=("Arial", 30))
                                                  # Affichage du texte "Boom!"
                self.canvas.delete(self.nb_score)
                self.nb_score = self.canvas.create_text(749, 50, text=f"Score = {self.score}",
                                                        font=("Lucida Console", 12))
                                                  # Mise à jour de l'affichage du score
                self.canvas.after_cancel(self.id1)
                self.create_balloon()                # Création d'un nouveau ballon
                self.is_shooting = False             # Réinitialisation de la variable de tir

                return

        self.is_shooting = False                    # Réinitialisation de la variable de tir

    def delete_oval(self):
        self.canvas.delete(self.ov)                 # Suppression du ballon (oval) du canevas

    def explode_balloon(self, x, y):
        self.canvas.delete(self.ov)                  # Suppression du ballon existant
        explosion_radius = 0                          # Rayon initial de l'explosion

        explosion_color_liste = ["red", "orange"]     # Liste des couleurs disponibles pour l'explosion

        explosion_particles = []                      # Liste pour stocker les particules de l'explosion

        for i in range(50):
            explosion_radius = explosion_radius + 1
            explosion_color = random.choice(explosion_color_liste)
            explosion_particle = self.canvas.create_oval(x - explosion_radius, y - explosion_radius,
                                                         x + explosion_radius, y + explosion_radius,
                                                         fill=explosion_color, outline="")
            explosion_particles.append(explosion_particle)
            self.canvas.update()

        self.canvas.after(50, self.delete_explosion_particles, explosion_particles)
                                                     # Planification de la suppression des particules après une seconde

    def delete_explosion_particles(self, explosion_particles):
        for particle in explosion_particles:
            self.canvas.delete(particle)               # Suppression de chaque particule de l'explosion

    def rotate_stick(self, event):
        global new_tank_x, new_x2, new_y2, ov       # Déclaration des variables globales
        delta = event.delta                           # Récupération du mouvement de la molette de la souris
        angle = delta / 120                            # Conversion du mouvement en angle

        self.angle -= angle                            # Mise à jour de l'angle du bâton

        self.canvas.delete(self.nb_angle)
        self.nb_angle = self.canvas.create_text(70, 20, text=f"{self.angle}°", font=("Lucida Console", 12))
                                                      # Mise à jour de l'affichage de l'angle

        if self.angle > 144:                           # Limite l'inclinaison maximale du bâton
            self.angle = 144
        elif self.angle < 36:                          # Limite l'inclinaison minimale du bâton
            self.angle = 36

        try:
            new_x2 = new_tank_x + self.stick_length * math.cos(math.radians(self.angle))
            new_y2 = self.caneau_y - self.stick_length * math.sin(math.radians(self.angle))
            self.canvas.coords(self.stick, new_tank_x, self.caneau_y, new_x2, new_y2)
                                                      # Mise à jour des coordonnées du bâton
        except:
            new_x2 = self.tank_x + self.stick_length * math.cos(math.radians(self.angle))
            new_y2 = self.caneau_y - self.stick_length * math.sin(math.radians(self.angle))
            self.canvas.coords(self.stick, self.tank_x, self.caneau_y, new_x2, new_y2)

    def move_tank(self, event):
        global new_tank_x, ov, text, text1, resized_image
        try:
            self.canvas.delete(text)
        except:
            pass
        try:
            self.canvas.delete(text1)
        except:
            pass

        new_tank_x = event.x                       # Coordonnée x de la position de la souris
        self.canvas.coords(self.tank, new_tank_x, self.tank_y)
                                                  # Mise à jour des coordonnées du tank

        new__x2 = new_tank_x + self.stick_length * math.cos(math.radians(self.angle))
        new__y2 = self.caneau_y - self.stick_length * math.sin(math.radians(self.angle))
        self.canvas.coords(self.stick, new_tank_x, self.caneau_y, new__x2, new__y2)
                                                  # Mise à jour des coordonnées du bâton

    def rpst(self):
        global image_repost, new_tank_x, text1, text, bal_repost
        try:
            self.canvas.after_cancel(self.aft_rpst)
        except:
            pass
        try:
            self.canvas.delete(text1)
        except:
            pass
        try:
            self.canvas.delete(text)
        except:
            pass
        try:
            self.canvas.delete(self.bal_repost_boom)
        except:
            pass
        try:
            x = new_tank_x
        except:
            new_tank_x = self.tank_x

        if self.x < new_tank_x:
            image02 = tk.PhotoImage(file="img/torpedo1.png")
            image_repost = image02.subsample(25, 25)    # Redimensionnement de l'image
            bal_repost = self.canvas.create_image(self.x, self.y, image=image_repost)
        else:
            image02 = tk.PhotoImage(file="img/torpedo.png")
            image_repost = image02.subsample(25, 25)    # Redimensionnement de l'image
            bal_repost = self.canvas.create_image(self.x, self.y, image=image_repost)

        self.xr = self.x
        self.yr = self.y + 20
        self.xtx = new_tank_x
        self.xrt = (self.xr - self.xtx)/30              # Calcul du déplacement horizontal du ballon de repostage

        self.repost()

    def repost(self):
        global text1, image_repost_boom, bal_repost
        self.xr -= self.xrt
        self.yr += 10
        self.canvas.moveto(bal_repost, self.xr, self.yr)

        if self.yr < 440:
            self.aft_rpst = self.canvas.after(70, self.repost)
            if (self.yr == 400 and self.xr > new_tank_x-75 and self.xr < new_tank_x+75) or (self.yr == 380 and self.xr > new_tank_x-45 and self.xr < new_tank_x+40):
                text1 = self.canvas.create_text(400, 200, text="Ohhh!!", font=("Arial", 30))
                image03 = tk.PhotoImage(file="img/blasting.png")
                image_repost_boom = image03.subsample(15, 15)  # Redimensionnement de l'image
                self.bal_repost_boom = self.canvas.create_image(self.xr, self.yr, image=image_repost_boom)
                self.canvas.after_cancel(self.aft_rpst)
                self.canvas.delete(bal_repost)

        else:
            image03 = tk.PhotoImage(file="img/blasting.png")
            image_repost_boom = image03.subsample(15, 15)  # Redimensionnement de l'image
            self.bal_repost_boom = self.canvas.create_image(self.xr, self.yr, image=image_repost_boom)
            self.canvas.after_cancel(self.aft_rpst)
            self.canvas.delete(bal_repost)

    def mvm(self):
        global ballon, ball_x, ball_y, image_repost
        self.xm = self.xm+1
        if self.xm == 2:
            self.canvas.bind("<MouseWheel>", self.rotate_stick)     # Association de la molette de la souris à la rotation du bâton
            self.canvas.bind("<Motion>", self.move_tank)             # Association du mouvement de la souris au déplacement du tank
            self.canvas.bind("<Button-1>", self.shoot)               # Association du clic gauche de la souris au tir

        self.x += 5
        if self.x in [40, 240, 440, 640]:
            self.rpst()                                      # Repostage du ballon à des positions spécifiques

        self.canvas.moveto(ballon, self.x, self.y)           # Déplacement du ballon sur le canevas

        if self.x > 800:
            self.canvas.delete(ballon)                      # Suppression du ballon lorsqu'il sort des limites
            self.create_balloon()                            # Création d'un nouveau ballon

        self.canvas.after(50, self.mvm)

    def on_closing(self):
        if tkinter.messagebox.askokcancel("Quitter", "Voulez-vous vraiment quitter?"):
            self.root.destroy()                                # Fermeture de la fenêtre principale

    def create_balloon(self):
        global ballon, image, resized_image, boom_resize
        self.x = random.randint(10, 790)                     # Position aléatoire en x
        self.y = random.randint(200, 400)                     # Position aléatoire en y
        image0 = tk.PhotoImage(file="img/baloon2.png")           # Chargement de l'image du ballon
        image = image0.subsample(9, 9)                        # Redimensionnement de l'image
        self.ballon = self.canvas.create_image(self.x, self.y, image=image)   # Création de l'image du ballon sur le canevas

    def start(self):
        self.canvas.after(0, self.mvm)                      # Lancement de la boucle principale du mouvement du ballon


if __name__ == "__main__":
    root = tk.Tk()                                       # Création de la fenêtre principale
    root.geometry("800x600")                             # Définition de la taille de la fenêtre
    root.title("Jeu de Tir")                             # Définition du titre de la fenêtre

    canvas = tk.Canvas(root, bg="white", width=800, height=500)
                                                         # Création d'un canevas pour le dessin
    canvas.pack()

    game = Tank(root, canvas)                             # Création de l'objet Tank

    root.mainloop()                                       # Boucle principale de la fenêtre
