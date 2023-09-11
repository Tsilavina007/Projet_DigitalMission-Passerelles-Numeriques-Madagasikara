import tkinter as Tk
from PIL import ImageTk, Image

def choisir_pc():
    # Code pour accéder au fichier python correspondant au jeu contre PC
    pass

def choisir_deux_joueurs():
    # Code pour accéder au fichier python correspondant au jeu à deux joueurs
    pass

# Création de la fenetre principale
fenetre = Tk.Tk()
fenetre.geometry('550x300')
fenetre.title('Morpio-Choix des joueurs')

# Création du canvas
can = Tk.Canvas(fenetre, width=550, height=300, bg='black')
img = ImageTk.PhotoImage(Image.open("Choix_players.png"))
can.create_image(525, 20, image=img)
can.place(x=0, y=0)

# Bouton pour accéder au jeu contre PC
bouton_PC = Tk.Button(fenetre, text='Contre PC', bg='black', font=('Arial', 20), fg='white', command=choisir_pc)
bouton_PC.place(x=55, y=170)

# Bouton pour accéder au jeu à deux joueurs
bouton_DeuxPlayers = Tk.Button(fenetre, text='2 Joueurs', bg='black', font=('Arial', 20), fg='white', command=choisir_deux_joueurs)
bouton_DeuxPlayers.place(x=360, y=170)

fenetre.mainloop()
