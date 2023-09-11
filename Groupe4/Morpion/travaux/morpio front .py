import tkinter as Tk
from tkinter import messagebox

#Création de la fenetre principale
fenetre= Tk.Tk()
fenetre.title("Morpion")

#Création du canvas
canvas=Tk.Canvas(fenetre, width= 500, height=500,bg='black')

#Création du score gauche
score1= canvas.create_oval((50,20),(70,40), fill='white')
score2= canvas.create_oval((80,20),(100,40), fill='white')
score3= canvas.create_oval((110,20),(130,40), fill='white')

# Create a Frame for border
#border_color = Tk.Frame(fenetre, background="red")

#Title
#E_date = Tk.Label(border_color,text="E-Date Morpion", bg='white')

#Création du score droit
score4= canvas.create_oval((350,20),(370,40), fill='white')
score5= canvas.create_oval((380,20),(400,40), fill='white')
score6= canvas.create_oval((410,20),(430,40), fill='white')


fenetre.mainloop()