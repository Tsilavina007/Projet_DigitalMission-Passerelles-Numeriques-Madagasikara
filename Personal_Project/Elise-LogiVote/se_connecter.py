import tkinter as tk
from tkinter import *
from tkinter import messagebox
import sqlite3
import subprocess
from PIL import Image, ImageTk

fenetre = tk.Tk()

fenetre.title("se_connecter")
chemin='image/logo_docx.ico'
fenetre.iconbitmap(chemin)
fenetre.geometry("600x500")

image_pil = Image.open("image\images.png")

# Déterminer la nouvelle taille de l'image (ex. double de la taille d'origine)
nouvelle_largeur = 600
nouvelle_hauteur = 500

# Agrandir l'image avec le canvas
image_agrandie_pil = image_pil.resize((nouvelle_largeur, nouvelle_hauteur), Image.BILINEAR)
image_agrandie_tk = ImageTk.PhotoImage(image_agrandie_pil)
canvas = tk.Canvas(fenetre, width=600, height=500)
canvas.place(x=0,y=0)
canvas.create_image(0, 0, anchor=tk.NW, image=image_agrandie_tk)




def connecter():
    nom = champ_nom.get()
    mot_de_pass = champ_mot_de_passe.get()
    print(nom, mot_de_pass)
     
    if (nom == "" or mot_de_pass == ""):
        print("tsy mety")
        messagebox.showwarning(title="misy banga", message="fenoy tsara izy rehetra")
    else:
        print("mety")
        if nom=="CENI_vote" and mot_de_pass== "CENI_vote_pnm_2023":
            messagebox.showinfo("info","Connexion reussie")
            subprocess.Popen(["Python","ceni.py"])
            fenetre.destroy()
            
        else:
            # Connexion à la base de données
            conn = sqlite3.connect('Base_projet.sqlite')
            cursor = conn.cursor()
            
            # Requête SQL corrigée avec les noms de colonnes spécifiés dans SELECT
            query = "SELECT * FROM Electeurs WHERE NOM=? AND MOT_DE_PASSE=?"
            cursor.execute(query, (nom, mot_de_pass))
            myresult = cursor.fetchone()
            
            if myresult is None:
                print("Diso")
                messagebox.showwarning(title="Erreur", message="Mot de passe ou utilisateur incorrect")
            else:
                print("Tafiditry")
                messagebox.showinfo("info","Connexion reussie")
                subprocess.Popen(["Python","vote.py"])
                fenetre.destroy()

def inscrire():
    subprocess.Popen(["Python","s_inscrire.py"])
    fenetre.destroy()
        
        
        
#creer labels
label_dg = tk.Label(fenetre, text="Nom :")
label_dg.place(x=200,y=100)
label_df = tk.Label(fenetre, text="Mot de pass :")
label_df.place(x=200,y=200)
        
#creer les codres
champ_nom = Entry(fenetre, width=30)
champ_nom.place(x=200,y=130)
champ_mot_de_passe = Entry(fenetre, width=30)
champ_mot_de_passe.place(x=200,y=230)

#creer les boutons    
bouton = Button(fenetre, text="se_connecter",command=connecter)
bouton.place(x=250,y=300)
bouton_inscrire= Button(fenetre, text="s'inscrire",command=inscrire)
bouton_inscrire.place(x=260,y=330)


fenetre.mainloop()