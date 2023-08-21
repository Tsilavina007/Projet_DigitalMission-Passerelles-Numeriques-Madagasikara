
import tkinter as tk
from tkinter import *
import pygame
import tkinter.messagebox
from PIL import Image, ImageTk
import tank

root = tk.Tk()
root.title('Tank')

# Affichage du GIF

def animate_gif(frame_number):
    global id_gif
    # Afficher l'image courante du GIF
    gif_image = gif_frames[frame_number]
    canvas.itemconfig(gif_item, image=gif_image)
    # Appeler la fonction à nouveau après un certain délai (en millisecondes)
    id_gif = root.after(delay, animate_gif, (frame_number + 1) % num_frames)

frame1 = tk.Frame(root, relief=GROOVE, bg="DeepSkyBlue")   # Créer un cadre à l'intérieur de la fenêtre principale
frame1.pack(fill=BOTH, expand=True)   # Placer le cadre dans la fenêtre, en le remplissant horizontalement et verticalement
menubar = Menu(frame1)
filemenu = Menu(menubar, tearoff=0)
langue = Menu(filemenu, tearoff=0)

menubar.add_cascade(label="Fichier", menu=filemenu)
filemenu.add_cascade(label="Langue", menu=langue)
langue.add_command(label="Malgache", command=animate_gif)
langue.add_command(label="Francais", command=animate_gif)

filemenu.add_command(label="About", command=animate_gif)
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

def quit():
    global text
    pygame.mixer.music.stop()
    root.after_cancel(id_gif)
    canvas.delete(ALL)
    pseudo['state'] = DISABLED
    password1['state'] = DISABLED
    canvas['cursor'] = 'watch'
    canvas1['cursor'] = 'watch'
    pseudo['cursor'] = 'watch'
    password1['cursor'] = 'watch'
    nv['cursor'] = 'watch'
    root['cursor'] = 'watch'
    text = canvas.create_text(200, 200, text="Attends!", font=('Brush Script MT', 20))
    def fermer_fenetre():
        root.destroy()
        tank.go()
    def afiche():
        global text
        canvas.delete(text)
        text = canvas.create_text(200, 200, text="Compte ok!",font=('Brush Script MT', 18))
        root.after(2000, fermer_fenetre)
    root.after(5000, afiche)

canvas.create_text(200,50, text="TankGame", font=('Brush Script MT', 40))



canvas1 = tk.Canvas(height=50, highlightthickness=0)
canvas1.pack(anchor=tk.CENTER, expand=True)

# Zone de texte
tk.Label(canvas1, text="pseudo", font=("consolas",12)).grid(row = 1, column=1)
pseudo = Entry(canvas1, width=20, font=("Arial", 12),bg="aliceblue", state=NORMAL)
pseudo.grid(row = 1, column=2)

tk.Label(canvas1, text="mots de pass", font=("consolas",12)).grid(row = 2, column=1)
password1 = Entry(canvas1, width=20, font=("Arial", 12), bg="aliceblue",state=NORMAL, show="*")
password1.grid(row = 2, column=2)



# Bouton pour jouer
bouton = tk.Button(canvas1, text='Jouer', command=quit)
bouton.grid(row=3, column=2)

nv = tk.Label(canvas1, text="Nouveau joueur?", font=("arial",9), cursor="question_arrow")
nv.grid(row = 4, column=2)


# Lecture de la musique
pygame.init()
pygame.mixer.music.load("song.mp3")
pygame.mixer.music.play()

# Fermeture de la fenêtre principale
root.mainloop()
