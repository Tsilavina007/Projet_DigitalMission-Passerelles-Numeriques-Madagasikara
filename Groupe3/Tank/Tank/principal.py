from tkinter import *
from math import pi, sin, cos
from tkinter import PhotoImage
from PIL import ImageTk, Image
import random
import customtkinter as ctk
import pygame


class Canon(object):
    def __init__(self, boss, x, y):
        """Initialisation des variables"""
        self.boss = boss  # référence du canevas
        self.x1, self.y1 = x, y  # axe de rotation du canon
        # dessiner la buse du canon, à l'horizontale pour commencer :
        self.angle = 0  # angle de la buse
        self.lbu = 50  # longueur de la buse
        self.x2 = x + self.lbu
        self.y1 = y-15 # Ajuster la coordonnée y1 pour déplacer la buse plus haut,Initialisation
        self.y2 = y-15# Ajuster la coordonnée y2 pour déplacer la buse plus haut,Initialisation
    
        # Lier l'événement de la molette de la souris à la fonction de gestion d'événements
        boss.bind("<MouseWheel>", self.deplacer_buse)#Evenement de la roulette
        boss.bind("<Button-1>", self.feu)#click
        boss.bind("<Motion>", self.deplacer_ovale)#Déplacer le tank
        
        
        # Création des images
        # Images Ciels Fond
        image6 = Image.open("./images/war.png")

        # Redimensionner l'image à la taille souhaitée
        new_size6 = (1800, 700)  # Remplacez width et height par les dimensions désirées
        resized_image6 = image6.resize(new_size6)

        # Créer un objet PhotoImage à partir de l'image redimensionnée
        self.image6_tk = ImageTk.PhotoImage(resized_image6)
        
    
        
        # Créer un nouvel élément d'image dans le canevas
        self.image6_item = boss.create_image(0, 340,image=self.image6_tk)
        
    
        
        #Création du buse ou le cannon
        self.buse = boss.create_line(self.x1-7, self.y1+5, self.x2, self.y2+5, width=5)
        
        #Création du tank
        image = Image.open("./images/tank.png")

        new_size = (140, 120)  # Remplacez width et height par les dimensions désirées
        resized_image = image.resize(new_size)
        
        self.image = ImageTk.PhotoImage(resized_image)
        self.y1=self.y1+15
        
        
        
        #Création du tank , on l'a nommé ovale
        self.ovale = boss.create_image(self.x1,self.y1, image=self.image)
        
        self.label_score = Label(self.boss, text="Score: 0", bg="lightgreen", font=("ds-digital", 22, "bold"))
        self.label_score.place(x=190, y=20)
        
        
        self.label_time = Label(self.boss, text="time: 60", bg="lime", font=("ds-digital", 22, "bold"))
        self.label_time.place(x=50, y=20)
        
        
        
        #Création des images vie en haut à droite
        
        image_vie1 = Image.open("./images/vie.png")
        
        
        # Redimensionner  à la taille souhaitée
        new_size_vie1 = (30, 30)  # Remplacez width et height par les dimensions désirées
        resized_image_vie1 = image_vie1.resize(new_size_vie1)

        # Créer un objet PhotoImage à partir de l'image redimensionnée 
        self.image_vie1_tk = ImageTk.PhotoImage(resized_image_vie1)

        # Créer l'image
        self.vie1 = boss.create_image(650 , 40 , image=self.image_vie1_tk)
        
        image_vie2 = Image.open("./images/vie.png")
        
        
        # Redimensionner à la taille souhaitée
        new_size_vie2 = (30, 30)  # Remplacez width et height par les dimensions désirées
        resized_image_vie2 = image_vie2.resize(new_size_vie2)

        # Créer un objet PhotoImage à partir de l'image redimensionnée 
        self.image_vie2_tk = ImageTk.PhotoImage(resized_image_vie2)

        # Créer  l'image
        self.vie2 = boss.create_image(700 , 40 , image=self.image_vie2_tk)
        
        image_vie3 = Image.open("./images/vie.png")
        
        
        # Redimensionner l'image à taille souhaitée
        new_size_vie3 = (30, 30)  # Remplacez width et height par les dimensions désirées
        resized_image_vie3 = image_vie3.resize(new_size_vie3)

        # Créer un objet PhotoImage à partir de l'image redimensionnée 
        self.image_vie3_tk = ImageTk.PhotoImage(resized_image_vie3)

        # Créer  l'image
        self.vie3 = boss.create_image(750 , 40 , image=self.image_vie3_tk)
        
        image_cible = Image.open("./images/mig.png")
        
        
        # Redimensionner l'image de la cible à la taille souhaitée
        new_size_cible = (190, 200)  # Remplacez width et height par les dimensions désirées
        resized_image_cible = image_cible.resize(new_size_cible)

        # Créer un objet PhotoImage à partir de l'image redimensionnée de la cible
        self.image_cible_tk = ImageTk.PhotoImage(resized_image_cible)

        # Créer la cible en utilisant l'image
        self.cible1 = boss.create_image(100 , 120 , image=self.image_cible_tk)
        self.jeu_en_cours=True#Variable pour l'etat de jeu
        self.score=0#Initaliser le score à 0
        self.time=0#Initaliser l'heure à 0
        self.time_true=False#Une variable pour arreter le timer
        
        
        """ Des listes pour stocker les images comme les explosions el les missiles du cibles"""
        self.explosion_images = [] 
        self.obus_enemy=[]
        self.bullet_images=[]
        self.nouveaux_obus_enemy=[]
        
        """Variable pour les emplacements du migue et pour le deplacements"""
        self.x_migue=100
        self.y_migue=150
        self.dx_migue=3
        self.dy_migue=4
        self.dy_enemy=1
        self.missile_time=1000
        self.bullet_loop=True#Une booleen pour faire marcher le boucle des balles du cibles
        self.id3=1#Initialisation du timer , utiliser pour
        
        self.missile_time_decremente()#Pour commencer l'incrementation du temps
        
        #Utilisation de pygame les sons
        pygame.mixer.init()
        #Utilisation des canals pour que les sons ne s'emmele pas
        self.channel1 = pygame.mixer.Channel(0)
        self.channel2 = pygame.mixer.Channel(1)
        self.channel3 = pygame.mixer.Channel(2)
        self.lire_la_musique()#Lire la musique de fond
        self.mettre_a_jour_position()#Déplacer la cible
        
        self.vie=[self.vie1,self.vie2,self.vie3]#Ajout des vies du tank dans une liste vie
        self.index=0
    
    """Début des fonctions"""
    """Fonction pour l'etat du jeu"""
    #Fonction game_over qui change l'etat du jeu
    def game_over(self):
        self.jeu_en_cours=False
    
    #Fonction pour restarter le jeu
    def restart_game(self):
        # Réinitialiser les attributs du canon
        self.angle = 0
        self.x2 = self.x1 + self.lbu
        self.y2 = self.y1 - self.lbu * sin(self.angle)


        # Supprimer les éléments graphiques existants
        self.boss.delete(self.ovale)
        self.boss.delete(self.buse)
        self.boss.delete(self.cible1)
        self.boss.delete(self.vie1)
        self.boss.delete(self.vie2)
        self.boss.delete(self.vie3)
        if self.time_true:
            self.label_gameover.destroy()
            self.label_affichescore.destroy()
        
        
        # Recréer les éléments 
        self.buse = self.boss.create_line(self.x1-7, self.y1, self.x2, self.y2-10, width=5)
        self.ovale = self.boss.create_image(self.x1, self.y1, image=self.image)
        self.cible1 = self.boss.create_image(100 , 120 , image=self.image_cible_tk)
        self.vie1 = self.boss.create_image(650 , 40 , image=self.image_vie1_tk)
        self.vie2 = self.boss.create_image(700 , 40 , image=self.image_vie2_tk)
        self.vie3 = self.boss.create_image(750 , 40 , image=self.image_vie3_tk)
        # Réinitialiser les compteurs
        self.score = 0
        self.label_score.configure(text="Score: 0")

        self.time = 0
        self.label_time.configure(text="Time: 0")

        # Réinitialiser les états du jeu
        self.jeu_en_cours = True
        
        
        #Arreter le timeur du fonction time_decremente
        self.boss.after_cancel(self.id)
        self.boss.after_cancel(self.id2)
        self.index=0
        self.vie=[]
        self.vie=[self.vie1,self.vie2,self.vie3]
        self.time_decremente()
        self.mettre_a_jour_position()
        
    
    """Fonction pour les deplacements automatiques avec le temps"""
    #Fonction pour le deplacement du missile avec le decrementation
    def missile_time_decremente(self):
        self.missile_time-=1
        self.enemy_ball()
        self.boss.after(1000, self.missile_time_decremente)
        
    def time_decremente(self):
        self.time+=1
        self.label_time.configure(text="Time:" +str(self.time))
        self.id=self.boss.after(1000, self.time_decremente)
    
    
    """Fonction pour l'affichage des explosions"""
    #Explosion sur la cible
    def afficher_explosion2(self, x, y):
        # Ouvrir le fichier GIF
        image_explosion = Image.open("./images/explosion.png")

        # Redimensionner l'image si nécessaire
        image_explosion = image_explosion.resize((50, 50))

        # Créer une instance de ImageTk.PhotoImage pour afficher l'image dans une interface graphique
        explosion_tk = ImageTk.PhotoImage(image_explosion)

        # Ajouter l'image à une liste ou un conteneur pour une utilisation ultérieure
        self.explosion_images.append(explosion_tk)

        # Créer une image à partir de l'image ouverte dans une interface graphique
        self.image_explode2 = self.boss.create_image(x, y, image=explosion_tk)
    
    def afficher_explosion_sol(self, x, y):
        # Ouvrir le fichier GIF
        image_explosion = Image.open("./images/tany_mipoka.png")

        # Redimensionner l'image si nécessaire
        image_explosion = image_explosion.resize((50, 50))

        # Créer une instance de ImageTk.PhotoImage pour afficher l'image dans une interface graphique
        explosion_tk = ImageTk.PhotoImage(image_explosion)

        # Ajouter l'image à une liste ou un conteneur pour une utilisation ultérieure
        self.explosion_images.append(explosion_tk)

        # Créer une image à partir de l'image ouverte dans une interface graphique
        self.image_explode = self.boss.create_image(x, y, image=explosion_tk)
    

                
    #Fonctions pour l'explosion devant la buse
    def afficher_explosionbuse(self, x, y):
        # Ouvrir le fichier GIF
        image_explosion = Image.open("./images/flash.png")

        # Redimensionner l'image si nécessaire
        image_explosion = image_explosion.resize((20, 20))

        # Créer une instance de ImageTk.PhotoImage pour afficher l'image dans une interface graphique
        explosion_tk = ImageTk.PhotoImage(image_explosion)

        # Ajouter l'image à une liste ou un conteneur pour une utilisation ultérieure
        self.explosion_images.append(explosion_tk)

        # Créer une image à partir de l'image ouverte dans une interface graphique
        self.image_explodebuse = self.boss.create_image(x, y, image=explosion_tk)
        
    
    #Fonction pour supprimer l'image de l'explosion
    def supprimer_explosionbuse(self):
        self.boss.delete(self.image_explodebuse)
        
        #Supprimer les images de l'explosion
    def supprimer_images(self):
        self.boss.delete(self.image_explode2)
    def supprimer_images_sol(self):
        self.boss.delete(self.image_explode)
       
       
       
    """Fonction pour les detection de collision"""
    #Détection des collisions avec les cibles
    def detecter_collision(self, obus):
        "Vérifier si l'obus touche la cible"
        coord_obus = self.boss.coords(obus)
        coord_cible1 = self.boss.coords(self.cible1)
        if coord_obus[2]+25 >= (coord_cible1[0]) and coord_obus[0]-25 <= coord_cible1[0] and coord_obus[3]+20 >= (coord_cible1[1]) and coord_obus[1]-20 <= coord_cible1[1]:
            # Instructions exécutées lorsque l'obus touche la cible
            self.afficher_explosion2(coord_cible1[0]+5, coord_cible1[1]) # Afficher l'explosion à la position de la cible
            self.boss.after(200, self.supprimer_images)
            self.explosion_migue_song()
            self.boss.delete(self.cible1)
            self.cible1 = self.boss.create_image(100 , 120 , image=self.image_cible_tk)
            self.boss.after_cancel(self.id2)
            self.mettre_a_jour_position()
            return True
        return False
    
    #Détection des collisions avec le tank
    def detecter_collision_bullet(self):
        "Vérifier si l'obus touche la cible"
        coord_ovale = self.boss.coords(self.ovale)

        indices_a_supprimer = []
        sol_a_supprimer=[]
        if self.bullet_loop:
            for i, obus_enemy in enumerate(self.obus_enemy):
                coord_obus_enemy = self.boss.coords(obus_enemy)

                if coord_ovale[0]-40 <= coord_obus_enemy[0] <= coord_ovale[0] + 50 and \
                coord_ovale[1]-30 <= coord_obus_enemy[1] <= coord_ovale[1] + 50:
                    indices_a_supprimer.append(i)
                    
                elif  500 <= coord_obus_enemy[1] <=  600:
                    sol_a_supprimer.append(i)
                    for index in reversed(sol_a_supprimer):
                        self.boss.delete(self.obus_enemy[index])
                        self.boss.delete(self.bullet_images[index])
                        self.obus_enemy.pop(index)
                        self.bullet_images.pop(index)
                        self.afficher_explosion_sol(coord_obus_enemy[0], coord_obus_enemy[1])
                        self.boss.after(200, self.supprimer_images_sol)
        
            # Supprimer les obus enemy et les images de balle correspondantes
            for index in reversed(indices_a_supprimer):
                self.boss.delete(self.obus_enemy[index])
                self.boss.delete(self.bullet_images[index])
                self.obus_enemy.pop(index)
                self.afficher_explosion_sol(coord_ovale[0], coord_ovale[1])
                self.boss.after(200, self.supprimer_images_sol)
                self.bullet_images.pop(index)
                #Fonction pour le game over
                if self.index==2:
                    self.label_gameover = Label(self.boss,text="Game Over" , bg="skyblue",fg="red", font=("ds-digital", 30, "bold"))
                    self.label_gameover.place(x=350, y=200)
                    self.label_affichescore = Label(self.boss,text="Score:"+str(self.score) , bg="skyblue",fg="red" , font=("ds-digital", 30, "bold"))
                    self.label_affichescore.place(x=350, y=300)
                    self.boss.delete(self.buse)
                    self.boss.delete(self.ovale)
                    self.gameover_song()
                    self.boss.after_cancel(self.id)
                    self.game_over()
                    self.bullet_loop=False
                self.boss.delete(self.vie[self.index])
                self.index+=1
        
        
    """Déplacement du buse"""
    def deplacer_buse(self, event):
        "Déplacer la buse du canon en fonction de la valeur de la molette de la souris"
        x = event.x
        self.x1=x
        delta = event.delta  # Valeur du défilement de la molette de la souris
        self.angle += delta * pi / 2000  # Convertit la valeur du défilement en radians
        self.angle = max(0, min(self.angle, pi))  # Limite l'angle entre 0 et pi (180 degrés)
        self.x2 = self.x1 + self.lbu * cos(self.angle)
        self.y2 = self.y1 - self.lbu * sin(self.angle)
        self.boss.coords(self.buse, self.x1-7, self.y1-10, self.x2, self.y2-10)
        
        
    """Déplcaments du tank"""
    def deplacer_ovale(self, event):
        "Déplacer l'ovale en fonction du mouvement de la souris"
        x = event.x
        y = self.y1  # Conserver la valeur actuelle de self.y1 pour l'origine de la bus
        self.boss.coords(self.ovale, x, y)  # Mettre à jour les coordonnées de l'ovale
        self.x1 = x  # Mettre à jour la coordonnée x de l'axe de rotation du canon
        self.x2 = self.x1 + self.lbu * cos(self.angle)
        self.y2 = self.y1 - self.lbu * sin(self.angle)
        self.boss.coords(self.buse, self.x1-7, self.y1-10, self.x2, self.y2-10)  # Mettre à jour les coordonnées de la buse

    
    #Fonction Incremetation score
    def incrementer_score(self):
        self.score += 1
        self.label_score.configure(text="Score: " + str(self.score))

    
    
    
    """Déplcaments"""
    def enemy_ball(self):
        if self.bullet_loop:
            coords_migue = self.boss.coords(self.cible1)
            image_bullet = Image.open("./images/bombe.png")
            image_bullet = image_bullet.resize((30, 30))
            bullet_tk = ImageTk.PhotoImage(image_bullet)
            self.bullet_images.append(bullet_tk)
            new_obus_enemy = self.boss.create_image(coords_migue[0], coords_migue[1], image=bullet_tk)
            self.obus_enemy.append(new_obus_enemy)
            self.animer_enemy_ball()
        
    """Animer missile cible"""
    def animer_enemy_ball(self):
        indices_a_supprimer = []
        for i, obus_enemy in enumerate(self.obus_enemy):
            self.boss.move(obus_enemy, 0, self.dy_enemy)
            c = self.boss.coords(obus_enemy)
            if c[1] < 0 or c[1] >= self.boss.winfo_height():
                indices_a_supprimer.append(i)

        # Supprimer les éléments marqués pour suppression
        for index in reversed(indices_a_supprimer):
            self.boss.delete(self.obus_enemy[index])
            self.boss.delete(self.bullet_images[index])
            self.obus_enemy.pop(index)
            self.bullet_images.pop(index)
            
        self.boss.after_cancel(self.id3)#Pour faire stoper les timer
        self.detecter_collision_bullet()
        self.id3 = self.boss.after(10, self.animer_enemy_ball)



    """Fonction pour tirer"""
    def feu(self, event):
        "Tir d'un obus"
        if self.jeu_en_cours:
            self.explosion_song()
            obus = self.boss.create_oval(self.x2 - 3, self.y2 - 3, self.x2 + 3, self.y2 + 3, fill='red')
            v = 17  # vitesse initiale
            vy = -v * sin(self.angle)
            vx = v * cos(self.angle)
            self.animer_obus(obus, vx, vy)
            self.afficher_explosionbuse(self.x2+3 ,self.y2-7)
            self.boss.after(500, self.supprimer_explosionbuse)
            
    """Fonction pour animer_la balle"""
    def animer_obus(self, obus, vx, vy):
        "Animer l'obus (trajectoire balistique)"
        self.boss.move(obus, int(vx), int(vy))
        c = self.boss.coords(obus)  # coordonnées résultantes
        vy += 0.3  # accélération verticale
        if c[3] < self.boss.winfo_height():#Condition s'il sorte canvas
            if self.detecter_collision(obus):#Collision à la cible
                self.incrementer_score()
                self.boss.delete(obus) 
            else:
                self.boss.after(20, self.animer_obus, obus, vx, vy)
        else:
            # Animation terminée - supprimer l'obus
            self.boss.delete(obus)



    
    #Mettre à jour à la position du cible
    def mettre_a_jour_position(self):
        coord_cible1=self.boss.coords(self.cible1)
        self.y_move=3
        if  coord_cible1[0]>=800:
            self.boss.delete(self.cible1)
            self.cible1 = self.boss.create_image(5 , 120 , image=self.image_cible_tk)
        if not 5<coord_cible1[1]<100:
            self.y_move=-self.y_move
        self.boss.move(self.cible1,self.dx_migue, self.y_move)  # Déplacer l'ovale selon les déplacements
        # Appeler à nouveau la fonction après 30 millisecondes
        self.id2=self.boss.after(30,self.mettre_a_jour_position)

         
    """Fonction pour les barres de menus"""
    def open_about(self):
        msg = Toplevel()
        Message(msg, width=200, aspect=100, justify=CENTER,
                text="Tank Game\n\n(C) Team Alpha, Juin 2023.\nDigital Mission Project\nVersion 1.0",bg='royal blue',fg='white').pack(padx=3, pady=3)
    
    def help_me(self):
        msg = Toplevel()
        Message(msg, width=200, aspect=100, justify=CENTER,
                text="Les principes de jeu c'est de tirer le plus sur les cibles\nRéf : Projet 'Digital mission' - Juin 2023",bg='royal blue',fg='white').pack(padx=3, pady=3)
    
    """Fonction pour les sons"""
    def gameover_song(self):
        # Initialisation de Pygame
        pygame.mixer.init()

        # Charger le fichier audio
        pygame.mixer.music.load("./images/laugh.wav")

        # Jouer le fichier audio
        pygame.mixer.music.play()
    
    def explosion_migue_song(self):
        sound = pygame.mixer.Sound("./images/crash.wav")

        # Jouer le fichier audio sur le premier canal
        self.channel1.play(sound)
        
            
    def explosion_song(self):
        # Charger le fichier audio
        sound = pygame.mixer.Sound("./images/explosionsong.mp3")

        # Jouer le fichier audio sur le deuxième canal
        self.channel2.play(sound)
    
        
    def lire_la_musique(self):
        # Charger le fichier audio
        pygame.mixer.music.load("./images/fond.mp3")
        pygame.mixer.music.set_volume(0.10)
        # Jouer le fichier audio en boucle en arrière-plan
        pygame.mixer.music.play(-1)


if __name__ == '__main__':
    # Code pour tester sommairement la classe Canon :
    f = ctk.CTk()
    
    f.title("Tank")
    can = Canvas(f, width=800, height=600, bg='skyblue')
    can.pack(padx=10, pady=10)
  
    c1 = Canon(can, 180, 470)
    menubar = Menu(f)
    # Menu Fichier
    
    
    file_menu = Menu(menubar,tearoff=0)
    file_menu.add_command(label="Restart",command=c1.restart_game)
    file_menu.add_command(label="Aide",command=c1.help_me)
    file_menu.add_command(label="A propos",command=c1.open_about)
    file_menu.add_command(label="Quitter",command=f.quit)
    f.config(menu=menubar)
    
    c1.time_decremente()
    f.mainloop()
