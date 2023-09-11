from tkinter import *

# Création de la fenêtre principale
root = Tk()
root.title("Morpion")
root.geometry("400x400")

# Création d'un widget Canvas
Largeur = 300
Hauteur = 300
Canevas = Canvas(root, width = Largeur, height =Hauteur, bg ="white")

# La méthode bind() permet de lier un événement avec une fonction :
# un clic gauche sur la zone graphique provoquera l'appel de la fonction utilisateur Clic()
#Canevas.bind("<Button-1>", Clic)
#Canevas.pack(padx =5, pady =5)


#ici on créer les lignes qui délimite les colones et les cases
Canevas.create_line(0,100,300,100,fill="black",width=4)

Canevas.create_line(0,200,300,200,fill="black",width=4)

Canevas.create_line(100,300,300,-100000,fill="black",width=4)

Canevas.create_line(200,300,300,-100000,fill="black",width=4)


# Création d'un widget Button (bouton Quitter)
#Button(Mafenetre, text ="Quitter", command = Mafenetre.destroy).pack(side=LEFT,padx=5,pady=5)

root.mainloop()