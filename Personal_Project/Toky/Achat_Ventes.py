from tkinter import *
from tkinter import messagebox
from tkcalendar import *
from tkinter import ttk
import sqlite3
from subprocess import call
import sys


class Formulaire:
    def __init__(self, root):
        self.root = root
        #self.Id_etr = Id_etr
        self.root.title("Manages")
        self.root.geometry('1000x600')

        # Changer le fond de la fenêtre
        self.root.configure(background='lightgrey')

        # Label titre
        label_titre = Label(root, borderwidth=3, relief=SUNKEN, text='GERER VOS ACHATS OU VENTES', font=('Arial', 25), background='blue', foreground='white')
        label_titre.place(x=200, y=0, width=550, height=100)

        # Champs de saisie pour Produit
        label_date = Label(root, text='Date:', font=('Arial', 12), background='lightgrey')
        label_date.place(x=50, y=150)
        self.date_entry = DateEntry(root, font=('Arial', 12))
        self.date_entry.place(x=200, y=150, width=200)

        label_produit = Label(root, text='Nom du Produit:', font=('Arial', 12), background='lightgrey')
        label_produit.place(x=50, y=200)
        self.nom_produit_entry = Entry(root, font=('Arial', 12))
        self.nom_produit_entry.place(x=200, y=200, width=200)

        label_prix_unitaire = Label(root, text='Prix Unitaires:', font=('Arial', 12), background='lightgrey')
        label_prix_unitaire.place(x=50, y=250)
        self.prix_unitaire_entry = Entry(root, font=('Arial', 12))
        self.prix_unitaire_entry.place(x=200, y=250, width=200)

        # Formulaire Achats/Ventes

        label_type = Label(root, text='Type:', font=('Arial', 12), background='lightgrey')
        label_type.place(x=50, y=300)
        self.type_combobox = ttk.Combobox(root, values=['Achat', 'Vente'], font=('Arial', 12))
        self.type_combobox.place(x=200, y=300, width=200)

        label_quantite = Label(root, text='Quantité:', font=('Arial', 12), background='lightgrey')
        label_quantite.place(x=50, y=350)
        self.quantite_entry = Entry(root, font=('Arial', 12))
        self.quantite_entry.place(x=200, y=350, width=200)

        # Champ de saisie pour Fournisseurs
        label_fournisseur = Label(root, text='Nom du Fournisseur:', font=('Arial', 12), background='lightgrey')
        label_fournisseur.place(x=50, y=400)
        self.nom_fournisseur_entry = Entry(root, font=('Arial', 12))
        self.nom_fournisseur_entry.place(x=200, y=400, width=200)

        # Bouton Enregistrer
        enregistrer = Button(root, text="ENREGISTRER", font=('Arial', 12), bg="green", fg="white", command=self.enregistrer)
        enregistrer.place(x=230, y=500, width=200)

        # Bouton Effacer
        effacer = Button(root, text="EFFACER", font=('Arial', 12), bg="orange", fg="white", command=self.effacer_formulaire)
        effacer.place(x=450, y=500, width=200)

        # Titre de l'écran d'affichage
        label_facture = Label(root, text='Recapitulation', font=('Arial', 16, 'bold'), background='lightgrey')
        label_facture.place(x=600, y=120)

        # Affichage des informations saisies sous forme de tableau
        self.treeview = ttk.Treeview(root, columns=('Date', 'Produit', 'Prix Unitaires', 'Type', 'Quantité', 'Fournisseur'), show='headings', height=15)
        self.treeview.place(x=462, y=150, height=300)

        self.treeview.heading('Date', text='Date', anchor='center')
        self.treeview.heading('Produit', text='Produit', anchor='center')
        self.treeview.heading('Prix Unitaires', text='PU', anchor='center')
        self.treeview.heading('Type', text='Type', anchor='center')
        self.treeview.heading('Quantité', text='Qté', anchor='center')
        self.treeview.heading('Fournisseur', text='Fournisseur', anchor='center')

        # Redimensionner les colonnes du tableau
        self.treeview.column('Date', width=50, anchor='center')
        self.treeview.column('Produit', width=100, anchor='center')
        self.treeview.column('Prix Unitaires', width=70, anchor='center')
        self.treeview.column('Type', width=50, anchor='center')
        self.treeview.column('Quantité', width=50, anchor='center')
        self.treeview.column('Fournisseur', width=150, anchor='center')

        # Configure la scrollbar pour le tableau
        scrollbar = Scrollbar(root, orient=VERTICAL, command=self.treeview.yview)
        scrollbar.place(x=450, y=150, height=300)
        self.treeview.configure(yscrollcommand=scrollbar.set)

        # Label pour afficher le total en bas à droite du tableau
        self.total_label = Label(root, text='Total:', font=('Arial', 12), background='lightgrey')
        self.total_label.place(x=800, y=460, anchor='e')  # 'e' pour aligner à droite

        # Boutton Retour
        retour = Button(root, text="RETOUR", font=('Arial', 12), bg="red", fg="white", command=self.Retour)
        retour.place(x=10, y=500, width=200)

         # Fonction pour gérer la sélection d'un élément dans le tableau
        self.treeview.bind("<ButtonRelease-1>", self.selectionner_element)

        # Variable pour stocker l'élément sélectionné dans le tableau
        self.element_selectionne = None

        # Connexion à la base de données
        self.conn = sqlite3.connect('ma_base_de_donnees.db')
        self.c = self.conn.cursor()

        # Créer la table 'Achats' pour cet utilisateur s'il n'existe pas
        self.c.execute('''CREATE TABLE IF NOT EXISTS Achats (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            
                            date TEXT,
                            nom_produit TEXT,
                            prix_unitaire REAL,
                            quantite INTEGER,
                            nom_fournisseur TEXT
                        )''')

        # Créer la table 'Vente' pour cet utilisateur s'il n'existe pas
        self.c.execute('''CREATE TABLE IF NOT EXISTS Vente (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            
                            date TEXT,
                            nom_produit TEXT,
                            prix_unitaire REAL,
                            quantite INTEGER,
                            nom_fournisseur TEXT
                        )''')

        # Sauvegarder les modifications
        self.conn.commit()

        # Load and display user's data from the database when the form is initialized
        self.load_user_data()

    def load_user_data(self):
        # Load data from 'Achats' table for the current user
        #self.c.execute('''SELECT * FROM Achats WHERE Id_etr=?''', (self.Id_etr,))
        #achats_data = self.c.fetchall()

        # Load data from 'Vente' table for the current user
        #self.c.execute('''SELECT * FROM Vente WHERE Id_etr=?''', (self.Id_etr,))
        #vente_data = self.c.fetchall()

        # Combine data from both tables and sort by date in descending order
        #combined_data = sorted(achats_data + vente_data, key=lambda x: x[2], reverse=True)

        # Update the Treeview to display the user's data
        #self.treeview.delete(*self.treeview.get_children())
        #for record in combined_data:
         #   self.treeview.insert('', 'end', values=record[2:])  # Exclude the 'id' and 'user_id' columns

        # Calculate and display the total for the user's data
        total = self.calculer_total()
        self.total_label.config(text=f'Total: {total}')

    def selectionner_element(self, event):
        # Récupérer l'élément sélectionné dans le tableau
        selected_item = self.treeview.selection()
        if selected_item:
            self.element_selectionne = selected_item

    def enregistrer(self):
        date = self.date_entry.get()
        nom_produit = self.nom_produit_entry.get()
        prix_unitaire = self.prix_unitaire_entry.get()
        quantite = self.quantite_entry.get()
        nom_fournisseur = self.nom_fournisseur_entry.get()
        type_achat_vente = self.type_combobox.get()

        # Insérer les données dans la table appropriée (Achats ou Vente) en fonction du type
        if type_achat_vente == "Achat":
            self.c.execute('''INSERT INTO Achats (date, nom_produit, prix_unitaire, quantite, nom_fournisseur)
                               VALUES (?, ?, ?, ?, ?)''', (date, nom_produit, prix_unitaire, quantite, nom_fournisseur))
        elif type_achat_vente == "Vente":
            self.c.execute('''INSERT INTO Vente (date, nom_produit, prix_unitaire, quantite, nom_fournisseur)
                               VALUES (?, ?, ?, ?, ?)''', (date, nom_produit, prix_unitaire, quantite, nom_fournisseur))

        # Sauvegarder les modifications
        self.conn.commit()

        # Mettre à jour le tableau (treeview) en ajoutant la nouvelle entrée
        self.treeview.insert('', 'end', values=(date, nom_produit, prix_unitaire, type_achat_vente, quantite, nom_fournisseur))

        # Calculer et afficher le total en bas à droite du tableau
        total = self.calculer_total()
        self.total_label.config(text=f'Total: {total}')

        # Mettre à jour le tableau (treeview) si nécessaire

    def effacer_formulaire(self):
        # Effacer les données saisies dans le formulaire
        self.date_entry.delete(0, END)
        self.nom_produit_entry.delete(0, END)
        self.prix_unitaire_entry.delete(0, END)
        self.type_combobox.set('')
        self.quantite_entry.delete(0, END)
        self.nom_fournisseur_entry.delete(0, END)

        # Supprimer l'élément sélectionné du tableau si un élément est sélectionné
        if self.element_selectionne:
            self.treeview.delete(self.element_selectionne)
            self.element_selectionne = None

    def calculer_total(self):
        total = 0
        for item in self.treeview.get_children():
            total += float(self.treeview.item(item, 'values')[2]) * float(self.treeview.item(item, 'values')[4])
        return total

    def Retour(self):
        self.root.destroy()
        call(["python", "connecter.py"])

    def __del__(self):
        # Fermer la connexion à la base de données lorsque l'objet est détruit
        self.conn.close()

if __name__ == "__main__":
    root = Tk()
    root.resizable(False, False)
    root.iconbitmap("ico.ico")
    
    Id_etr = None
    if len(sys.argv) > 1:
          # Récupère l'ID de l'utilisateur passé en argument
        Id_etr = sys.argv[1]
    obj = Formulaire(root)
    root.mainloop()