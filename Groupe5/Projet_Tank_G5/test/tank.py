import tkinter as tk                       # Importation du module tkinter pour l'interface graphique
from tkinter import CENTER, ttk  # Importation de la constante CENTER pour l'alignement
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

        self.vie2 = 449
        self.vie = self.canvas.create_rectangle(349, 9, 450, 20, fill="white")
        self.vie1 = self.canvas.create_rectangle(351, 11, self.vie2, 19 , fill="green", outline= "")

        self.score = 0                         # Score initial à 0
        self.tire = 0                          # Nombre de tires initial à 0

        self.cadre = self.canvas.create_rectangle(600, 10, 790, 70, fill="white")

        self.nb_score = self.canvas.create_text(740, 50, text=f"Score = {self.score}", font=("Verdana", 12))
                                              # Création d'un texte pour afficher le score
        self.nb_tire = self.canvas.create_text(695, 25, text=f"Nombre de tires = {self.tire}",
                                               font=("Verdana", 12))
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

        tank0 = tk.PhotoImage(file="tank.png")  # Chargement de l'image du tank
        resized_image1 = tank0.subsample(4, 4)  # Redimensionnement de l'image
        self.tank = self.canvas.create_image(self.tank_x, self.tank_y, image=resized_image1)
                                              # Création de l'image du tank sur le canevas

        ttk.Button(self.root, text='Rejouer', command=self.reset).pack()
                                              # Création d'un bouton de réinitialisation

        self.text = canvas.create_text(440, 200, text="Cliquer ici pour commencer!", font=("Arial", 24), fill="black", anchor=CENTER)
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
            self.canvas.delete(self.nb_score)
            self.canvas.delete(self.nb_tire)
            self.score = 0                     # Réinitialisation du score à 0
            self.tire = 0                      # Réinitialisation du nombre de tires à 0

            self.nb_score = self.canvas.create_text(740, 50, text=f"Score = {self.score}", font=("Verdana", 12))     # Création d'un texte pour afficher le score
            self.nb_tire = self.canvas.create_text(695, 25, text=f"Nombre de tires = {self.tire}", font=("Verdana", 12))     # Création d'un texte pour afficher le nombre de tires

            self.canvas.delete(ballon)         # Suppression du ballon existant
            self.is_shooting = False           # Réinitialisation de la variable de tir
            self.canvas.delete(self.text)      # Suppression du texte
            self.text = self.canvas.create_text(440, 200, text="Cliquer ici pour commencer!", font=("Arial", 24), fill="black", anchor=CENTER)
                                              # Recréation du texte initial
            self.canvas.tag_bind(self.text, "<Button-1>", self.on_text_click)
                                              # Association de l'événement de clic gauche sur le texte
            self.canvas.unbind("<Button-1>")   # Désassociation de l'événement de clic gauche de la souris

            self.vie2 = 449
            self.canvas.delete(self.vie1)
            self.vie1 = self.canvas.create_rectangle(351, 11, self.vie2, 19, fill="green", outline="")
            self.canvas.delete(self.bal_repost_boom)

            self.canvas.after_cancel(self.aft_rpst)  # Annule le prochain déplacement du repost
            self.canvas.delete(bal_repost)  # Supprime l'image du repost
            self.canvas.after_cancel(self.id1)

        except:
            pass

    def shoot(self, event):
        # Déclaration des variables en tant que variables globales
        global ballon, text, score, ball_x, ball_y, new_tank_x, ov, av, boom_resize

        if self.is_shooting:  # Vérifier si le tank est déjà en train de tirer
            return

        pygame.init()
        sound1 = pygame.mixer.Sound("canoon+4.mp3")  # Charger le son du canon
        sound1.play()  # Jouer le son du canon

        self.tire += 1  # Incrémenter le compteur de tirs du tank
        self.angle_rotate = 0

        print(f"Nombre de tire = {self.tire}")  # Afficher le nombre de tirs effectués
        self.canvas.delete(self.nb_tire)  # Supprimer le texte affichant le nombre de tirs précédent
        self.nb_tire = self.canvas.create_text(695, 25, text=f"Nombre de tires = {self.tire}",
                                               font=("Verdana", 12))  # Afficher le nombre de tirs mis à jour

        try:
            self.canvas.delete(ov)   #Tente de supprimer une ancienne balle sur le canevas.
            self.canvas.delete(text)
        except:
            pass

        try:
            ball_x = new_tank_x + self.stick_length * math.cos(math.radians(self.angle))   #Calcule la position initiale de la balle en fonction de la nouvelle position du tank et de la longueur du canon.
            ball_y = self.caneau_y - self.stick_length * math.sin(math.radians(self.angle))
        except:
            ball_x = self.tank_x + self.stick_length * math.cos(math.radians(self.angle))   ##Calcule la position initiale de la balle en fonction de la position du tank et de la longueur du canon.
            ball_y = self.caneau_y - self.stick_length * math.sin(math.radians(self.angle))

        ball_radius = 3    # Définit le rayon de la balle.
        velocity = 15  # Vitesse initiale de la balle
        angle = self.angle  # Angle du bâton
        angle_radians = math.radians(angle)  # Convertir l'angle en radians

        time_interval = 0.083  # Intervalle de temps entre les mises à jour de la position du boulet
        gravity = 9.8  # Accélération due à la gravité en m/s^2
        time1 = 0   # Initialise le temps à 0.
        self.is_shooting = True   #Définit la variable de contrôle de tir à True.

        boom = tk.PhotoImage(file="blast.png")   # Charge l'image de l'explosion.
        boom_resize = boom.subsample(20, 20)  # Modifier la taille de l'image
        self.boom = self.canvas.create_image(ball_x, ball_y - 8, image=boom_resize)  # Créer l'image de l'explosion

        list_color_ball = ['red', 'black']   # Définit une liste de couleurs pour les balles.
        i = 0    # Initialise un compteur.
        while ball_y <= 450 and ball_x <= 800 and self.is_shooting == True:    # Boucle tant que la balle est dans les limites du canevas et que le tir est en cours.
            i += 1
            if i > 5:
                self.canvas.delete(self.boom)  # Supprimer l'explosion après 5 itérations

            color_ball = random.choice(list_color_ball)  # Sélectionner une couleur aléatoire pour la balle

            ball_x += velocity * math.cos(angle_radians) * time1  # Mettre à jour la position x de la balle
            ball_y -= velocity * math.sin(
                angle_radians) * time1 - 0.5 * gravity * time1 ** 2  # Mettre à jour la position y de la balle

            self.ov = self.canvas.create_oval(ball_x - ball_radius, ball_y - ball_radius, ball_x + ball_radius,
                                              ball_y + ball_radius, fill=color_ball,
                                              outline="")  # Créer une balle sur le canevas

            time1 += time_interval  # Incrémenter le temps
            self.canvas.update()  # Mettre à jour le canevas
            time.sleep(time_interval)  # Pause pour ralentir le mouvement de la balle

            self.canvas.delete(self.ov)  # Supprimer la balle du canevas

            if (self.x < ball_x and (self.x + 50) > ball_x) and (self.y + 15 < ball_y and (self.y + 45) > ball_y):
                print("boom")  # Afficher "boom" dans la console

                sound3 = pygame.mixer.Sound("Explosion+7.mp3")  # Charger le son de l'explosion
                sound3.set_volume(3.0)  # Définir le volume de l'explosion
                sound3.play()  # Jouer le son de l'explosion

                self.score += 1  # Incrémenter le score du joueur

                self.canvas.delete(ballon)  # Supprimer le ballon cible
                self.ov = self.canvas.create_oval(ball_x - ball_radius, ball_y - ball_radius, ball_x + ball_radius,
                                                  ball_y + ball_radius, fill="red",
                                                  outline="")  # Créer une balle rouge à l'emplacement de l'explosion
                self.canvas.delete(self.ov)  # Supprimer la balle rouge

                self.explode_balloon(ball_x, ball_y)  # Déclencher l'animation d'explosion

                text = self.canvas.create_text(400, 200, text="Boom!",
                                               font=("Arial", 30))  # Afficher "Boom!" sur le canevas

                self.canvas.delete(self.nb_score)  # Supprimer le texte affichant le score précédent
                self.nb_score = self.canvas.create_text(740, 50, text=f"Score = {self.score}",
                                                        font=("Verdana", 12))  # Afficher le score mis à jour

                self.canvas.after_cancel(self.id1)  # Annuler la prochaine mise à jour du mouvement du ballon cible
                self.create_balloon()  # Créer un nouveau ballon cible

                self.is_shooting = False  # Réinitialiser la variable de contrôle

                return

        self.is_shooting = False  # Réinitialiser la variable de contrôle de tir

    def delete_oval(self):   # fonction pour la suppression de l'ovale
        self.canvas.delete(self.ov)  # Supprimer l'ovale (balle) du canevas

    def explode_balloon(self, x, y):    # animation d'explosion à l'emplacement spécifié du ballon cible
        self.canvas.delete(self.ov)  # Supprimer le ballon existant du canevas
        explosion_radius = 0
        explosion_color_liste = ["red", "orange"]  # Liste de couleurs pour les particules d'explosion

        explosion_particles = []  # Créer une liste pour stocker les identifiants des particules d'explosion

        # Boucle pour créer les particules d'explosion
        for i in range(50):
            explosion_radius = explosion_radius + 1
            explosion_color = random.choice(explosion_color_liste)  # Sélectionner une couleur aléatoire
            explosion_particle = self.canvas.create_oval(x - explosion_radius, y - explosion_radius,
                                                         x + explosion_radius, y + explosion_radius,
                                                         fill=explosion_color, outline="")
            explosion_particles.append(explosion_particle)  # Ajouter l'identifiant de la particule à la liste
            self.canvas.update()  # Mettre à jour le canevas pour afficher les nouvelles particules

        self.canvas.after(50, self.delete_explosion_particles,
                          explosion_particles)  # Planifier la suppression des particules après une seconde

    def delete_explosion_particles(self, explosion_particles):   # supprime toutes les particules d'explosion du canevas.
        for particle in explosion_particles:  # Parcourir toutes les particules d'explosion
            self.canvas.delete(particle)  # Supprimer chaque particule du canevas

    def rotate_stick(self, event):   # lorsqu'il y a un événement de rotation de la molette de la souris.
        global new_tank_x, new_x2, new_y2, ov
        delta = event.delta  # Obtient le déplacement de la molette de la souris
        angle = delta / 120  # Convertit le déplacement en angle

        self.angle -= angle  # Met à jour l'angle du bâton

        self.canvas.delete(self.nb_angle)  # Supprime l'ancien texte affichant l'angle sur le canevas
        self.nb_angle = self.canvas.create_text(70, 20, text=f"{self.angle}°", font=(
        "Lucida Console", 12))  # Crée un nouveau texte affichant l'angle mis à jour sur le canevas

        if self.angle > 144:  # Limite l'inclinaison du canon
            self.angle = 144
        elif self.angle < 36:
            self.angle = 36

        try:  # Mettre à jour les coordonnées du bâton
            new_x2 = new_tank_x + self.stick_length * math.cos(
                math.radians(self.angle))  # Calcule la nouvelle coordonnée x de l'extrémité du bâton
            new_y2 = self.caneau_y - self.stick_length * math.sin(
                math.radians(self.angle))  # Calcule la nouvelle coordonnée y de l'extrémité du bâton
            self.canvas.coords(self.stick, new_tank_x, self.caneau_y, new_x2,
                               new_y2)  # Met à jour les coordonnées du bâton sur le canevas
        except:
            new_x2 = self.tank_x + self.stick_length * math.cos(
                math.radians(self.angle))  # Calcule la nouvelle coordonnée x de l'extrémité du bâton en cas d'erreur
            new_y2 = self.caneau_y - self.stick_length * math.sin(
                math.radians(self.angle))  # Calcule la nouvelle coordonnée y de l'extrémité du bâton en cas d'erreur
            self.canvas.coords(self.stick, self.tank_x, self.caneau_y, new_x2,
                               new_y2)  # Met à jour les coordonnées du bâton sur le canevas en cas d'erreur

    def move_tank(self, event):  #  lorsqu'il y a un événement de déplacement de la souris. Elle permet de déplacer le tank horizontalement sur le canevas.
        global new_tank_x, ov, text, text1, resized_image

        try:
            self.canvas.delete(text)  # Supprime le texte précédent affiché sur le canevas
        except:
            pass

        try:
            self.canvas.delete(text1)  # Supprime le texte précédent affiché sur le canevas
        except:
            pass

        new_tank_x = event.x  # Coordonnée x de la position de la souris

        self.canvas.coords(self.tank, new_tank_x, self.tank_y)  # Met à jour les coordonnées du tank sur le canevas

        new__x2 = new_tank_x + self.stick_length * math.cos(
            math.radians(self.angle))  # Calcule la nouvelle coordonnée x de l'extrémité du bâton
        new__y2 = self.caneau_y - self.stick_length * math.sin(
            math.radians(self.angle))  # Calcule la nouvelle coordonnée y de l'extrémité du bâton

        self.canvas.coords(self.stick, new_tank_x, self.caneau_y, new__x2,
                           new__y2)  # Met à jour les coordonnées du bâton sur le canevas

    def rpst(self):   # effectuer une action de "repost" dans le jeu.
        global image_repost, new_tank_x, text1, text, bal_repost

        try:
            self.canvas.after_cancel(self.aft_rpst)  # Annule l'after précédemment programmé
        except:
            pass

        try:
            self.canvas.delete(text1)  # Supprime le texte précédent affiché sur le canevas
        except:
            pass

        try:
            self.canvas.delete(text)  # Supprime le texte précédent affiché sur le canevas
        except:
            pass

        try:
            self.canvas.delete(self.bal_repost_boom)  # Supprime l'explosion précédente sur le canevas
        except:
            pass

        try:
            x = new_tank_x  # Récupère la position x du tank
        except:
            new_tank_x = self.tank_x  # Utilise la position x par défaut du tank

        if self.x < new_tank_x:
            image02 = tk.PhotoImage(file="torpedo1.png")  # Charge l'image du repost
            image_repost = image02.subsample(25, 25)  # Redimensionne l'image
            bal_repost = self.canvas.create_image(self.x, self.y,
                                                  image=image_repost)  # Crée l'image du repost sur le canevas
        else:
            image02 = tk.PhotoImage(file="torpedo.png")  # Charge l'image du repost
            image_repost = image02.subsample(25, 25)  # Redimensionne l'image
            bal_repost = self.canvas.create_image(self.x, self.y,
                                                  image=image_repost)  # Crée l'image du repost sur le canevas

        self.xr = self.x  # Position x de départ du repost
        self.yr = self.y + 20  # Position y de départ du repost
        self.xtx = new_tank_x  # Position x cible du repost
        self.xrt = (self.xr - self.xtx) / 30  # Calcul de la vitesse de déplacement

        self.repost()  # Appelle la méthode "repost" pour effectuer l'action

    def repost(self):
        global text1, image_repost_boom, bal_repost

        self.xr -= self.xrt  # Met à jour la position x du repost
        self.yr += 10  # Met à jour la position y du repost

        self.canvas.moveto(bal_repost, self.xr, self.yr)  # Déplace l'image du repost à la nouvelle position

        if self.yr < 440:  # Vérifie si le repost est encore dans les limites du canevas
            self.aft_rpst = self.canvas.after(70, self.repost)  # Planifie le prochain déplacement du repost

            if (self.yr == 400 and self.xr > new_tank_x - 75 and self.xr < new_tank_x + 75) or \
                    (self.yr == 380 and self.xr > new_tank_x - 45 and self.xr < new_tank_x + 40):


# ======================================================================================================
# vie du tank quand la balle de repost le touche
                self.vie2 -= 40
                self.canvas.delete(self.vie1)
                if self.vie2 < 400 and self.vie2>351:

                    sound4 = pygame.mixer.Sound("song4.mp3")  # Charger le son de l'explosion
                    sound4.set_volume(0.5)  # Définir le volume de l'explosion
                    sound4.play()  # Jouer le son de l'explosion
                    self.vie1 = self.canvas.create_rectangle(351, 11, self.vie2, 19, fill="red", outline="")
                    image03 = tk.PhotoImage(file="blasting.png")  # Charge l'image de l'explosion du repost
                    image_repost_boom = image03.subsample(15, 15)  # Redimensionne l'image de l'explosion du repost
                    self.bal_repost_boom = self.canvas.create_image(self.xr, self.yr,
                                                                    image=image_repost_boom)  # Crée l'image de l'explosion du repost
                elif self.vie2 < 351:
                    sound4 = pygame.mixer.Sound("gameover.mp3")  # Charger le son de l'explosion
                    sound4.set_volume(1.0)  # Définir le volume de l'explosion
                    sound4.play()  # Jouer le son de l'explosion

                    self.text = self.canvas.create_text(400, 200, text="Game over!", font=("Arial", 24),
                                                        fill="black", anchor=CENTER)

                    self.canvas.delete(ballon)  # Suppression du ballon existant
                    self.is_shooting = False  # Réinitialisation de la variable de tir

                    self.canvas.unbind("<Button-1>")  # Désassociation de l'événement de clic gauche de la souris

                    self.canvas.after_cancel(self.aft_rpst)  # Annule le prochain déplacement du repost
                    self.canvas.delete(bal_repost)  # Supprime l'image du repost
                    self.canvas.after_cancel(self.id1)
                else:

                    sound4 = pygame.mixer.Sound("song4.mp3")  # Charger le son de l'explosion
                    sound4.set_volume(0.5)  # Définir le volume de l'explosion
                    sound4.play()  # Jouer le son de l'explosion
                    self.vie1 = self.canvas.create_rectangle(351, 11, self.vie2, 19, fill="green", outline="")
                    image03 = tk.PhotoImage(file="blasting.png")  # Charge l'image de l'explosion du repost
                    image_repost_boom = image03.subsample(15, 15)  # Redimensionne l'image de l'explosion du repost
                    self.bal_repost_boom = self.canvas.create_image(self.xr, self.yr,
                                                                    image=image_repost_boom)  # Crée l'image de l'explosion du repost

                self.canvas.after_cancel(self.aft_rpst)  # Annule le prochain déplacement du repost
                self.canvas.delete(bal_repost)  # Supprime l'image du repost

        else:
            image03 = tk.PhotoImage(file="blasting.png")  # Charge l'image de l'explosion du repost
            image_repost_boom = image03.subsample(15, 15)  # Redimensionne l'image de l'explosion du repost
            self.bal_repost_boom = self.canvas.create_image(self.xr, self.yr,
                                                            image=image_repost_boom)  # Crée l'image de l'explosion du repost
            self.canvas.after_cancel(self.aft_rpst)  # Annule le prochain déplacement du repost
            self.canvas.delete(bal_repost)  # Supprime l'image du repost

    def mvm(self):
        global ballon, ball_x, ball_y, image_repost

        self.xm = self.xm + 1  # Incrémente le compteur de mouvement du ballon

        if self.xm == 2:
            # Lie les événements de la souris aux fonctions correspondantes
            self.canvas.bind("<MouseWheel>",
                             self.rotate_stick)  # Lier la molette de la souris à la fonction rotate_stick
            self.canvas.bind("<Motion>", self.move_tank)  # Lier le mouvement de la souris à la fonction move_tank
            self.canvas.bind("<Button-1>", self.shoot)  # Lier le clic gauche de la souris à la fonction shoot

        self.x += 5  # Déplace le ballon horizontalement

        if self.x in [240, 440, 640]:
            self.rpst()  # Déclenche le repost si le ballon atteint certaines positions

        self.canvas.moveto(ballon, self.x, self.y)  # Déplace l'image du ballon à la nouvelle position

        try:
            if (self.x < ball_x and (self.x + 50) > ball_x) and (self.y + 15 < ball_y and (self.y + 45) > ball_y):
                return  # Si le ballon touche le ballon cible, la méthode se termine
        except:
            pass

        if self.x >= 800:
            self.canvas.delete(ballon)  # Supprime le ballon
            self.create_balloon()  # Crée un nouveau ballon
            return  # Termine la méthode
        else:
            self.id1 = self.canvas.after(70, self.mvm)  # Planifie le prochain mouvement du ballon

    def create_balloon(self): # creation de la balle de tank
        global ballon, av, resized_image
        try:
            self.canvas.delete(av)
        except:
            pass
        try:
            self.canvas.after_cancel(self.id1)
        except:
            pass
        self.xm = 0
        self.x = 10  # Position aléatoire en x
        self.y = 100  # Position aléatoire en y
        colors = ["red", "blue", "green", "yellow", "orange", "purple"]  # Couleurs disponibles
        sizes = [10]  # Tailles disponibles

        self.color = random.choice(colors)  # Couleur aléatoire
        self.size = random.choice(sizes)  # Taille aléatoire

        # Charger l'image
        image01 = tk.PhotoImage(file="rocket.png")
        resized_image = image01.subsample(self.size, self.size)  # Modifier la taille de l'image
        ballon = self.canvas.create_image(self.x, self.y, image=resized_image)
        self.mvm()     # appel la methode mvm pour la mouvement de balle

    def start(self):
        self.root.mainloop()  # Démarre la boucle principale de l'application tkinter

    def quit(self):
        global app
        pygame.mixer.music.stop()  # Arrête la musique en cours
        app.quit()  # Quitte l'application

    def on_closing(self):
        if tkinter.messagebox.askokcancel("Quitter", "Êtes-vous sûr de vouloir quitter ?"):
            quit()  # Demande à l'utilisateur de confirmer s'il souhaite quitter, puis quitte l'application


if __name__ == "__main__":
    # Lecture de la musique
    pygame.init()  # Initialise la bibliothèque Pygame

    # Chargement du fichier audio
    pygame.mixer.music.load("song2.mp3")  # Charge le fichier audio "song2.mp3"
    pygame.mixer.music.set_volume(0.1)  # Réglage du volume de la musique
    pygame.mixer.music.play(-1)  # Joue la musique en boucle

    root = tk.Tk()  # Crée une instance de la classe Tk pour la fenêtre principale de l'application

    # Crée un canevas avec une largeur et une hauteur spécifiées
    canvas_width = 800
    canvas_height = 600
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
    canvas.pack()

    # Charge l'image de fond
    image_fond = Image.open("fond.jpg")
    new_image_fond = image_fond.resize((canvas_width, canvas_height), Image.LANCZOS)
    background_image = ImageTk.PhotoImage(new_image_fond)

    # Crée une image de fond sur le canevas
    canvas.create_image(0, 0, anchor=tk.NW, image=background_image)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        app = Tank(root, canvas)  # Crée une instance de la classe Tank avec la fenêtre et le canevas
        pygame.time.Clock().tick(30)  # Limite la boucle principale à 30 images par seconde
        app.start()  # Démarre l'application tkinter en appelant la méthode start de l'instance de Tank
