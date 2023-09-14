import tkinter as tk  # Importe le module tkinter et le renomme en tk
from tkinter import messagebox  # Importe la classe messagebox du module tkinter
import random  # Importe le module random

def afficher_lignes():
    label_image.destroy()  # Supprime le widget d'affichage de l'image

def click(row, col):
    global player_turn, game_over  # Déclare les variables player_turn et game_over comme globales

    if buttons[row][col]["text"] == "" and not game_over:  # Vérifie si le bouton est vide et que le jeu n'est pas terminé
        if player_turn:  # Si c'est le tour du joueur
            buttons[row][col]["text"] = "O"  # Met le texte du bouton à "O"
        else:
            buttons[row][col]["text"] = "X"  # Sinon, met le texte du bouton à "X"
        check_game_status()  # Vérifie l'état du jeu
        player_turn = not player_turn  # Change le tour du joueur
        if against_computer:  # Si le joueur joue contre l'ordinateur
            computer_move()  # Effectue le mouvement de l'ordinateur

def check_game_status():
    global game_over  # Déclare la variable game_over comme globale

    if check_win("O"):  # Si le joueur 1 a gagné
        highlight_winning_combination("O")  # Met en évidence la combinaison gagnante
        messagebox.showinfo("Tic Tac Toe", "Le joueur 1 a gagné!")  # Affiche une boîte de dialogue avec le message "Le joueur 1 a gagné!"
        game_over = True  # Le jeu est terminé
    elif check_win("X"):  # Sinon, si le joueur 2 a gagné
        highlight_winning_combination("X")  # Met en évidence la combinaison gagnante
        messagebox.showinfo("Tic Tac Toe", "Le joueur 2 a gagné!")  # Affiche une boîte de dialogue avec le message "Le joueur 2 a gagné!"
        game_over = True  # Le jeu est terminé
    elif check_tie():  # Sinon, si c'est un match nul
        messagebox.showinfo("Tic Tac Toe", "Match nul!")  # Affiche une boîte de dialogue avec le message "Match nul!"
        game_over = True  # Le jeu est terminé
        
        
def highlight_winning_combination(player):
    for i in range(3):  # Parcourt les lignes du tableau
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] == player:  # Vérifie si les boutons dans une ligne sont tous du même joueur
            buttons[i][0].config(bg="chartreuse")  # Change la couleur de fond du premier bouton de la ligne en rouge
            buttons[i][1].config(bg="chartreuse")  # Change la couleur de fond du deuxième bouton de la ligne en rouge
            buttons[i][2].config(bg="chartreuse")  # Change la couleur de fond du troisième bouton de la ligne en rouge
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] == player:  # Vérifie si les boutons dans une colonne sont tous du même joueur
            buttons[0][i].config(bg="chartreuse")  # Change la couleur de fond du premier bouton de la colonne en rouge
            buttons[1][i].config(bg="chartreuse")  # Change la couleur de fond du deuxième bouton de la colonne en rouge
            buttons[2][i].config(bg="chartreuse")  # Change la couleur de fond du troisième bouton de la colonne en rouge
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] == player:  # Vérifie si les boutons sur la diagonale principale sont tous du même joueur
        buttons[0][0].config(bg="chartreuse")  # Change la couleur de fond du premier bouton de la diagonale principale en rouge
        buttons[1][1].config(bg="chartreuse")  # Change la couleur de fond du deuxième bouton de la diagonale principale en rouge
        buttons[2][2].config(bg="chartreuse")  # Change la couleur de fond du troisième bouton de la diagonale principale en rouge
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] == player:  # Vérifie si les boutons sur la diagonale inverse sont tous du même joueur
        buttons[0][2].config(bg="chartreuse")  # Change la couleur de fond du premier bouton de la diagonale inverse en rouge
        buttons[1][1].config(bg="chartreuse")  # Change la couleur de fond du deuxième bouton de la diagonale inverse en rouge
        buttons[2][0].config(bg="chartreuse")  # Change la couleur de fond du troisième bouton de la diagonale inverse en rouge

def check_win(player):
    for i in range(3):  # Parcourt les lignes du tableau
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] == player:  # Vérifie si les boutons dans une ligne sont tous du même joueur
            return True
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] == player:  # Vérifie si les boutons dans une colonne sont tous du même joueur
            return True
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] == player:  # Vérifie si les boutons sur la diagonale principale sont tous du même joueur
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] == player:  # Vérifie si les boutons sur la diagonale inverse sont tous du même joueur
        return True
    return False

def check_tie():
    for i in range(3):  # Parcourt les lignes du tableau
        for j in range(3):  # Parcourt les colonnes du tableau
            if buttons[i][j]["text"] == "":  # Vérifie s'il y a un bouton vide
                return False  # Il n'y a pas de match nul
    return True  # Tous les boutons sont remplis, c'est un match nul


def computer_move():
    global player_turn, game_over  # Déclare les variables player_turn et game_over comme globales

    # Vérifie si l'ordinateur peut gagner
    for i in range(3):  # Parcourt les lignes du tableau
        for j in range(3):  # Parcourt les colonnes du tableau
            if buttons[i][j]["text"] == "":  # Vérifie s'il y a un bouton vide
                buttons[i][j]["text"] = "X"  # Remplit le bouton avec "X"
                if check_win("X"):  # Vérifie si l'ordinateur a gagné
                    highlight_winning_combination("X")  # Met en évidence la combinaison gagnante
                    messagebox.showinfo("Tic Tac Toe", "Le PC a gagné!")  # Affiche une boîte de dialogue avec le message "Le PC a gagné!"
                    game_over = True  # Le jeu est terminé
                buttons[i][j]["text"] = ""  # Réinitialise le bouton

    if not game_over:
        # Vérifie si le joueur peut gagner et bloque
        for i in range(3):  # Parcourt les lignes du tableau
            for j in range(3):  # Parcourt les colonnes du tableau
                if buttons[i][j]["text"] == "":  # Vérifie s'il y a un bouton vide
                    buttons[i][j]["text"] = "O"  # Remplit le bouton avec "O"
                    if check_win("O"):  # Vérifie si le joueur a gagné
                        buttons[i][j]["text"] = "X"  # Remplit le bouton avec "X" pour bloquer le joueur
                        player_turn = True  # C'est à nouveau le tour du joueur
                        return
                    buttons[i][j]["text"] = ""  # Réinitialise le bouton

        # Joue au centre
        if buttons[1][1]["text"] == "":  # Vérifie si le bouton du centre est vide
            buttons[1][1]["text"] = "X"  # Remplit le bouton du centre avec "X"
            player_turn = True  # C'est à nouveau le tour du joueur
            return

        # Joue dans les coins
        corners = [(0, 0), (0, 2), (2, 0), (2, 2)]  # Liste des positions des coins
        random.shuffle(corners)  # Mélange les positions des coins de manière aléatoire
        for corner in corners:  # Parcourt les positions des coins
            if buttons[corner[0]][corner[1]]["text"] == "":  # Vérifie si le coin est vide
                buttons[corner[0]][corner[1]]["text"] = "X"  # Remplit le coin avec "X"
                player_turn = True  # C'est à nouveau le tour du joueur
                return

        # Joue dans les positions restantes
        for i in range(3):  # Parcourt les lignes du tableau
            for j in range(3):  # Parcourt les colonnes du tableau
                if buttons[i][j]["text"] == "":  # Vérifie s'il y a un bouton vide
                    buttons[i][j]["text"] = "X"  # Remplit le bouton avec "X"
                    player_turn = True  # C'est à nouveau le tour du joueur
                    return


def reset():
    global game_over, player_turn  # Déclare les variables game_over et player_turn comme globales

    game_over = False  # Réinitialise la variable game_over à False
    player_turn = True  # Réinitialise la variable player_turn à True

    for i in range(3):  # Parcourt les lignes du tableau
        for j in range(3):  # Parcourt les colonnes du tableau
            buttons[i][j].config(text="", bg="SystemButtonFace")  # Réinitialise le texte et la couleur de fond des boutons

def quitter():
    quitter = messagebox.askyesno("Morpion games", "Do you want to exit?")  # Affiche une boîte de dialogue de confirmation pour quitter
    if quitter > 0:  # Si l'utilisateur choisit "Oui"
        fenetre.destroy()  # Ferme la fenêtre principale
        return

def jouer_contre_ordi():
    global against_computer  # Déclare la variable against_computer comme globale
    against_computer = True  # Définit against_computer à True
    reset()  # Réinitialise le jeu

def jouer_contre_joueur():
    global against_computer  # Déclare la variable against_computer comme globale
    against_computer = False  # Définit against_computer à False
    reset()  # Réinitialise le jeu

fenetre = tk.Tk()  # Crée une fenêtre principale
fenetre.title("Tic Tac Toe")  # Définit le titre de la fenêtre

# Chargement de l'image
image = tk.PhotoImage(file='test1.ppm')  # Charge une image à partir d'un fichier
largeur_image = image.width()  # Récupère la largeur de l'image
hauteur_image = image.height()  # Récupère la hauteur de l'image

# Définir la taille de la fenêtre pour correspondre à l'image
fenetre.geometry(f"{largeur_image}x{hauteur_image}")

# Création d'un label pour afficher l'image
label_image = tk.Label(fenetre, image=image)
label_image.grid(row=0, column=0, columnspan=3)

# Planifie la destruction de l'image et l'affichage des lignes après 5 secondes
fenetre.after(5000, afficher_lignes)

# Modif
game_over = False  # Variable pour indiquer si le jeu est terminé
player_turn = True  # Variable pour indiquer le tour du joueur
against_computer = False  # Variable pour indiquer si le joueur joue contre l'ordinateur

# Création d'un cadre pour le plateau de jeu
plateau_frame = tk.Frame(fenetre, bg="blue")
plateau_frame.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

# Ajout des lignes à gauche
buttons = []
for i in range(3):  # Parcourt les lignes du tableau
    row = []
    for j in range(3):  # Parcourt les colonnes du tableau
        button = tk.Button(plateau_frame, text="", font=("Helvetica", 20), height=2, width=7, border=2,
                           command=lambda row=i, col=j: click(row, col))  # Crée un bouton avec une fonction de rappel pour le clic
        button.grid(row=i, column=j+3, padx=2, pady=2)  # Place le bouton dans le cadre
        row.append(button)  # Ajoute le bouton à la liste de lignes
    buttons.append(row)  # Ajoute la liste de lignes à la liste de boutons

my_menu = tk.Menu(fenetre)  # Crée un menu
fenetre.config(menu=my_menu)  # Configure le menu pour la fenêtre principale
fenetre.resizable (width = False , height = False)

options_menu = tk.Menu(my_menu, tearoff=False)  # Crée un sous-menu pour les options
my_menu.add_cascade(label="Options", menu=options_menu)  # Ajoute le sous-menu au menu principal
options_menu.add_command(label="Rejouer", command=reset)  # Ajoute une commande au sous-menu pour réinitialiser le jeu
options_menu.add_command(label="Quitter", command=quitter)  # Ajoute une commande au sous-menu pour quitter le jeu

# Ajout d'un sous-menu pour choisir le mode de jeu
mode_menu = tk.Menu(options_menu, tearoff=False)  # Crée un sous-menu pour le mode de jeu
options_menu.add_cascade(label="Mode de jeu", menu=mode_menu)  # Ajoute le sous-menu au sous-menu des options
mode_menu.add_command(label="Jouer contre un autre joueur", command=jouer_contre_joueur)  # Ajoute une commande au sous-menu pour jouer contre un autre joueur
mode_menu.add_command(label="Jouer contre l'ordinateur", command=jouer_contre_ordi)  # Ajoute une commande au sous-menu pour jouer contre l'ordinateur

reset()  # Réinitialise le jeu

fenetre.mainloop()  # Lance la boucle principale de la fenêtre



