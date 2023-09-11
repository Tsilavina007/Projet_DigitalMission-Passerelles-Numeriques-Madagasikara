import tkinter as tk
from tkinter import messagebox

#Création fenetre principale
fenetre = tk.Tk()
fenetre.title('Color choice morpion')
fenetre.configure(bg='black')

#Etiquette
etiquette = tk.Label(fenetre, text="Choisissez votre couleur pour le jeu", bg='black')
etiquette.config(font=("Helvetica bold", 20),fg="white")
etiquette.pack()

# Création du canvas
canvas = tk.Canvas(fenetre, width=550, height=300,bg="black")
canvas.pack()

#creation des ronds pour les choix de couleurs
Bleu = canvas.create_rectangle((50,50),(150,150), fill='blue')
Rouge = canvas.create_rectangle((160,50),(260,150), fill='red')
Vert = canvas.create_rectangle((270,50),(370,150), fill='green')
Yellow = canvas.create_rectangle((380,50),(480,150), fill='yellow')

#Création des boutons
bouton_bleu=tk.Button(fenetre,text='Click', bg='blue', font=('Arial',15))
bouton_bleu.config(fg='white')
bouton_bleu.place(x=70,y=126)

bouton_rouge=tk.Button(fenetre,text='Click', bg='red', font=('Arial',15))
bouton_rouge.config(fg='white')
bouton_rouge.place(x=180,y=126)

bouton_vert=tk.Button(fenetre,text='Click', bg='green', font=('Arial',15))
bouton_vert.config(fg='white')
bouton_vert.place(x=290,y=126)

bouton_jaune=tk.Button(fenetre,text='Click', bg='yellow', font=('Arial',15))
bouton_jaune.config(fg='white')
bouton_jaune.place(x=400,y=126)

fenetre.mainloop()