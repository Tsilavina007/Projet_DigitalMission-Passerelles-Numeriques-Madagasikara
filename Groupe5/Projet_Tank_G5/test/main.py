import tkinter as tk
from tkinter import *
import pygame
import tkinter.messagebox
from PIL import Image, ImageTk
root = tk.Tk()
root.title('Tank')
import subprocess

# Affichage du GIF

def animate_gif(frame_number):
    global id_gif
    # Afficher l'image courante du GIF
    gif_image = gif_frames[frame_number]
    canvas.itemconfig(gif_item, image=gif_image)
    # Appeler la fonction à nouveau après un certain délai (en millisecondes)
    id_gif = root.after(delay, animate_gif, (frame_number + 1) % num_frames)

translations = {
    "Malgache": {
        "title": "Tank",  # Translation for the title
        "button": "Ilalao",  # Translation for the button
        "new_player": "Mpilalao vaovao?",  # Translation for new_player
        "language_changed": "Niova Malagasy ny fiteny"  # Translation for language changed message
    },
    "Francais": {
        "title": "Tank",  # Translation for the title
        "button": "Jouer",  # Translation for the button
        "new_player": "Nouveau joueur?",  # Translation for new_player
        "language_changed": "Langue changée en Français"  # Translation for language changed message
    },
    "Anglais": {
        "title": "Tank",  # Translation for the title
        "button": "Play",  # Translation for the button
        "new_player": "New player?",  # Translation for new_player
        "language_changed": "Language changed to English"  # Translation for language changed message
    }
}



current_language = "Malgache"  # Default language


def change_language(language):
    global current_language
    if language in translations:
        current_language = language
        update_ui()

def update_ui():
    # Update the labels and other elements with translations based on the current language
    root.title(translations[current_language]["title"])
    bouton.config(text=translations[current_language]["button"])
    nv.config(text=translations[current_language]["new_player"])


def langue_malgache():
    change_language("Malgache")
    tkinter.messagebox.showinfo("Language", translations[current_language]["language_changed"])

def langue_Francais():
    change_language("Francais")
    tkinter.messagebox.showinfo("Language", translations[current_language]["language_changed"])

def langue_Anglais():
    change_language("Anglais")
    tkinter.messagebox.showinfo("Language", translations[current_language]["language_changed"])

def about():
    # Fonction à exécuter lorsque l'option "About" est sélectionnée
    tkinter.messagebox.showinfo("About", "TankGame - Version 1.0")


def quit():
    global text
    # root.after_cancel(id_gif)
    canvas.delete(name)
    canvas['cursor'] = 'watch'
    canvas1['cursor'] = 'watch'
    nv['cursor'] = 'watch'
    root['cursor'] = 'watch'
    text = canvas.create_text(200, 50, text="Attends!", font=('Brush Script MT', 20))
    def fermer_fenetre():
        pygame.quit()
        root.destroy()
        filename = "tank.py"
        subprocess.run(["python", filename])
    def afiche():
        global text
        canvas.delete(text)
        text = canvas.create_text(200, 50, text="Compte ok!",font=('Brush Script MT', 18))
        root.after(2000, fermer_fenetre)
    root.after(5000, afiche)




frame1 = tk.Frame(root, relief=GROOVE, bg="DeepSkyBlue")   # Créer un cadre à l'intérieur de la fenêtre principale
frame1.pack(fill=BOTH, expand=True)   # Placer le cadre dans la fenêtre, en le remplissant horizontalement et verticalement
menubar = Menu(frame1)
filemenu = Menu(menubar, tearoff=0)
langue = Menu(filemenu, tearoff=0)

menubar.add_cascade(label="Fichier", menu=filemenu)
filemenu.add_cascade(label="Langue", menu=langue)
langue.add_command(label="Malgache", command=langue_malgache)
langue.add_command(label="Francais", command=langue_Francais)
langue.add_command(label="Anglais", command=langue_Anglais)

filemenu.add_command(label="About", command=about)
filemenu.add_separator()
filemenu.add_command(label="Quitter", command=root.destroy)

root.config(menu=menubar)





# Charger le GIF en utilisant la bibliothèque Pillow
gif = Image.open("rocket11.gif")

# Extraire chaque image du GIF
gif_frames = []
num_frames = gif.n_frames
for frame_number in range(num_frames):
    gif.seek(frame_number)
    gif_frames.append(ImageTk.PhotoImage(gif.copy()))

# Créer un canevas pour afficher le GIF
canvas = tk.Canvas(root, width=gif.width, height=gif.height)
canvas.pack()

# Afficher la première image du GIF
gif_item = canvas.create_image(0, 0, anchor=tk.NW, image=gif_frames[0])

# Définir le délai entre chaque image du GIF (en millisecondes)
delay = gif.info["duration"]

# Lancer l'animation du GIF en appelant la fonction animate_gif
root.after(delay, animate_gif, 1)



name = canvas.create_text(200,50, text="TankGame", font=('Brush Script MT', 40))
canvas1 = tk.Canvas(height=50, highlightthickness=0)
canvas1.pack(anchor=tk.CENTER, expand=True)

# Bouton pour jouer
bouton = tk.Button(canvas1, text='Jouer', command=quit)
bouton.grid(row=3, column=2)

nv = tk.Label(canvas1, text="Nouveau joueur?", font=("arial",9), cursor="question_arrow")
nv.grid(row = 4, column=2)

change_language("Malgache")

# Lecture de la musique
pygame.init()
pygame.mixer.music.load("song.mp3")
pygame.mixer.music.play()

# Fermeture de la fenêtre principale
root.mainloop()
