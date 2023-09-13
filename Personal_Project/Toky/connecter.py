import sqlite3
from subprocess import call
from tkinter import ttk, Tk, messagebox, Frame, Entry, Label, BooleanVar, Checkbutton, SUNKEN, Button
import tkinter as tk
from Inscription import Inscription
import os


def Connecter():
    username = obj.Username.get()
    password = obj.Passeword.get()

    # Connexion à la base de données
    conn = sqlite3.connect('ma_base_de_donnees.db')
    cursor = conn.cursor()

    # Vérification des informations de connexion dans la base de données
    cursor.execute("SELECT id FROM utilisateurs WHERE username=? AND password=?", (username, password))
    row = cursor.fetchone()

    if row:
        # Récupérer l'ID de l'utilisateur connecté à partir de la base de données
        Id_etr = row[0]  

        # Fermeture de la connexion à la base de données avant d'ouvrir une nouvelle connexion
        cursor.close()
        conn.close()

        # Rediriger l'utilisateur vers la page Achat_Ventes.py avec l'ID de l'utilisateur en tant qu'argument
        root.destroy()
        # Passer l'ID de l'utilisateur à Achat_Ventes.py
        call(["python Achat_Ventes.py"])  
    else:
        messagebox.showerror("Erreur de connexion", "Nom d'utilisateur ou mot de passe incorrect.")




def Inscription():
    username = obj.Username.get()
    email = obj.Mail.get()
    password = obj.Passeword.get()
    confirm_password = obj.ConfirmPasseword.get()

    if password != confirm_password:
        messagebox.showerror("Erreur d'inscription", "Les mots de passe ne correspondent pas.")
        

    # Appel de la fonction Inscription() avec les informations de l'utilisateur
    Id_etr = Inscription(username, email, password)

    root.destroy()
    os.system(f"python Inscription.py {Id_etr}")


class Formulaire:
    def __init__(self, root):
        self.root = root
        self.root.title("2Manages")
        self.root.geometry('400x400+400+200')

        canvas = tk.Canvas(root, width=50, height=20, background='red')
        canvas.pack()

        canvas.create_line(50, 300, 400, 300, width=2, fill='red')

        frame1 = Frame(root, bg='grey')
        frame1.place(x=0, y=0, width=400, height=500)

        Username = Label(root, text="Username", font=("time new rom", 15, 'bold'), bg='grey', fg='black').place(x=10, y=60)
        self.Username = Entry(root, font=('time new rom', 15), fg='black')
        self.Username.place(x=10, y=90, width=380, height=40)

        Passeword = Label(root, text="Password", font=("times new roman", 15, 'bold'), bg='grey', fg='black')
        Passeword.place(x=10, y=140)
        self.Passeword = Entry(root, font=('times new roman', 15), fg='black', show="*")
        self.Passeword.place(x=10, y=170, width=380, height=40)

        self.show_password = BooleanVar()
        show_password_checkbox = Checkbutton(root, text="", variable=self.show_password, command=self.toggle_password_visibility)
        show_password_checkbox.place(x=360, y=180)

    def toggle_password_visibility(self):
        if self.show_password.get():
            self.Passeword.config(show="")
        else:
            self.Passeword.config(show="*")


# Fenetre
root = tk.Tk()
root.resizable(False, False)
root.configure(background='white')
obj = Formulaire(root)

# Titre
label_titre = Label(root, borderwidth=3, relief=SUNKEN, text='CONNECTER ICI', font=('Arial', 25), background='white')
label_titre.place(x=0, y=0, width=400)

separator = ttk.Separator(root, orient='horizontal', style='LineSeparator.TSeparator')
separator.place(x=50, y=300, width=300)

enregistrer = Button(root, text="SE CONNECTER", font=('Time new rom', 18, 'bold'), bg="green", fg="blue", command=Connecter)
enregistrer.place(x=100, y=230, width=200)

# Bouton S'inscrire
enregistrer = Button(root, text="S'INSCRIRE", font=('Time new rom', 18, 'bold'), bg="green", fg="blue", command=Inscription)
enregistrer.place(x=100, y=320, width=200)

root.mainloop()
