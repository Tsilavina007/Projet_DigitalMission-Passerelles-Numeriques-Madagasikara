import tkinter as tk
import random
from tkinter import messagebox

# Incréments pour le déplacement de la balle
dx = 15  # Déplacement horizontal de la balle (on peut ajuster cette valeur pour modifier la vitesse de la balle)
dy = 12  # Déplacement vertical de la balle (on peut ajuster cette valeur pour modifier la vitesse de la balle)

# Score du joueur A et B
scA = 0  # Score du joueur A initialisé à 0
scB = 0  # Score du joueur B initialisé à 0

# Variable pour indiquer si la raquette de la machine doit bouger
bouger_raquette_machine = False  # Initialisation à False (la raquette de la machine ne bouge pas au début)

# Variables pour stocker l'état des touches de direction du joueur
haut_pressee = False  # Indique si la touche "haut" est enfoncée
bas_pressee = False  # Indique si la touche "bas" est enfoncée

text_gm = None  # Variable pour stocker le texte affiché pour le message de fin de jeu


def debutPartie():
    global balle, mvm_ball, mvm_machine
    # Réinitialiser le score au démarrage d'une nouvelle partie
    # Dessiner la balle
    try:
        canvas.after_cancel(mvm_ball)  # Annule le mouvement de la balle s'il était en cours
    except:
        pass
    try:
        canvas.delete(balle)  # Supprime l'ancienne balle si elle existe
    except:
        pass
    balle = canvas.create_oval(largeur / 2 - 18, hauteur / 2 - 15, largeur / 2 + 15, hauteur / 2 + 15, width=2,
                               fill='white')  # Crée une nouvelle balle au centre du canvas
    canvas.after_cancel(mvm_machine)  # Annule le mouvement de la raquette de la machine s'il était en cours

    deplacerRaquetteMachine()  # Démarre le mouvement automatique de la raquette de la machine
    bougerBalle()  # Démarre le mouvement de la balle


def reset():
    global balle, mvm_ball, scA, scB, text_gm, mvm_machine
    confirmed = messagebox.askyesno("Confirmation", "Êtes-vous sûr de rejouer le jeu ?")
    if confirmed:
        try:
            canvas.delete(text_gm)  # Supprime le message de fin de jeu s'il existe
        except:
            pass
        scA = 0  # Réinitialise le score du joueur A à 0
        scB = 0  # Réinitialise le score du joueur B à 0
        textA.set(str(scA))  # Met à jour l'affichage du score du joueur A
        textB.set(str(scB))  # Met à jour l'affichage du score du joueur B

        # Réinitialiser le score au démarrage d'une nouvelle partie
        # Dessiner la balle
        try:
            canvas.after_cancel(mvm_ball)  # Annule le mouvement de la balle s'il était en cours
        except:
            pass
        try:
            canvas.delete(balle)  # Supprime l'ancienne balle si elle existe
        except:
            pass
        balle = canvas.create_oval(largeur / 2 - 18, hauteur / 2 - 15, largeur / 2 + 15, hauteur / 2 + 15, width=2,
                                   fill='white')  # Crée une nouvelle balle au centre du canvas

        canvas.after_cancel(mvm_machine)  # Annule le mouvement de la raquette de la machine s'il était en cours
        deplacerRaquetteMachine()  # Démarre le mouvement automatique de la raquette de la machine
        bougerBalle()  # Démarre le mouvement de la balle


def deplacerRaquetteMachine():
    global bouger_raquette_machine, rx2, bx2, rx1, mvm_machine

    # Vérifier si la balle se dirige vers la raquette de la machine
    bx1, by1, bx2, by2 = canvas.coords(balle)  # Récupère les coordonnées de la balle
    rx1, ry1, rx2, ry2 = canvas.coords(raquette2)  # Récupère les coordonnées de la raquette de la machine
    if bx1 > largeur / 2 and not bouger_raquette_machine:
        bouger_raquette_machine = True  # Active le mouvement de la raquette de la machine lorsque la balle dépasse le centre du terrain

    # Faire bouger la raquette de la machine automatiquement en fonction de la position de la balle
    if bouger_raquette_machine:
        if by1 < ry1 + (ry2 - ry1) / 2:
            canvas.move(raquette2, 0, -10)  # Déplace la raquette de la machine vers le haut
        elif by2 > ry1 + (ry2 - ry1) / 2:
            canvas.move(raquette2, 0, 10)  # Déplace la raquette de la machine vers le bas

        # Limiter les mouvements de la raquette pour éviter qu'elle sorte de l'écran
        if ry1 < 0:
            canvas.move(raquette2, 0, 10)  # Déplace la raquette vers le bas si elle atteint le bord supérieur
        elif ry2 > hauteur:
            canvas.move(raquette2, 0, -10)  # Déplace la raquette vers le haut si elle atteint le bord inférieur

    if scA < 8 and scB < 8:  # Continuer le mouvement de la raquette si aucun joueur n'a atteint 5 points
        mvm_machine = ecran.after(50, deplacerRaquetteMachine)  # Répète la fonction après un court délai pour le mouvement continu


# Vérifier les collisions avec les raquettes
def detecterCollisionRaquettes():
    bx1, by1, bx2, by2 = canvas.coords(balle)  # Récupère les coordonnées de la balle
    rx1, ry1, rx2, ry2 = canvas.coords(raquette1)  # Récupère les coordonnées de la raquette du joueur
    rx1_m, ry1_m, rx2_m, ry2_m = canvas.coords(raquette2)  # Récupère les coordonnées de la raquette de la machine

    if bx1 < rx2 and by1 < ry2 and by2 > ry1:  # Collision avec raquette gauche (joueur)
        return True
    elif bx2 > rx1_m and by1 < ry2_m and by2 > ry1_m:  # Collision avec raquette droite (machine)
        return True

    return False


# Vérifier les collisions avec les bords
def detecterCollisionBords():
    x1, y1, x2, y2 = canvas.coords(balle)  # Récupère les coordonnées de la balle
    if y1 <= 0 or y2 >= hauteur:
        return True  # Indique qu'il y a collision avec le bord supérieur ou inférieur

    return False  # Indique qu'il n'y a pas de collision avec le bord


def bougerBalle():
    global dx, dy, scA, scB, bouger_raquette_machine, text_gm, mvm_machine
    detecterCollisionBords()
    detecterCollisionRaquettes()
    # Déplacement de la balle
    canvas.move(balle, dx, dy)  # Déplace la balle selon les valeurs dx (déplacement horizontal) et dy (déplacement vertical)

    # Vérifier les collisions avec les bords
    if detecterCollisionBords():
        dy = -dy  # Inverse la direction de déplacement vertical de la balle (rebond)

    # Vérifier les collisions avec les raquettes
    if detecterCollisionRaquettes():
        dx = -dx  # Inverse la direction de déplacement horizontal de la balle (rebond)

    # Récupérer les coordonnées de la balle
    x1, y1, x2, y2 = canvas.coords(balle)

    # Vérifier les sorties de balle
    if x1 <= 0:  # Balle sortie à gauche (le joueur B marque un point)
        scB += 1  # Incrémente le score du joueur B
        canvas.after_cancel(mvm_machine)  # Annule le mouvement de la raquette de la machine
        textB.set(str(scB))  # Met à jour l'affichage du score du joueur B
        if scB == 7:
            text_gm = canvas.create_text(largeur / 2, hauteur / 2, text="Game Over - Joueur B gagne!", font=("Arial", 20),
                                         fill="red")  # Affiche le message de fin de jeu si le joueur B a atteint 7 points
        else:
            canvas.after_cancel(mvm_ball)  # Annule le mouvement de la balle
            canvas.coords(balle, largeur / 2 - 15, hauteur / 2 - 15, largeur / 2 + 15, hauteur / 2 + 15)  # Replace la balle au centre
            dx = 5  # Réinitialise la direction de déplacement horizontal de la balle vers la droite
            dy = random.choice([-3, 3])  # Réinitialise la direction de déplacement vertical de la balle de façon aléatoire
            bouger_raquette_machine = False  # Réinitialise le mouvement de la raquette de la machine
            return

    if x2 >= largeur:  # Balle sortie à droite (le joueur A marque un point)
        scA += 1  # Incrémente le score du joueur A
        textA.set(str(scA))  # Met à jour l'affichage du score du joueur A
        if scA == 7:
            text_gm = canvas.create_text(largeur / 2, hauteur / 2, text="Game Over - Joueur A gagne!", font=("Arial", 20),
                                         fill="white")  # Affiche le message de fin de jeu si le joueur A a atteint 7 points
        else:
            canvas.after_cancel(mvm_ball)  # Annule le mouvement de la balle
            canvas.coords(balle, largeur / 2 - 15, hauteur / 2 - 15, largeur / 2 + 15, hauteur / 2 + 15)  # Replace la balle au centre
            dx = -5  # Réinitialise la direction de déplacement horizontal de la balle vers la gauche
            dy = random.choice([-3, 3])  # Réinitialise la direction de déplacement vertical de la balle de façon aléatoire

            bouger_raquette_machine = False  # Réinitialise le mouvement de la raquette de la machine
            return

    if scA < 8 and scB < 8:  # Continuer le jeu si aucun joueur n'a atteint 5 points
        mvm_ball = ecran.after(50, bougerBalle)  # Répète la fonction après un court délai pour le mouvement continu


def haut_pressee_evt(event):
    global haut_pressee
    haut_pressee = True  # Met à True lorsque la touche "haut" est enfoncée


def haut_relache_evt(event):
    global haut_pressee
    haut_pressee = False  # Met à False lorsque la touche "haut" est relâchée


def bas_pressee_evt(event):
    global bas_pressee
    bas_pressee = True  # Met à True lorsque la touche "bas" est enfoncée


def bas_relache_evt(event):
    global bas_pressee
    bas_pressee = False  # Met à False lorsque la touche "bas" est relâchée


def deplacerRaquetteJoueur():
    global x2, x1
    # Mouvement de la raquette du joueur en fonction des touches pressées
    if haut_pressee:
        canvas.move(raquette1, 0, -20)  # Déplace la raquette du joueur vers le haut
    elif bas_pressee:
        canvas.move(raquette1, 0, 20)  # Déplace la raquette du joueur vers le bas

    # Limiter les mouvements de la raquette pour éviter qu'elle sorte de l'écran
    x1, y1, x2, y2 = canvas.coords(raquette1)  # Récupère les coordonnées de la raquette du joueur
    if y1 < 0:
        canvas.move(raquette1, 0, 10)  # Déplace la raquette vers le bas si elle atteint le bord supérieur
    elif y2 > hauteur:
        canvas.move(raquette1, 0, -10)  # Déplace la raquette vers le haut si elle atteint le bord inférieur

    # Rappeler la fonction après un court délai pour le mouvement continu
    ecran.after(50, deplacerRaquetteJoueur)


# Création de la fenêtre de l’application
ecran = tk.Tk()
ecran.title("Pong")

# Bouton pour lancer le jeu
demarrer = tk.Button(ecran, text="Démarrer", command=debutPartie, bg='silver', font=('Arial', 15))
demarrer.grid(row=0, column=0, padx=5, pady=5)
reset = tk.Button(ecran, text="Reset", command=reset, bg='silver', font=('Arial', 15))
reset.grid(row=0, column=3, padx=5, pady=5)

# Labels Score A
LabelScoreA = tk.Label(ecran, text="Score A", bg='purple', fg='white', font=('Arial', 15))
LabelScoreA.grid(row=1, column=0, padx=5, pady=5)

textA = tk.StringVar()
textA.set("0")
ScoreA = tk.Label(ecran, textvariable=textA)
ScoreA.grid(row=1, column=1, padx=5, pady=5)

# Labels Score B
LabelScoreB = tk.Label(ecran, text="Score B", bg='purple', fg='white', font=('Arial', 15))
LabelScoreB.grid(row=1, column=2, padx=5, pady=5)

textB = tk.StringVar()
textB.set("0")
ScoreB = tk.Label(ecran, textvariable=textB)
ScoreB.grid(row=1, column=3, padx=5, pady=5)

# Création du canvas pour dessiner le jeu
largeur, hauteur = 800, 400
canvas = tk.Canvas(ecran, width=largeur, height=hauteur, bg="green")
canvas.grid(row=2, column=0, columnspan=4)

# Dessiner les raquettes
raquette1 = canvas.create_rectangle(0, hauteur / 2 - 30, 15, hauteur / 2 + 30, fill="black")
raquette2 = canvas.create_rectangle(largeur - 15, hauteur / 2 - 30, largeur, hauteur / 2 + 30, fill="black")

# Dessiner la balle
balle = canvas.create_oval(largeur / 2 - 18, hauteur / 2 - 15, largeur / 2 + 15, hauteur / 2 + 15, width=2,
                           fill='white')

# Capturer les événements des touches de direction pour le joueur
ecran.bind("<Up>", haut_pressee_evt)
ecran.bind("<KeyRelease-Up>", haut_relache_evt)
ecran.bind("<Down>", bas_pressee_evt)
ecran.bind("<KeyRelease-Down>", bas_relache_evt)

# Démarrer le mouvement de la raquette de la machine
deplacerRaquetteMachine()

# Démarrer le mouvement de la raquette du joueur
deplacerRaquetteJoueur()

ecran.mainloop()
