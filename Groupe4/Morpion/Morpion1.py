import tkinter as tk
from tkinter import messagebox

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Jeu du Morpion")

# Couleurs
COULEUR_FOND = "#FFFFFF"  # Blanc
COULEUR_GRILLE = "#000000"  # Noir
COULEUR_X = "red"  # Rouge
COULEUR_O = "blue"  # Bleu

# Symboles des joueurs
SYMBOLES = {1: "X", 2: "O"}
Couleur = {1:COULEUR_X, 2:COULEUR_O} # Pour les deux couleurs

# Grille de jeu
grille = [[None, None, None],
          [None, None, None],
          [None, None, None]]

# Joueur courant
joueur_courant = 1

# Fonction appelée lorsqu'un bouton de la grille est cliqué
def case_clique(ligne, colonne):
    global joueur_courant

    if grille[ligne][colonne] is None:
        grille[ligne][colonne] = SYMBOLES[joueur_courant]
        boutons[ligne][colonne].config(text=SYMBOLES[joueur_courant], state=tk.DISABLED)
        if verifier_victoire():
            messagebox.showinfo("Fin de partie", "Le joueur " + SYMBOLES[joueur_courant] + " a gagné !")
            fenetre.quit()
        elif not any(None in row for row in grille):
            messagebox.showinfo("Fin de partie", "Match nul !")
            fenetre.quit()
        else:
            joueur_courant = 3 - joueur_courant
            etat_joueur.config(text="Joueur " + SYMBOLES[joueur_courant])

# Fonction pour vérifier s'il y a un gagnant
def verifier_victoire():
    # Vérification des lignes
    for ligne in grille:
        if ligne[0] == ligne[1] == ligne[2] != None:
            return True
    # Vérification des colonnes
    for colonne in range(3):
        if grille[0][colonne] == grille[1][colonne] == grille[2][colonne] != None:
            return True
    # Vérification des diagonales
    if grille[0][0] == grille[1][1] == grille[2][2] != None:
        return True
    if grille[0][2] == grille[1][1] == grille[2][0] != None:
        return True
    # Aucun gagnant
    return False

# Création des boutons de la grille
boutons = []
for i in range(3):
    ligne_boutons = []
    for j in range(3):
        bouton = tk.Button(fenetre, text="", font=("Arial", 70), width=8, height=4,
                          command=lambda i=i, j=j: case_clique(i, j))
        bouton.grid(row=i, column=j, padx=10, pady=10)
        ligne_boutons.append(bouton)
    boutons.append(ligne_boutons)

# État du joueur courant
etat_joueur = tk.Label(fenetre, text="Joueur " + SYMBOLES[joueur_courant], font=("Arial", 16))
etat_joueur.grid(row=3, column=0, columnspan=3)

# Paramètres de la grille
for i in range(3):
    fenetre.grid_rowconfigure(i, weight=1)
    fenetre.grid_columnconfigure(i, weight=1)

# Affichage de la fenêtre principale
fenetre.mainloop()
