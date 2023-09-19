import tkinter as tk
from tkinter import ttk
from tkinter import *
import sqlite3
from PIL import Image, ImageTk


def create_table():
    conn = sqlite3.connect('Base_projet.sqlite')
    cursor = conn.cursor()

    # Requête pour créer la table DGarcon si elle n'existe pas déjà
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS SGarcon (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Nom TEXT NOT NULL,
        Valeur INTEGER 
    )
    '''

    cursor.execute(create_table_query)
    conn.commit()
    conn.close()

def valider():
    global options1,options
    DG = combobox_dg.get()
    DF = combobox_df.get()
    SG = combobox_sg.get()
    SF = combobox_sf.get()
    conn = sqlite3.connect('Base_projet.sqlite')
    cursor = conn.cursor()
    query0 = "SELECT Valeur FROM DGarcon WHERE Nom=?"
    cursor.execute(query0, (DG,))
    myresult0 = cursor.fetchone()
    
    query1 = "SELECT Valeur FROM DFille WHERE Nom=?"
    cursor.execute(query1, (DF,))
    myresult1 = cursor.fetchone()
    
    query2= "SELECT Valeur FROM SGarcon WHERE Nom=?"
    cursor.execute(query2, (SG,))
    myresult2 = cursor.fetchone()
    
    query3 = "SELECT Valeur FROM SFille WHERE Nom=?"
    cursor.execute(query3, (SF,))
    myresult3 = cursor.fetchone()
    
    
    
    
    # Pour une requête avec un seul paramètre, il faut passer un tuple (parametre,)
       
    valeur0 = myresult0[0]
    valeur1 = myresult1[0]
    valeur2 = myresult2[0]
    valeur3 = myresult3[0]
    valeur0+=1
    valeur1+=1
    valeur2+=1
    valeur3+=1
    update_query0 = f"UPDATE DGarcon SET Valeur = ? WHERE Nom =?"
    cursor.execute(update_query0, (valeur0,DG))
    update_query1 = f"UPDATE DFille SET Valeur = ? WHERE Nom =?"
    cursor.execute(update_query1, (valeur1, DF))
    update_query2 = f"UPDATE SGarcon SET Valeur = ? WHERE Nom =?"
    cursor.execute(update_query2, (valeur2, SG))
    update_query3 = f"UPDATE SFille SET Valeur = ? WHERE Nom =?"
    cursor.execute(update_query3, (valeur3, SF))
    
    conn.commit()
    conn.close()
    root.destroy()
    


# Créer une fenêtre principale
root = tk.Tk()
root.title("Liste déroulante avec Combobox")
root.geometry("600x400")
chemin='image/logo_docx.ico'
root.iconbitmap(chemin)


image_pil = Image.open("image\Doc_vote.png")

# Déterminer la nouvelle taille de l'image (ex. double de la taille d'origine)
nouvelle_largeur = 600
nouvelle_hauteur = 400

# Agrandir l'image avec Pillow en utilisant la méthode agrandir_image()
image_agrandie_pil = image_pil.resize((nouvelle_largeur, nouvelle_hauteur), Image.BILINEAR)


# Convertir l'image agrandie de Pillow en objet PhotoImage de Tkinter
image_agrandie_tk = ImageTk.PhotoImage(image_agrandie_pil)

# Créer un canevas pour afficher l'image en tant que fond
canvas = tk.Canvas(root, width=600, height=400)
canvas.place(x=10,y=10)

# Placer l'image au fond du canevas
canvas.create_image(0, 0, anchor=tk.NW, image=image_agrandie_tk)


# Options pour la liste déroulante
options = ["Angelico","Didier","Elisé","Freddy","Jonathan","Judicaël","Kevin","Odauphin","Pierrot","Rado","Toky","Tsilavina","Tsiory"]
options1 = ["Adelaïde","Anjary","Dihariniaina","Edwine","Elivette","Fenitra","Fidelicia","Julia","Miantsa","Nekena","Pascaline","Zoeline"]

#Liste des deliguers
label_dg = tk.Label(canvas, text="Deleguer garçon :")
label_dg.place(x=50,y=60)

label_df = tk.Label(canvas, text="Deleguer fille :")
label_df.place(x=400,y=60)



#Listes des suplientes
label_sg = tk.Label(canvas, text="Suplient garçon :")
label_sg.place(x=50,y=195)

label_sf = tk.Label(canvas, text="Supliente fille :")
label_sf.place(x=400,y=195)

# Créer la liste déroulante (Combobox)
combobox_dg = ttk.Combobox(canvas, values=options)
combobox_dg.set(options[0])
combobox_dg.place(x=50,y=80)

combobox_df = ttk.Combobox(canvas, values=options1)
combobox_df.set(options1[0])
combobox_df.place(x=400,y=80)

# Créer la liste déroulante (Combobox)
combobox_sg = ttk.Combobox(canvas, values=options)
combobox_sg.set(options[0])  
combobox_sg.place(x=50,y=215)

# Créer la liste déroulante (Combobox)
combobox_sf = ttk.Combobox(canvas, values=options1)
combobox_sf.set(options1[0])
combobox_sf.place(x=400,y=215)


#creer de bouton valier
bouton_valider= tk.Button(canvas, text="Validé",command=valider)
bouton_valider.place(x=220,y=330)


# Lancer la boucle principale de l'application
root.mainloop()
