import random
import tkinter as tk
from tkinter import messagebox

# Variables globales
EMPTY = 0
PLAYER = 1
COMPUTER = 2


# Fonctions du jeu
def initialiser_plateau():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def est_case_vide(plateau, ligne, colonne):
    return plateau[ligne][colonne] == EMPTY


def est_coup_gagnant(plateau, joueur):
    combinaisons_gagnantes = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]

    for combinaison in combinaisons_gagnantes:
        lignes, colonnes = zip(*combinaison)
        if all(plateau[l][c] == joueur for l, c in zip(lignes, colonnes)):
            return True

    return False


def est_match_nul(plateau):
    for ligne in plateau:
        if EMPTY in ligne:
            return False
    return True


def est_jeu_termine(plateau):
    if est_coup_gagnant(plateau, PLAYER):
        return True, "Vous avez gagné !"
    elif est_coup_gagnant(plateau, COMPUTER):
        return True, "L'ordinateur a gagné."
    elif est_match_nul(plateau):
        return True, "Match nul."
    else:
        return False, ""


def coup_gagnant(plateau, joueur):
    combinaisons_gagnantes = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]

    for combinaison in combinaisons_gagnantes:
        lignes, colonnes = zip(*combinaison)
        if plateau[lignes[0]][colonnes[0]] == plateau[lignes[1]][colonnes[1]] == joueur and \
                plateau[lignes[2]][colonnes[2]] == EMPTY:
            return lignes[2], colonnes[2]


def jouer_coup(plateau, ligne, colonne, joueur):
    plateau[ligne][colonne] = joueur


def coup_ordinateur(plateau):
    # 1) Vérifier si l'ordinateur peut gagner en jouant un coup gagnant
    for ligne in range(3):
        for colonne in range(3):
            if est_case_vide(plateau, ligne, colonne):
                plateau[ligne][colonne] = COMPUTER
                if est_coup_gagnant(plateau, COMPUTER):
                    return ligne, colonne
                else:
                    plateau[ligne][colonne] = EMPTY

    # 2) Vérifier si l'adversaire a un coup gagnant et l'empêcher
    for ligne in range(3):
        for colonne in range(3):
            if est_case_vide(plateau, ligne, colonne):
                plateau[ligne][colonne] = PLAYER
                if est_coup_gagnant(plateau, PLAYER):
                    return ligne, colonne
                else:
                    plateau[ligne][colonne] = EMPTY

    # 3) Jouer au centre s'il est vide
    if est_case_vide(plateau, 1, 1):
        return 1, 1

    # 4) Jouer dans un coin s'il est vide
    coins = [(0, 0), (0, 2), (2, 0), (2, 2)]
    random.shuffle(coins)
    for ligne, colonne in coins:
        if est_case_vide(plateau, ligne, colonne):
            return ligne, colonne

    # 5) Jouer n'importe où dans les places restantes
    for ligne in range(3):
        for colonne in range(3):
            if est_case_vide(plateau, ligne, colonne):
                return ligne, colonne


def jouer(ligne, colonne):
    if est_case_vide(plateau, ligne, colonne):
        jouer_coup(plateau, ligne, colonne, PLAYER)
        case_jouee(ligne, colonne)

        fin_jeu, resultat = est_jeu_termine(plateau)
        if fin_jeu:
            messagebox.showinfo("Fin du jeu", resultat)
            reinitialiser_jeu()
        else:
            ligne, colonne = coup_ordinateur(plateau)
            jouer_coup(plateau, ligne, colonne, COMPUTER)
            case_jouee(ligne, colonne)

            fin_jeu, resultat = est_jeu_termine(plateau)
            if fin_jeu:
                messagebox.showinfo("Fin du jeu", resultat)
                reinitialiser_jeu()


def case_jouee(ligne, colonne):
    if plateau[ligne][colonne] == PLAYER:
        canvas.itemconfigure(grilles[ligne][colonne], fill="green")
    elif plateau[ligne][colonne] == COMPUTER:
        canvas.itemconfigure(grilles[ligne][colonne], fill="red")


def reinitialiser_jeu():
    global plateau
    plateau = initialiser_plateau()
    canvas.delete("all")
    dessiner_grille()


def dessiner_grille():
    for ligne in range(3):
        for colonne in range(3):
            x1 = colonne * 100
            y1 = ligne * 100
            x2 = x1 + 100
            y2 = y1 + 100
            grilles[ligne][colonne] = canvas.create_rectangle(x1, y1, x2, y2, outline="black")

# Interface graphique
def dessiner_grille():
    for ligne in range(3):
        for colonne in range(3):
            x1 = colonne * 100
            y1 = ligne * 100
            x2 = x1 + 100
            y2 = y1 + 100
            grilles[ligne][colonne] = canvas.create_rectangle(x1, y1, x2, y2, outline="black")

def clic_case(event):
    colonne = event.x // 100
    ligne = event.y // 100
    jouer(ligne, colonne)

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Morpion")

# Création du canvas
canvas = tk.Canvas(fenetre, width=300, height=300)
canvas.pack()

# Initialisation du plateau
plateau = initialiser_plateau()

# Initialisation des grilles
grilles = [[None, None, None],
           [None, None, None],
           [None, None, None]]

# Dessin de la grille
dessiner_grille()

# Gestion des clics
canvas.bind("<Button-1>", clic_case)

# Lancement de la fenêtre principale
fenetre.mainloop()

