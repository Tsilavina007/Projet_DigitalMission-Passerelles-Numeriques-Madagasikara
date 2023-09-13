from tkinter import Tk, Button, Canvas
from PIL import ImageTk, Image
import pygame


# Fonction pour fermer la fenêtre actuelle et importer le fichier "deplacement.py"
def pass_deplacement():
    first.destroy()  
    import deplacement  
    
# Fonction pour quitter l'application
def quit_application():
    first.destroy()

# Création de la fenêtre principale
first = Tk()
first.geometry('1500x1000')
first.title('Puzzle')

# Création de l'icône et le titre de l'application 
icon_path = r"C:\Users\MIANTSA\Desktop\Python_puzzle_Miantsa\logo.ico"
first.iconbitmap(icon_path)

# Chemin d'accès à l'image
image_path = r"C:\Users\MIANTSA\Desktop\Python_puzzle_Miantsa\fifteen.png"
image_path2 = r"C:\Users\MIANTSA\Desktop\Python_puzzle_Miantsa\Start.png"
image_path3 = r"C:\Users\MIANTSA\Desktop\Python_puzzle_Miantsa\Quitter.png"

# Charger l'image personnalisée
image2 = ImageTk.PhotoImage(file=image_path2)
image3 = ImageTk.PhotoImage(file=image_path3)

# Crée un Canvas pour afficher l'image de fond
canvas = Canvas(first, width=1500, height=1000)  
canvas.pack()

# Ouvrir l'image avec PIL
image = Image.open(image_path)
image = image.resize((1500, 1000), Image.LANCZOS) 
background_image = ImageTk.PhotoImage(image)

# Affiche l'image de fond sur le Canvas
canvas.create_image(0, 0, anchor='nw', image=background_image)  

#Création et position du bouton "PLAY"
button_play = Button(first,image=image2, command=pass_deplacement,bd=4, highlightthickness=5, highlightbackground="black")
button_play.place(x=400, y=300)

#Création et position du bouton "Quit"
button_quit = Button(first,image=image3, command=quit_application,bd=4, highlightthickness=5, highlightbackground="black")
button_quit.place(x=700, y=300)  

first.mainloop()
