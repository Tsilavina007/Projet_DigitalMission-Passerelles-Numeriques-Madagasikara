import tkinter as tk
from tkinter import messagebox
from tkinter import font
import random
from PIL import Image, ImageTk
import pygame

# Créer une fenêtre Tkinter
root = tk.Tk()
root.resizable(False, False)
root.geometry("780x629")
root.title("Jeu de Mémoire")
# Définir la couleur de fond de la fenêtre
root.configure(bg="skyblue")

# Créer une police personnalisée en spécifiant la famille, la taille et le style
custom_font = font.Font(family="Times New Roman", size=12, slant="italic")

#creer un label pour un score
score = 0
score_label = tk.Label(root, text="Score : {}".format(score), font = custom_font, bg="skyblue", padx=5, pady =15)
score_label.place(relx=0.005, rely=0.01)

#Creer une frame pour
frame = tk.Frame(root, bg="red",  width=600, height=520)
frame.place(anchor="center", relx=0.5, rely=0.495)

# Liste des noms de fichiers d'images
noms_images = [(1,'Lm.png'), (2,'CRIS.jpg'), (3,'MRE.png'), (4,'PC.png'),(4,'PC.png'),(3,'MRE.png'), (2,'CRIS.jpg'), (1,'Lm.png'),
               (5,'EH.png'), (6,'Grii.png'), (7,'TS.png'), (8,'KM.png'), (8,'KM.png'), (7,'TS.png'), (6,'Grii.png'), (5,'EH.png')]


numeros_images = {}
numero = 1
# Liste pour stocker les chemins complets des images
chemins_images = []
# Charger les images et les stocker dans la liste des chemins d'images
for nom in noms_images:
    nom_id , nom_img = nom
    #chemin_image = f'D:/Python_Projet_Personnel/MyProject/{nom_img}'
    chemin_image = f'C:/Users/PN/Desktop/Projet_Personnel_Python_Didier_JEU_de_MEMOIRE/{nom_img}'
    chemin_image_id = nom_id, chemin_image
    chemins_images.append(chemin_image_id)


# Créer les objets PhotoImage lorsqu'on en a besoin
Joueurs = []
for chemin_image_s in chemins_images:
    chemin_id , chemin_image = chemin_image_s
    image_pil = Image.open(chemin_image)
    nouvelle_largeur = 150
    nouvelle_hauteur = 150
    image_redim = image_pil.resize((nouvelle_largeur, nouvelle_hauteur))
    photo_redim = ImageTk.PhotoImage(image_redim)
    photo_redim_id = chemin_id, photo_redim
    Joueurs.append(photo_redim_id)

# Mélanger les images
random.shuffle(Joueurs)
#Creer une grande liste pour les listes de stockage des images
buttons = []
#Creer listes de stockage des images
img_row1 = []
img_row2 = []
img_row3 = []
img_row4 = []
#PStcoker des images dans une liste de stockage
for i , img in enumerate(Joueurs):

    if i==0 or i==1 or i==2 or i==3:
        img_row1.append(img)
    elif i == 4 or i == 5 or i == 6 or i == 7:
        img_row2.append(img)
    elif i == 8 or i == 9 or i == 10 or i == 11:
        img_row3.append(img)
    elif i == 12 or i == 13 or i == 14 or i == 15:
        img_row4.append(img)
#Stocker chaque liste de stockage dans une autre liste
Joueurs1 = []
Joueurs1.append(img_row1)
Joueurs1.append(img_row2)
Joueurs1.append(img_row3)
Joueurs1.append(img_row4)

# Créer une liste vide nommée id_btn avec 4 sous-listes vides
id_btn=[[], [], [], []]
# Remplir la liste id_btn avec des entiers de 0 à 3 inclus
for x in range(4):
    for y in range(4):
        id_btn[x].append(y)

# Initialisation des variables
num_clicks = 0
prev_row = None
prev_column = None

# Creer un canva pour le frame, le bouton qui ser a rejouer le jeu, le score
can = tk.Canvas(root, width=400, height=400, bg='skyblue')

# Image de dos de carte (à masquer)
# Chargez l'image avec PIL
dos_carte_image = Image.open('C:/Users/PN/Desktop/Projet_Personnel_Python_Didier_JEU_de_MEMOIRE/MES.jpg')
# Nouvelles dimensions de l'image
nouvelle_largeur = 150
nouvelle_hauteur = 150
# Redimensionnez l'image
image_redime = dos_carte_image.resize((nouvelle_largeur, nouvelle_hauteur,))
# Convertissez l'image redimensionnée en objet PhotoImage
photo_redime = ImageTk.PhotoImage(image_redime)


# Fonction pour masquer les cases avec l'image de dos de carte
def hide_cards():
    global row, column, prev_row, prev_column
    buttons[prev_row][prev_column].config(image=photo_redime)
    buttons[prev_row][prev_column].bind("<Button-1>", lambda event, r=prev_row, c=prev_column: click_case(r, c))
    buttons[row][column].config(image=photo_redime)
    buttons[row][column].bind("<Button-1>", lambda event, r=row, c=column: click_case(r, c))

# Fonction appelee pour refaire le jeu
def reset():
    global button, photo_redime, buttons, Joueurs, Joueurs1, score, score_label
    score = 0
    score_label = tk.Label(root, text="Score : {}".format(score), font=custom_font, bg="skyblue", padx=5, pady=15)
    score_label.place(relx=0.005, rely=0.01)
    random.shuffle(Joueurs)
    # Creer listes de stockage des images
    img_row1 = []
    img_row2 = []
    img_row3 = []
    img_row4 = []
    # Stcoker des images dans une liste de stockage
    for i, img in enumerate(Joueurs):

        if i == 0 or i == 1 or i == 2 or i == 3:
            img_row1.append(img)
        elif i == 4 or i == 5 or i == 6 or i == 7:
            img_row2.append(img)
        elif i == 8 or i == 9 or i == 10 or i == 11:
            img_row3.append(img)
        elif i == 12 or i == 13 or i == 14 or i == 15:
            img_row4.append(img)
    # Stocker chaque liste de stockage dans une autre liste
    Joueurs1 = []
    Joueurs1.append(img_row1)
    Joueurs1.append(img_row2)
    Joueurs1.append(img_row3)
    Joueurs1.append(img_row4)
    # Stocker dans une grnade liste tous les boutons avec l'image qui cache les images a chercher
    buttons = []
    for row in range(4):
        button_row = []
        for column in range(4):
            button = tk.Button(frame, width=150, height=150, image=photo_redime)
            button.grid(row=row, column=column)
            button.bind("<Button-1>", lambda event, r=row, c=column: click_case(r, c))
            button_row.append(button)
        buttons.append(button_row)
    arreter_son()

# Créer un bouton avec du texte et utiliser la police personnalisée
bttn = tk.Button(root, text="Rejouer!", bg="blue", fg= "white", font ="oblique", command= reset)
bttn.place(relx=0.905, rely=0)

# Créer les boutons pour les cases
buttons = []
for row in range(4):
    button_row = []
    for column in range(4):
        button = tk.Button(frame, width=150, height=150, image= photo_redime)
        button.grid(row=row, column=column)
        button.bind("<Button-1>", lambda event, r=row, c=column: click_case(r, c))
        button_row.append(button)
    buttons.append(button_row)

# Fonction appelée lorsque le joueur clique sur une case
def click_case(row1, column1):
    global first_click, prev_row, prev_column, num_clicks, row, column, id_img1, id_img2, score, score_label

    num_clicks += 1

    if num_clicks % 2 != 0:
        row, column = row1, column1
        # Afficher l'image de la case
        image = Joueurs1[row][column]
        id_img1, image_img1 = image
        id1 = id_btn[row][column]
        print(row, column)
        print(id1)
        buttons[row][column].config(image=image_img1)
        buttons[row][column].image = photo_redim
        buttons[row][column].unbind("<Button-1>")
    if num_clicks % 2 == 0:
        prev_row, prev_column = row1, column1
        # Afficher l'image de la case
        id2 = id_btn[prev_row][prev_column]
        print(prev_row, prev_column)
        print(id2)
        image = Joueurs1[prev_row][prev_column]
        id_img2, image_img2 = image
        buttons[prev_row][prev_column].config(image=image_img2)
        buttons[prev_row][prev_column].image = photo_redim
        buttons[prev_row][prev_column].unbind("<Button-1>")

        # Deuxième clic, vérifier si les deux cases sont identiques
        if id_img1 == id_img2:
            score +=2
            score_label = tk.Label(root, text="Score : {}".format(score), font=custom_font, bg="skyblue", padx=3, pady=15)
            score_label.place(relx=0.002, rely=0.01)
            if score == 16:
                messagebox.showinfo("Félicitations !", "Bravo! Vous avez gagné car vous avez trouvé tous les paires jusqu'au bout. Pour vous bien avoir une bonne mémorisation, rejouer ne perd pas votre temps.")
                buttons[row][column].config(state=tk.DISABLED)
                buttons[prev_row][prev_column].config(state=tk.DISABLED)
                jouer_son()

            else:
                messagebox.showinfo("Bien joué !", "Vous avez trouvé une paire !")
                buttons[row][column].config(state=tk.DISABLED)
                buttons[prev_row][prev_column].config(state=tk.DISABLED)

        else:
            # Attendez un court instant puis masquez les cases
            root.after(500, hide_cards)
    else:
        # Premier clic, enregistrez la position de la case
        prev_row = row
        prev_column = column
# Initialisation de pygame
pygame.init()
# Chargement du fichier audio
son = pygame.mixer.Sound("C:/Users/PN/Desktop/Projet_Personnel_Python_Didier_JEU_de_MEMOIRE/son (3).wav")
def jouer_son():
    son.play()
def arreter_son():
    son.stop()
# Lancer la boucle principale Tkinter
root.mainloop()