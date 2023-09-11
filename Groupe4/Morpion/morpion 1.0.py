from tkinter import * #importer les outils de tkinter

fenetre = Tk() #créer la fenêtre
fenetre.title("Morpion") #donner un titre
fenetre.geometry("320x340") #fixer le format

#couleurs utilisées
couleur_fond = '#FFFFFF'
couleur_bordure = '#000000'

#créer des boutons
boutons = []

for i in range(9):
    boutons.append(Button(fenetre, width=10, bg='#FFFFFF', bd=5, relief='raised'))
    boutons[i].grid(row=int(i/3), column=(i%3))

#définir les symboles
rond = 'O'
croix = 'X'

#définir le vainqueur
gagnant = 0

#créer la fonction pour jouer
def jouer(bouton):
    global gagnant

    #vérifier si la case est vide
    if bouton['text'] == '':
        bouton.config(text=rond, state=DISABLED, disabledforeground=couleur_bordure)
        gagnant = verification_victoire(rond)
        if not gagnant:
            ordinateur_joue()
            gagnant = verification_victoire(croix)
    if gagnant:
        game_over()

#définir la fonction pour l'ordinateur
def ordinateur_joue():
    #chercher la case vide
    choix_ordi = ''
    for i in range(9):
        if boutons[i]['text'] == '':
            choix_ordi = i
            break

    #mettre la croix dans la case vide
    boutons[choix_ordi].config(text=croix, state=DISABLED, disabledforeground=couleur_bordure)

#définir la fonction pour vérifier la victoire
def verification_victoire(symbole):
    #vérifier les lignes
    for i in range(3):
        if (boutons[3 * i]['text'] == symbole and
            boutons[3 * i + 1]['text'] == symbole and
            boutons[3 * i + 2]['text'] == symbole):
            return True

    #vérifier les colonnes
    for i in range(3):
        if (boutons[i]['text'] == symbole and
            boutons[i + 3]['text'] == symbole and
            boutons[i + 6]['text'] == symbole):
            return True

    #vérifier les diagonales
    if (boutons[0]['text'] == symbole and
        boutons[4]['text'] == symbole and
        boutons[8]['text'] == symbole) or \
       (boutons[2]['text'] == symbole and
        boutons[4]['text'] == symbole and
        boutons[6]['text'] == symbole):
        return True

#définir la fonction pour le jeu terminé
def game_over():
    for i in range(9):
        boutons[i].config(state=DISABLED)
        if gagnant == rond:
            état.config(text='Vous avez gagné !')
        elif gagnant == croix:
            état.config(text='Vous avez perdu !')
        else:
            état.config(text='Partie nulle !')

#définir la fonction pour relancer
def restart():
    global gagnant
    for i in range(9):
        boutons[i].config(text='', state=NORMAL)
    gagnant = 0
    état.config(text='C’est à votre tour !')

#créer le texte pour l'état du jeu
état = Label(fenetre, text='C’est à votre tour !', width=25, bd=1, relief='sunken', bg='#FFFFFF')
état.grid(row=4, column=0, columnspan=4)

#créer le bouton pour relancer
bouton_restart = Button(fenetre, text='Rejouer', width=5, command=restart)
bouton_restart.grid(row=4, column=3)

#attacher la fonction jouer aux boutons
for i in range(9):
    boutons[i].config(command=(lambda x=boutons[i]: jouer(x)))

fenetre.mainloop() #faire tourner la fenêtre
