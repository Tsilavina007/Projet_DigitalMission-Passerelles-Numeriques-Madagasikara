import tkinter as tk
import time
from tkinter import Button, Label
from random import randrange # Importe la fonction randrange de la bibliothèque random pour générer des nombres aléatoires
import tkinter.font as tkfont
from tkinter import ttk
from PIL import ImageTk, Image
import pygame 
from tkinter.ttk import Style

# Fonction pour fermer la fenêtre actuelle et importer le fichier "Accueil.py"
def return_accueil():
    tout.destroy()
    import Accueil

# Fonction pour jouer de la musique
def play_music(): 
    sound=pygame.mixer.Sound(r"C:\Users\MIANTSA\Desktop\Python_puzzle_Miantsa\Professor Layton & The Miracle Mask - Puzzles Abound [Extended].mp3")
    channel1.play(sound)

# Fonction pour jouer un son de clic
def play_click_song(): 
    sound=pygame.mixer.Sound(r"C:\Users\MIANTSA\Desktop\Python_puzzle_Miantsa\click_song.mp3")
    channel2.play(sound)

# Fonction pour arrêter la musique
def stop_music(): 
    channel1.stop()

DELTA = 20  # Valeur utilisée pour l'animation de déplacement des tuiles
DIST = 10  # Distance parcourue à chaque itération de l'animation
moving = 0  # Compteur pour suivre le nombre d'éléments en mouvement

bravo= False # Variable pour indiquer si le joueur a réussi le puzzle

# Fonction pour réinitialiser le compteur de temps
def reset_timer(): 
    global seconds
    seconds = 0

# Fonction pour démarrer le compteur de temps
def start_timer(): 
    reset_timer()
    global seconds, id_timer
    seconds = 0
    if id_timer is not None:
        timer_label.after_cancel(id_timer)
    update_timer()
    
# Fonction pour mettre à jour le compteur de temps    
def update_timer(): 
    global seconds,id_timer
    seconds += 1
    time_text = format_time(seconds)
    timer_label.config(text=time_text)

    if not bravo:
        id_timer=timer_label.after(1000, update_timer)
        timer_booleen=False

# Fonction pour formater le temps au format "hh:mm:ss"
def format_time(seconds): 
    minutes = seconds // 60
    seconds = seconds % 60
    hours = minutes // 60
    minutes = minutes % 60
    time_text = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
    return time_text

# Fonction pour calculer les mouvements valides d'une tuile
def multi(orig, vide): 
    i, j=orig
    ii, jj=vide
    delta =(di, dj)=(ii-i, jj-j)
    if di!=0!=dj or di==dj==0:
        return None
    norm=max(abs(di), abs(dj))

    dirx, diry =(di//norm, dj//norm)
    L=[((ii-dirx, jj-diry), (ii, jj))]

    for k in range(norm-1):
        (a, b), destn=L[-1]
        pos=((a-dirx, b-diry), (a, b))
        L.append(pos)
    return L, (dirx, diry)

# Fonction pour animer le déplacement d'une tuile
def anim(item, target, drtn): 
    global moving
    L =cnv.coords(item)
    a=L[0]
    b=L[1]
    x, y=target
    u, v=drtn
    d=u*(x-a)+v*(y-b)
    if d>DIST:
        cnv.move(item, u*DIST, v*DIST)
        cnv.after(DELTA, anim, item, target, drtn)
    else:
        cnv.move(item, (x-a), (y-b))
        moving-=1

# Fonction pour effectuer le déplacement d'une tuile
def move_tile(orig, dstn, drtn):
    global moving
    i, j=orig
    nro=board[i][j]
    rect, txt=items[nro]
    ii, jj =dstn
    target=100*jj, 100*ii
    target_txt=100*jj+50, 100*ii+50

    anim(rect, target, drtn)
    anim(txt, target_txt, drtn)
    moving+=2

    board[i][j],board[ii][jj]=board[ii][jj], board[i][j]

# Fonction pour afficher un message de félicitations
def congrat():
    global bravo
    if not moving:
        sound=pygame.mixer.Sound(r"C:\Users\MIANTSA\Desktop\Python_puzzle_Miantsa\winner_song.mp3")
        channel3.play(sound)
        lbl.configure(text="Congratulations!")
        bravo=True
    else:
        cnv.after(20, congrat)

# Fonction appelée lorsqu'un clic de souris est détecté sur le canvas
def clic(event):
    global i_vide, j_vide
    play_click_song()
    if bravo:
        return
    i=event.y//100
    j=event.x//100

    r=multi((i,j), (i_vide, j_vide))
    if (r is None) or moving:
        return
    L, drtn=r
    for orig, dstn in L:
        move_tile(orig, dstn, drtn[::-1])
    i_vide=i
    j_vide=j
    if board==win:
        congrat()

# Fonction pour obtenir les positions voisines valides d'une case
def voisins(n, i, j):
    return [(a,b) for (a, b) in
            [(i, j+1),(i, j-1), (i-1, j), (i+1,j)]
            if a in range(n) and b in range(n)]

# Fonction pour effectuer un échange aléatoire de la case vide avec l'une de ses voisines
def echange(board, vide):
    i, j=vide
    V=voisins(4, i, j)
    ii, jj=V[randrange(len(V))]
    board[ii][jj], board[i][j]=board[i][j],board[ii][jj]
    return ii, jj

# Fonction pour déplacer la case vide vers le bas et vers la droite dans le tableau
def normal(board, vide):
    i_vide, j_vide = vide
    for i in range(i_vide, 4):
        (board[i][j_vide], board[i_vide][j_vide])= (
            board[i_vide][j_vide], board[i][j_vide])
        i_vide=i
    for j in range(j_vide, 4):
        board[i_vide][j], board[i_vide][j_vide]= (
            board[i_vide][j_vide],board[i_vide][j])
        j_vide=j

# Fonction pour mélanger le tableau de jeu
def melanger(N):
    global bravo
    bravo=False
    start_timer()
    board=[[4*lin+1+col for col in range(4)]
        for lin in range(4)]

    vide=(3,3)

    for i in range(N):
        vide=echange(board, vide)
    return board

# Fonction pour initialiser le jeu
def init(N=1000):
    global i_vide, j_vide, items, board, bravo
    cnv.delete("all")
    items=[None]

    board=melanger(N)
    for i in range(4):
        for j in range(4):
            if board[i][j]==16:
                i_vide, j_vide=i, j
    vide=i_vide, j_vide
    normal(board, vide)
    i_vide, j_vide=3,3
    items=[None for i in range(17)]

    for i in range(4):
        for j in range(4):
            x, y = 100*j, 100*i
            A, B, C = (x, y), (x+100, y+100), (x+50, y+50)
            rect = cnv.create_rectangle(A, B, fill="#A9A9A9", outline="#CD5C5C", width=5, stipple="gray50")
            nro = board[i][j]
            txt = cnv.create_text(C, text=nro, fill="white", font=FONT, anchor='center', justify='center')
            items[nro] = (rect, txt)
    rect, txt=items[16]
    cnv.delete(txt)
    cnv.delete(rect)
    lbl.configure(text="")
    bravo=False
    
    def on_enter(event):
        cnv.itemconfig(txt, outline="#CD5C5C")

    def on_leave(event):
        cnv.itemconfig(txt, outline="")

    def f():
        print("TODO")    
        # Association des événements de la souris
        cnv.tag_bind(txt, "<Enter>", on_enter)
        cnv.tag_bind(txt, "<Leave>", on_leave)
        cnv.delete(rect)
        cnv.delete(txt)

win=[[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]

# Création de la fenêtre principale
tout = tk.Tk()
tout.geometry('1500x1000',)
tout.title('Puzzle')

# Création de l'icône et le titre de l'application 
icon_path=r"C:\Users\MIANTSA\Desktop\Python_puzzle_Miantsa\logo.ico"
tout.iconbitmap(icon_path)

# Icône pour revenir à la page d'accueil
image_path1 = r"C:\Users\MIANTSA\Desktop\Python_puzzle_Miantsa\Revenir1.png"
image1 = Image.open(image_path1)
image1 = image1.resize((30, 30), Image.ANTIALIAS)  # Définir la nouvelle taille de l'image
image1 = ImageTk.PhotoImage(image1)

# Initialise le module mixer de pygame pour la gestion du son
pygame.mixer.init()

#variable 
id_timer = None

# Réinitialise le module mixer de pygame
pygame.mixer.init()
channel1 = pygame.mixer.Channel(0)  # Crée un canal audio pour la musique
channel2 = pygame.mixer.Channel(1)  # Crée un canal audio pour le son de clic
channel3 = pygame.mixer.Channel(2)  # Crée un canal audio pour le son de victoire

# Charge l'image de fond
image = Image.open(r"C:\Users\MIANTSA\Desktop\Python_puzzle_Miantsa\fond.png")
image = image.resize((1500, 1000), Image.LANCZOS)  
background_image = ImageTk.PhotoImage(image) # Convertit l'image en un format compatible avec tkinter
background_label = tk.Label(tout, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#Pour recherchez des polices disponibles sur le système
available_fonts = tkfont.families()
print(available_fonts)

# Affiche une étiquette avec le titre du jeu
etiquette = tk.Label(tout, text="Fifteen Puzzle Game", bg="#4B0082", fg="white", width=19, height=2, font=('Lumanosimo', 20, 'bold'))
etiquette.pack()

C = (200, 200) # Coordonnées du centre du canvas
FONT = ('Lumanosimo', 20, 'bold')
cnv = tk.Canvas(tout, width=400, height=400, bg='#4B0082',)
cnv.pack(side='left',padx=(160,100), pady=((40,20)))# Centrer le canvas au milieu de la fenêtre principale

# Ajouter un contour rouge autour du canvas
cnv.create_rectangle(0, 0, 400, 400, outline="red", width=5)
police_TITRE = tkfont.Font(size=40)

# Affiche un bouton pour Reset les tuiles 
btn=Button(text="Reset", command=init, font=('Lumanosimo',20, 'bold'), bg="#4B0082", fg="white", width=17, height=2)
btn.pack(side='top',pady=(130,0), padx=(0,360))

# Affiche une étiquette pour afficher un message de victoire
lbl=Label(text="      ",font=('Lumanosimo', 20, 'bold'),
          justify='center', width=16, height=18)
lbl.pack(side="left", padx=(20,0), pady=(0,100) )

# Affiche un conteneur pour les boutons stylés
button_container = ttk.Frame(tout)
button_container.pack()

# Affiche un bouton pour démarrer le compteur de temps
start_button = tk.Button(tout, text="Start", command=start_timer, width=11, height=2, font=('Lumanosimo', 17, 'bold'), bg="#8B0000")
start_button.pack()

# Affiche une étiquette pour afficher le compteur de temps
timer_label = tk.Label(font=("Tektur", 17), fg="black", width=13, height=8 )
timer_label.pack(pady=(0,110))

# Configure le style du bouton de lecture et d'arrêt de musique
style = Style()
style.configure('Play.TButton', font=('FontAwesome', 12), foreground='green')
style.configure('Stop.TButton', font=('FontAwesome', 12), foreground='red')
style.map('Play.TButton',
          foreground=[('active', 'green')],
          background=[('active', 'white')])
style.map('Stop.TButton',
          foreground=[('active', 'red')],
          background=[('active', 'white')])

# Affiche un bouton de lecture de musique stylé à gauche du conteneur
play_button = ttk.Button(button_container, text='\uf04b', style='Play.TButton', command=play_music)
play_button.pack(side='left', padx=10)

# Affiche un bouton d'arrêt de la musique stylé à gauche du bouton de lecture
stop_button = ttk.Button(button_container, text='\uf04d', style='Stop.TButton', command=stop_music)
stop_button.pack(side='left', padx=10)

# Bouton pour faire revenir à la page d'accueil
quit_button = Button(image=image1, command=return_accueil ,bd=4, highlightthickness=5, highlightbackground="black")
quit_button.place(x=0, y=0)  

# Configure le style du conteneur des boutons
style = ttk.Style()
style.configure('Flex.TFrame', flexgrid='true')
button_container.configure(style='Flex.TFrame')

# Démarre le compteur de temps
start_timer()

# Lie la fonction clic à l'événement clic de la souris sur le canvas
cnv.bind("<Button-1>",clic)

# Initialise le jeu
init()

tout.mainloop()
