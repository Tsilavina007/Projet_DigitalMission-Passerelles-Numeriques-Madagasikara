from tkinter import ttk, Tk
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import sqlite3
import os
import time
from subprocess import call

def Inscription():
    username = obj.Username.get()
    email = obj.Mail.get()
    password = obj.Passeword.get()
    confirm_password = obj.ConfirmPasseword.get()

    if password != confirm_password:
        messagebox.showerror("Erreur d'inscription", "Les mots de passe ne correspondent pas.")
        return

    cursor.execute("INSERT INTO utilisateurs (username, email, password) VALUES (?, ?, ?)", (username, email, password))
    conn.commit()

    # Récupérer l'identifiant de l'utilisateur nouvellement inscrit
    Id_etr = cursor.lastrowid

    root.destroy()
    os.system(f"python Achat_Ventes.py {Id_etr}")

    try:
        cursor.execute("INSERT INTO utilisateurs (username, email, password) VALUES (?, ?, ?)", (username, email, password))
        conn.commit()
    except sqlite3.OperationalError as e:
        print("Erreur de verrouillage, réessayer dans 1 seconde...")
        time.sleep(1)
        # Appel récursif pour réessayer l'insertion
        Inscription()

    # Rediriger l'utilisateur vers la page Achat_Ventes.py avec l'ID de l'utilisateur en tant qu'argument
    root.destroy()
    # Passer l'ID de l'utilisateur à Achat_Ventes.py
    call(["python", "Achat_Ventes.py", str(Id_etr)])
    # Retourner l'identifiant de l'utilisateur nouvellement inscrit
    return Id_etr




class Formulaire:
    def __init__(self, root):
        self.root = root
        self.root.title("GESTION ACHATS")
        self.root.geometry('400x500+400+200')

        frame1 = Frame(root, bg='grey')
        frame1.place(x=0, y=0, width=400, height=500)

        Username = Label(root, text="Username", font=("time new rom", 15, 'bold'), bg='grey', fg='black').place(x=10, y=60)
        self.Username = Entry(root, font=('time new rom', 15), fg='black')
        self.Username.place(x=10, y=90, width=380, height=40)

        Mail = Label(root, text="E-mail", font=("time new rom", 15, 'bold'), bg='grey', fg='black').place(x=10, y=140)
        self.Mail = Entry(root, font=('time new rom', 15), fg='black')
        self.Mail.place(x=10, y=170, width=380, height=40)

        Passeword = Label(root, text="Password", font=("times new roman", 15, 'bold'), bg='grey', fg='black')
        Passeword.place(x=10, y=220)
        self.Passeword = Entry(root, font=('times new roman', 15), fg='black', show="*")
        self.Passeword.place(x=10, y=250, width=380, height=40)

        ConfirmPasseword = Label(root, text="Confirm The Password", font=("times new roman", 15, 'bold'), bg='grey', fg='black')
        ConfirmPasseword.place(x=10, y=300)
        self.ConfirmPasseword = Entry(root, font=('times new roman', 15), fg='black', show="*")
        self.ConfirmPasseword.place(x=10, y=330, width=380, height=40)

        self.show_password = BooleanVar()
        show_password_checkbox = Checkbutton(root, text="", variable=self.show_password, command=self.toggle_password_visibility)
        show_password_checkbox.place(x=360, y=260)

        self.show_Confirm_password = BooleanVar()
        show_show_Confirm_password_checkbox = Checkbutton(root, text="", variable=self.show_Confirm_password, command=self.toggle_ConfirmPassword_visibility)
        show_show_Confirm_password_checkbox.place(x=360, y=340)

    def toggle_password_visibility(self):
        if self.show_password.get():
            self.Passeword.config(show="")
        else:
            self.Passeword.config(show="*")

    def toggle_ConfirmPassword_visibility(self):
        if self.show_Confirm_password.get():
            self.ConfirmPasseword.config(show="")
        else:
            self.ConfirmPasseword.config(show="*")


# Création de la connexion à la base de données
conn = sqlite3.connect('ma_base_de_donnees.db')
cursor = conn.cursor()

# Créer la table 'utilisateurs' s'il n'existe pas
cursor.execute('''CREATE TABLE IF NOT EXISTS utilisateurs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT,
                    password TEXT,
                    email TEXT
                )''')

# Vérification si la colonne "email" existe déjà dans la table
cursor.execute("PRAGMA table_info(utilisateurs)")
columns = [column[1] for column in cursor.fetchall()]
if 'email' not in columns:
    # Si la colonne "email" n'existe pas, on ajoute la colonne à la table
    cursor.execute("ALTER TABLE utilisateurs ADD COLUMN email TEXT")
    conn.commit()

# Fenêtre principale
root = tk.Tk()
root.resizable(False, False)
root.configure(background='white')
obj = Formulaire(root)

# Titre
label_titre = Label(root, borderwidth=3, relief=SUNKEN, text='INSCRIVEZ-VOUS ICI', font=('Arial', 25), background='white')
label_titre.place(x=0, y=0, width=400)

# Bouton S'inscrire
enregistrer = Button(root, text="S'INSCRIRE", font=('Time new rom', 18, 'bold'), bg="green", fg="blue", command=Inscription)
enregistrer.place(x=100, y=410, width=200)

root.mainloop()
