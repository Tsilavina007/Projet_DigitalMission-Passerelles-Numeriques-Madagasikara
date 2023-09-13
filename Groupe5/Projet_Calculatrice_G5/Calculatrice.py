
from tkinter import *
import tkinter as tk
from math import *
import tkinter.messagebox


# Creation fenetre
root = Tk()   # Créer une instance de la fenêtre principale
root.title("Calculatrice Scientifique")   # Définir le titre de la fenêtre
root.configure(background="DeepSkyBlue")   # Définir la couleur de fond de la fenêtre
root.resizable(width=False, height=False)   # Désactiver le redimensionnement de la fenêtre
root.geometry("384x540+0+0")   # Définir les dimensions et la position de la fenêtre sur l'écran

frame = tk.Frame(root, borderwidth=12, relief=GROOVE, bg="DeepSkyBlue")   # Créer un cadre à l'intérieur de la fenêtre principale
frame.pack(fill=BOTH, expand=True)   # Placer le cadre dans la fenêtre, en le remplissant horizontalement et verticalement
        
test_mode = Test_OnOff = Test_Egal = result = 0   # Initialisation des variables test_mode, Test_OnOff, Test_Egal et result à 0

def quitter():
    # Afficher une boîte de dialogue demandant confirmation pour quitter
    quitter = tkinter.messagebox.askyesno("Calculatrice Scientifique", "Êtes-vous sûr de vouloir quitter ?")
    if quitter > 0:
        root.destroy()  # Fermer la fenêtre principale de l'application

def scientifique():
    root.resizable(width=False, height=False)  # Désactiver le redimensionnement de la fenêtre
    root.geometry("755x540+0+0")  # Définir les dimensions et la position de la fenêtre

def standard():
    root.resizable(width=False, height=False)  # Désactiver le redimensionnement de la fenêtre
    root.geometry("384x540+0+0")  # Définir les dimensions et la position de la fenêtre


def mode():
    global test_mode, color_bt
    if test_mode:
        # Mode éclair
        frame['bg'] = "DeepSkyBlue"   # Changer la couleur de fond du cadre en bleu ciel
        text['fg'] = "black"   # Changer la couleur du texte en noir
        text['bg'] = "DeepSkyBlue"   # Changer la couleur de fond du texte en bleu ciel
        label['bg'] = "DeepSkyBlue"   # Changer la couleur de fond de l'étiquette en bleu ciel
        entry['bg'] = "white"   # Changer la couleur de fond de la zone de saisie en blanc
        entry['fg'] = "black"   # Changer la couleur du texte de la zone de saisie en noir
        test_mode = 0   # Définir la variable test_mode à 0 (mode éclair désactivé)
    else:
        # Mode nuit
        frame['bg'] = "black"   # Changer la couleur de fond du cadre en noir
        text['fg'] = "white"   # Changer la couleur du texte en blanc
        text['bg'] = "black"   # Changer la couleur de fond du texte en noir
        label['bg'] = "white"   # Changer la couleur de fond de l'étiquette en blanc
        entry['bg'] = "grey"   # Changer la couleur de fond de la zone de saisie en gris
        entry['fg'] = "white"   # Changer la couleur du texte de la zone de saisie en blanc
        test_mode = 1   # Définir la variable test_mode à 1 (mode éclair activé)


menubar = Menu(frame)   # Créer une barre de menu à l'intérieur du cadre

menubar.add_command(label="Simple", command=standard)   # Ajouter une commande "Simple" dans la barre de menu, associée à la fonction standard()
menubar.add_command(label="Scientifique", command=scientifique)   # Ajouter une commande "Scientifique" dans la barre de menu, associée à la fonction scientifique()
menubar.add_command(label="Mode", command=mode)   # Ajouter une commande "Mode" dans la barre de menu, associée à la fonction mode()
menubar.add_command(label="Quitter", command=quitter)   # Ajouter une commande "Quitter" dans la barre de menu, associée à la fonction quitter()



def button_click(number):
    global Test_OnOff, Test_Egal

    if Test_Egal:     # Si Test_Egal est vrai, on vérifie les actions en fonction du bouton
        if number == "On":
            # Si le bouton est "On", on effectue les actions suivantes
            entry.delete(0, tk.END)  # Supprime le contenu du champ d'entrée
            entry['state'] = NORMAL  # Active le champ d'entrée
            entry['disabledbackground'] = ""  # Met le fond en noir
            Test_OnOff = 0  # Met Test_OnOff à 0 pour indiquer que le mode est activé
        elif number == "Off":
            # Si le bouton est "Off", on effectue les actions suivantes
            entry.delete(0, tk.END)  # Supprime le contenu du champ d'entrée
            entry['state'] = DISABLED  # Désactive le champ d'entrée
            entry['disabledbackground'] = "black"  # Met le fond en noir
            Test_OnOff = 1  # Met Test_OnOff à 1 pour indiquer que le mode est désactivé
        elif number == "⌫":
            # Si le bouton est "⌫", on effectue les actions suivantes
            entry.delete(0, tk.END)  # Supprime le contenu du champ d'entrée
            Test_Egal = 0  # Met Test_Egal à 0 pour indiquer que l'égalité a été réinitialisée
        else:
            # Si le bouton n'est pas "On/Off", on insère la valeur du bouton dans le champ d'entrée
            entry.delete(0, tk.END)  # Supprime le contenu du champ d'entrée
            entry.insert(tk.END, str(number))  # Insère la valeur du bouton dans le champ d'entrée
            Test_Egal = 0  # Met Test_Egal à 0 pour indiquer que l'égalité a été réinitialisée
    else:
        # Si Test_Egal est faux, on vérifie les autres actions en fonction du bouton
        if number == "On":
            # Si le bouton est "On", on effectue les actions suivantes
            entry.delete(0, tk.END)  # Supprime le contenu du champ d'entrée
            entry['state'] = NORMAL  # Active le champ d'entrée
            entry['disabledbackground'] = ""  # Met le fond en noir
            Test_OnOff = 0  # Met Test_OnOff à 0 pour indiquer que le mode est activé
        elif number == "Off":
            # Si le bouton est "Off", on effectue les actions suivantes
            entry.delete(0, tk.END)  # Supprime le contenu du champ d'entrée
            entry['state'] = DISABLED  # Désactive le champ d'entrée
            entry['disabledbackground'] = "black"  # Met le fond en noir
            Test_OnOff = 1  # Met Test_OnOff à 1 pour indiquer que le mode est désactivé
        elif number == "⌫":
            # Si le bouton est "⌫", on effectue les actions suivantes
            user_input = entry.get()  # Récupère le contenu actuel du champ d'entrée
            entry.delete(0, tk.END)  # Supprime le contenu du champ d'entrée
            entry.insert(tk.END, user_input[:-1])  # Insère le contenu du champ d'entrée sans le dernier caractère
        elif number == "x":
            # Si le bouton est "x", on effectue les actions suivantes
            current = entry.get()  # Récupère le contenu actuel du champ d'entrée
            entry.delete(0, tk.END)  # Supprime le contenu du champ d'entrée
            entry.insert(tk.END, current + "*")  # Insère le contenu actuel du champ d'entrée suivi de "*"
        elif number == "Deg":
            # Si le bouton est "Deg", on effectue les actions suivantes
            current = entry.get()  # Récupère le contenu actuel du champ d'entrée
            entry.delete(0, tk.END)  # Supprime le contenu du champ d'entrée
            entry.insert(tk.END, current + "°")  # Insère le contenu actuel du champ d'entrée suivi de "°"
        elif number == "xⁿ":
            # Si le bouton est "xⁿ", on effectue les actions suivantes
            current = entry.get()  # Récupère le contenu actuel du champ d'entrée
            entry.delete(0, tk.END)  # Supprime le contenu du champ d'entrée
            entry.insert(tk.END, current + "ˆ(")  # Insère le contenu actuel du champ d'entrée suivi de "ˆ("
        elif number == "x²":
            # Si le bouton est "x²", on effectue les actions suivantes
            current = entry.get()  # Récupère le contenu actuel du champ d'entrée
            entry.delete(0, tk.END)  # Supprime le contenu du champ d'entrée
            entry.insert(tk.END, current + "²")  # Insère le contenu actuel du champ d'entrée suivi de "²"
        elif number == "x³":
            # Si le bouton est "x³", on effectue les actions suivantes
            current = entry.get()  # Récupère le contenu actuel du champ d'entrée
            entry.delete(0, tk.END)  # Supprime le contenu du champ d'entrée
            entry.insert(tk.END, current + "³")  # Insère le contenu actuel du champ d'entrée suivi de "³"
        elif number == "exp":
            # Si le bouton est "exp", on effectue les actions suivantes
            current = entry.get()  # Récupère le contenu actuel du champ d'entrée
            entry.delete(0, tk.END)  # Supprime le contenu du champ d'entrée
            entry.insert(tk.END, current + "eˆ(")  # Insère le contenu actuel du champ d'entrée suivi de "eˆ("
        else:
            # Si le bouton ne correspond à aucune action spécifique, on insère simplement la valeur du bouton dans le champ d'entrée
            current = entry.get()  # Récupère le contenu actuel du champ d'entrée
            entry.delete(0, tk.END)  # Supprime le contenu du champ d'entrée
            entry.insert(tk.END, current + str(number))  # Insère le contenu actuel du champ d'entrée suivi de la valeur du bouton

    entry.xview_moveto(1)  # Déplace la vue du champ d'entrée vers la droite


def move_text_left():
    # Fonction pour déplacer le texte du champ d'entrée vers la gauche
    entry.xview_scroll(-1, 'units')  # Déplace la vue du champ d'entrée d'une unité vers la gauche

def move_text_right():
    # Fonction pour déplacer le texte du champ d'entrée vers la droite
    entry.xview_scroll(1, 'units')  # Déplace la vue du champ d'entrée d'une unité vers la droite


def button_equal():
    global Test_Egal, result

    Test_Egal = 1  # Indique que le bouton d'égalité a été enclenché
    expression = entry.get()  # Récupère l'expression dans le champ d'entrée

    try:
        # Remplace certains symboles et fonctions par leurs équivalents pour évaluer l'expression
        expression = expression.replace("Ans", str(result)).replace("√", "sqrt").replace("π", str(pi)) \
            .replace("ˆ", "**").replace("log", "log10").replace("ln", "log").replace("Deg", "radians") \
            .replace("²", "**2").replace("³", "**3").replace("%", "*(1/100)").replace("Rad", "degrees")

        result = str(eval(expression))  # Évalue l'expression et stocke le résultat
        entry.delete(0, tk.END)  # Efface le contenu du champ d'entrée
        entry.insert(tk.END, result)  # Insère le résultat dans le champ d'entrée
        print(result)  # Affiche le résultat dans la console
    except:
        entry.delete(0, tk.END)  # Efface le contenu du champ d'entrée
        entry.insert(tk.END, "Erreur")  # Affiche "Erreur" dans le champ d'entrée en cas d'erreur lors de l'évaluation


def button_clear():   #fonction pour le boutton clear
    entry.config(state='normal')  # Réactive l'état normal du champ d'entrée pour permettre la suppression
    entry.delete(0, tk.END)  # Efface tout le contenu du champ d'entrée

#----------------------------------------------------------------------------------------------------
# Zone de texte
entry =Entry(frame, width=14, highlightcolor="black", font=("Arial", 34), bd=8, state=NORMAL)
entry.grid(row=0, column=0, columnspan=4)

#Charger l'image
image = tk.PhotoImage(file="logoPN.png")
resized_image = image.subsample(4, 4)  # Modifier la taille de l'image

label = Label(frame, image=resized_image, bg="DeepSkyBlue")  # Créer le widget Label avec l'image
label.grid(row=0, column=7)

# Frame1 pour les boutton deplacer
frame1 = tk.Frame(frame, borderwidth=3, relief=GROOVE, bg="DeepSkyBlue")
frame1.grid(row=0, column=4)

# Boutton deplacer gauche droite
tk.Button(frame1, text='<', command=move_text_left).grid(row=0, column=0, padx=2, pady=2)
tk.Button(frame1, text='>', command=move_text_right).grid(row=0, column=1, padx=2, pady=2)

# Text PNM Calculator
text = tk.Label(frame, text="PNM Calculator", fg="Black", bg="DeepSkyBlue", font=("Brush Script MT", 20))
text.grid(row=0, column=5, columnspan=2)

# Liste des bouttons, avec le text, ligne et colone
buttons = [("On", 1, 0), ("Off", 1, 1), ("AC", 1, 2), ("⌫", 1, 3),("e", 1, 4), ("π", 1, 5), ("%", 1, 6), ("Ans", 1, 7),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("+", 2, 3), ("asinh", 2, 4), ("acosh", 2, 5), ("atanh", 2, 6), ("x²", 2, 7),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3), ("sin", 3, 4), ("cos", 3, 5), ("tan", 3, 6), ("x³", 3, 7),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("x", 4, 3), ("ln", 4, 4), ("log", 4, 5), ("exp", 4, 6), ("xⁿ", 4, 7),
    ("0", 5, 0), (".", 5, 1), ("=", 5, 2), ("/", 5, 3), ("(", 5, 4), (")", 5, 5), ("Deg", 5, 6), ("Rad", 5, 7)
]

# Emplacement des bouttons avec un boucle
for button_text, row, column in buttons:
    # Crée un bouton avec les paramètres spécifiés qui specifie un boutton pendant chaque iteration
    button = tk.Button(frame, text=button_text, width=4, height=2, bg="CadetBlue", font=("Lucida Console", 20),
                       relief=GROOVE, borderwidth=6, command=lambda text=button_text: button_click(text))

    # Configuration du fond du bouton en fonction du texte du bouton
    if button_text in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        button['bg'] = "AliceBlue"
    if button_text in [".", "=", "+", "-", "x", "/"]:
        button['bg'] = "Turquoise"
    if button_text in ["asinh", "acosh", "atanh"]:
        button['font'], button['width'], button['height'] = ("Lucida Console", 14), 6, 3

    # Configuration de la commande du bouton en fonction du texte du bouton
    if button_text == "=":
        button.config(command=lambda: button_equal())
    if button_text == "AC":
        button.config(command=lambda: button_clear())
    if button_text in ["sin","asinh", "cos","acosh", "tan","atanh","√", "ln", "log", "Deg"]:
        button.config(command=lambda text=button_text: button_click((text + "(")))

    # Positionne le bouton dans la grille
    button.grid(row=row, column=column, padx=4, pady=4)

root.config(menu=menubar)
root.mainloop()