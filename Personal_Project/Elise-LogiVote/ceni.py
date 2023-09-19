import tkinter as tk
from tkinter import ttk
import sqlite3
from PIL import Image, ImageTk


# Créer une fenêtre principale
root = tk.Tk()
root.title("CENI")
root.geometry("1200x800")
root.iconbitmap("image\logo_docx.ico")

image_pil = Image.open("./image/photo.png")

# Déterminer la nouvelle taille de l'image (ex. double de la taille d'origine)
nouvelle_largeur = 1175
nouvelle_hauteur = 780

# Agrandir l'image avec Pillow en utilisant la méthode agrandir_image()
image_agrandie_pil = image_pil.resize((nouvelle_largeur, nouvelle_hauteur), Image.BILINEAR)


# Convertir l'image agrandie de Pillow en objet PhotoImage de Tkinter
image_agrandie_tk = ImageTk.PhotoImage(image_agrandie_pil)

# Créer un canevas pour afficher l'image en tant que fond
canvas = tk.Canvas(root, width=1200, height=800)
canvas.place(x=10,y=10)

# Placer l'image au fond du canevas
canvas.create_image(0, 0, anchor=tk.NW, image=image_agrandie_tk)

def afficher_valeur():
    # Connexion à la base de données
    conn = sqlite3.connect('Base_projet.sqlite')
    cursor = conn.cursor()
        
    # Requête SQL corrigée avec les noms de colonnes spécifiés dans SELECT
    query = "SELECT Nom,Valeur FROM DGarcon ORDER BY Valeur DESC;"
    cursor.execute(query)
    myresult_dg = cursor.fetchall()
    
    
    # Requête SQL corrigée avec les noms de colonnes spécifiés dans SELECT
    query = "SELECT Nom,Valeur FROM DFille ORDER BY Valeur DESC;"
    cursor.execute(query)
    myresult_df = cursor.fetchall()
    
    
    # Requête SQL corrigée avec les noms de colonnes spécifiés dans SELECT
    query = "SELECT Nom,Valeur FROM SGarcon ORDER BY Valeur DESC;"
    cursor.execute(query)
    myresult_sg = cursor.fetchall()
    
    
    # Requête SQL corrigée avec les noms de colonnes spécifiés dans SELECT
    query = "SELECT Nom,Valeur FROM SFille ORDER BY Valeur DESC;"
    cursor.execute(query)
    myresult_sf = cursor.fetchall()
    
    
    cursor.close()
    conn.close()
    
    remplir_tableau(myresult_dg,myresult_df,myresult_sg,myresult_sf)

def remplir_tableau(result1,result2,result3,result4):
    
    # Nettoyer le tableau existant s'il y en a déjà
    for item in tree_dg.get_children():
        tree_dg.delete(item)

    for ligne, ligne_result in enumerate(result1):
        tree_dg.insert('', 'end', values=ligne_result)
        
     
    for ligne, ligne_result in enumerate(result2):
         tree_df.insert('', 'end', values=ligne_result)   
    
    
    for ligne, ligne_result in enumerate(result3):
        tree_sg.insert('', 'end', values=ligne_result)
        
    
    for ligne, ligne_result in enumerate(result4):
        tree_sf.insert('', 'end', values=ligne_result)    
    



# Créer le tableau (Treeview) avec deux colonnes : Nom et Valeur
tree_dg = ttk.Treeview(canvas, columns=("Nom", "Valeur"), show="headings")
tree_dg.heading("Nom", text="Nom")
tree_dg.heading("Valeur", text="Valeur")
# Afficher le tableau
tree_dg.place(x=50,y=150)


# Créer le tableau (Treeview) avec deux colonnes : Nom et Valeur
tree_df = ttk.Treeview(canvas, columns=("Nom", "Valeur"), show="headings")
tree_df.heading("Nom", text="Nom")
tree_df.heading("Valeur", text="Valeur")
# Afficher le tableau
tree_df.place(x=700,y=150)


# Créer le tableau (Treeview) avec deux colonnes : Nom et Valeur
tree_sg = ttk.Treeview(canvas, columns=("Nom", "Valeur"), show="headings")
tree_sg.heading("Nom", text="Nom")
tree_sg.heading("Valeur", text="Valeur")
# Afficher le tableau
tree_sg.place(x=50,y=500)


# Créer le tableau (Treeview) avec deux colonnes : Nom et Valeur
tree_sf = ttk.Treeview(canvas, columns=("Nom", "Valeur"), show="headings")
tree_sf.heading("Nom", text="Nom")
tree_sf.heading("Valeur", text="Valeur")
# Afficher le tableau
tree_sf.place(x=700,y=500)


afficher_valeur()

#Liste des deliguers
label_dg = tk.Label(canvas, text="Deleguer garçon:")
label_dg.place(x=50,y=100)

label_df = tk.Label(canvas, text="Deleguer fille:")
label_df.place(x=700,y=100)

#Liste des suplients
label_sg = tk.Label(canvas, text="Suplient garçon:")
label_sg.place(x=50,y=450)

label_sf = tk.Label(canvas, text="Supliente fille:")
label_sf.place(x=700,y=450)



# Lancer la boucle principale de l'application
root.mainloop()