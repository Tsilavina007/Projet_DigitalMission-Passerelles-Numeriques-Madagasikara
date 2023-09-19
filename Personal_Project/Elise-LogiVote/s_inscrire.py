import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3
import subprocess

def inscrire():
    nom = champ_nom.get()
    mot_de_passe = champ_mot_de_passe.get()
    print(nom, mot_de_passe)
    if (nom == "" or mot_de_passe == ""):
        print("tsy mety")
        messagebox.showwarning(title="misy banga", message="fenoy tsara izy rehetra")
    else:
        print("mety")
        
        # Connexion à la base de données
        conn = sqlite3.connect('Base_projet.sqlite')
        cursor = conn.cursor()
        # Requête d'insertion à la base de données
        query = "INSERT INTO Electeurs(NOM, MOT_DE_PASSE) VALUES (?, ?)"
        cursor.execute(query, (nom, mot_de_passe))
        conn.commit()
        conn.close()
        print("lasa")
        messagebox.showinfo("info", "Utilisateur ajouté")

def connecter():
    subprocess.Popen(["Python", "se_connecter.py"])
    fenetre.destroy()


fenetre = tk.Tk()
fenetre.title("s'inscrire")
fenetre.geometry("600x400")

#insertion d'image au fond
chemin = 'image/logo.ico'
fenetre.iconbitmap(chemin)
image_pil = Image.open("image\photo.png")
nouvelle_largeur = 600
nouvelle_hauteur = 500
image_agrandie_pil = image_pil.resize((nouvelle_largeur, nouvelle_hauteur), Image.BICUBIC)
image_agrandie_tk = ImageTk.PhotoImage(image_agrandie_pil)

position_x = (nouvelle_largeur - image_agrandie_pil.width) // 2
position_y = (nouvelle_hauteur - image_agrandie_pil.height) // 2
    
canvas = tk.Canvas(fenetre, width=nouvelle_largeur, height=nouvelle_hauteur)
canvas.place(x=0, y=0)
canvas.create_image(0, 0, anchor=tk.NW, image=image_agrandie_tk)
canvas.create_image(position_x, position_y, anchor=tk.NW, image=image_agrandie_tk)

#creer labes
label_dg = tk.Label(canvas, text="Entrer nom :")
label_dg.place(x=200,y=20)
label_df = tk.Label(canvas, text="Entrer mot de passe :")
label_df.place(x=200,y=100)

#creer cadres
champ_nom = tk.Entry(canvas, width=30)
champ_nom.place(x=200, y=50)
champ_mot_de_passe = tk.Entry(canvas, width=30)
champ_mot_de_passe.place(x=200, y=130)

#creer bouton commande
bouton = tk.Button(canvas, text="s'inscrire", command=inscrire)
bouton.place(x=260, y=260)
bouton_connecter = tk.Button(canvas, text="Se connecter", command=connecter)
bouton_connecter.place(x=250, y=300)
    


fenetre.mainloop()

