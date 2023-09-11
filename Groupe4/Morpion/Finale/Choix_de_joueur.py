import tkinter as Tk
from PIL import ImageTk, Image
import subprocess


#Création de la fenetre principale
main= Tk.Tk()
main.geometry('550x300')
main.title('Morpio-Choix des joueurs')

# Création du canvas
can=Tk.Canvas(main, width=550, height=300, bg='black')
img=Tk.PhotoImage(file="..\image\Choix_players.png")
can.create_image(525,20,image=img)
can.place(x=0, y=0)

#fonction pour bouton robot
def robot():
    print("Jeu contre le PC")
    subprocess.Popen(["python","./robot.py"])
    #main.destroy()

def two_player():
    print("Jeu un contre un")
    subprocess.Popen(["python","./human.py"])
    #main.destroy()

#Bouton pour acceder au jeux à contre PC
bouton_PC=Tk.Button(main,command=robot,text='     Contre PC', bg='black', font=('Arial',20))
bouton_PC.config(fg='white')
bouton_PC.place(x=55,y=170)

#Bouton pour acceder au jeux à deux joueurs
bouton_DeuxPlayers=Tk.Button(main,command=two_player,text='2Players        ', bg='black', font=('Arial',20))
bouton_DeuxPlayers.config(fg='white')
bouton_DeuxPlayers.place(x=360,y=170)


main.mainloop()