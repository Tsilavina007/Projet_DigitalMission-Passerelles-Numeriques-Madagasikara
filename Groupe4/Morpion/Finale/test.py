import tkinter as Tk
from PIL import ImageTk, Image
import subprocess


#Création de la fenetre principale
main= Tk.Tk()
main.geometry('550x300')
main.title('Morpio-Choix des joueurs')

can=Tk.Canvas(main, width=550, height=300, bg='black')
img=Tk.PhotoImage(file="..\image\Choix_players.png")
can.create_image(525,20,image=img)
can.place(x=0, y=0)

bouton_PC=Tk.Button(main,text='     Contre PC', bg='black', font=('Arial',20)).pack()

main.mainloop()