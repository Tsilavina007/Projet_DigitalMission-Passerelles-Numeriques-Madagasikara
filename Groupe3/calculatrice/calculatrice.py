import tkinter as tk
from tkinter import *
import math
import customtkinter # module pour les boutons

#fonction qui prend les valeurs click
def button_click(nbr):
    txtDisplay.insert(tk.END, nbr)

resultat=""

#fonction de le bouton egal
def button_equals():
    try:
        global resultat
        expression = str(txtDisplay.get())
        substitutions = {
            "sin(": "math.sin(",
            "cos(": "math.cos(",
            "tan(": "math.tan(",
            "log(": "math.log10(",
            "ln(": "math.log(",
            "fact(": "math.factorial(",
            "√": "math.sqrt(",
            "e":"math.exp(",
            "EXP":"*10**",
            "π":"22/7",
            "%":"* (1/100)",
            "ANS":str(resultat),
            }
        for val, replacement in substitutions.items():#On verifie si les resultats obtenu est parmi le dictionnaire en haut et on change les expression par ces vrai expression dans le module math
            if val in expression:
                if val == "√" or val == "e":
                    expression = expression.replace(val, replacement)
                    expression += ")"
                else:
                    expression = expression.replace(val, replacement)
        resultat = eval(expression)#On evalue les expressions
        txtDisplay.delete(0, tk.END)
        txtDisplay.insert(tk.END, resultat)

    except SyntaxError:#Exception pour l'erreur de syntaxe
        txtDisplay.delete(0, tk.END)
        error="SYNTAX ERROR"
        txtDisplay.insert(tk.END, error)
    except ZeroDivisionError:#Exception pour le division par zéro
        txtDisplay.delete(0, tk.END)
        error="MATH ERROR"
        txtDisplay.insert(tk.END, error)

#fonction qui efface un à un
def button_clear():
    text = txtDisplay.get()
    text = text[:-1]  # Supprime le dernier caractère
    txtDisplay.delete(0, "end")  # Efface tout le contenu du widget Entry
    txtDisplay.insert(0, text)  # Réinsère le texte modifié dans le widget Entry


#Fonction qui efface tous
def button_clear_all():
    txtDisplay.delete("0", "end")

#Fonction qui fait marcher et arret
def button_onoff():
    if txtDisplay["state"] == "normal":
        txtDisplay.delete(0, tk.END)
        txtDisplay.configure(state="disabled")
    else:
        txtDisplay.configure(state="normal")
        txtDisplay.configure(bg="white")  # Réinitialiser la couleur de fond à sa valeur par défaut


#fonction pour afficher l'aide
def Apropos():
    msg = Toplevel()
    Message(msg, width=200, aspect=100, justify=CENTER,
            text="Calculatrice Scientifique\n\n(C) Team Alpha, Juin 2023.\nDigital Mission Project\nVersion 1.0",bg='#68aec9',fg='white').pack(padx=3, pady=3)




#front
# Création de la fenetre
calculatrice = tk.Tk()
calculatrice.geometry("590x455")
calculatrice.title("Calculatrice Scientifique")
calculatrice.config(bg="PeachPuff4")
calculatrice.resizable(False, False)


#barre de menu

menubar = Menu(calculatrice)

# Menu Fichier en bas de la barre de fenetre
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="Quitter", command=calculatrice.quit)
file_menu.add_command(label="A propos", command=Apropos)
menubar.add_cascade(label="Fichier", menu=file_menu)

calculatrice.config(menu=menubar)

#Création des frame ou cadre
main_color = "#262626"
top_frame_color = "ivory4"

top_frame = Frame(calculatrice, bg=main_color)
top_frame.pack(side=TOP, fill=X)

bottom_frame = Frame(calculatrice, bg=main_color)
bottom_frame.pack(side=TOP, fill=BOTH, expand=True)

txtDisplay = Entry(top_frame, font=("ds-digital", 40, "bold"), width=40, borderwidth=10, relief="sunken", justify="right")
txtDisplay.pack(side=LEFT, padx=10, pady=10, expand=True, fill=X)

main_font = customtkinter.CTkFont(family="Helvetica", size=12)

#paramétres pour les styles des boutons
params = {
    'font' : main_font,
    'text_color' : "#eda850",
    'hover' : True,
    'hover_color' : "black",
    'height' : 40,
    'width' : 120,
    'border_width' : 1,
    'corner_radius' : 10,
    'border_color' : "#eda850",
    'bg_color' : "#262626",
    'fg_color' : "#262626"
    }

params1 = {
    'font' : main_font,
    'text_color' : "#68aec9",
    'hover' : True,
    'hover_color' : "black",
    'height' : 40,
    'width' : 120,
    'border_width' : 1,
    'corner_radius' : 10,
    'border_color' : "#68aec9",
    'bg_color' : "#262626",
    'fg_color' : "#262626"
    }


boutons1 = customtkinter.CTkButton(bottom_frame, text="ON/OFF", **params1, command=button_onoff)
boutons1.grid(row=0, column=0, padx=2, pady=2)
boutons2 = customtkinter.CTkButton(bottom_frame, text="π", command=lambda:button_click("π"),**params1).grid(row=0, column=1, padx=2, pady=2)
boutons3 = customtkinter.CTkButton(bottom_frame, text="%", command=lambda:button_click("%"), **params1).grid(row=0, column=2, padx=2, pady=2)
boutons4 = customtkinter.CTkButton(bottom_frame, text="⌫", command=button_clear, **params1)
boutons4.grid(row=0, column=3, padx=2, pady=2)
boutons5 = customtkinter.CTkButton(bottom_frame, text="AC", command=button_clear_all, **params1)
boutons5.grid(row=0, column=4, padx=2, pady=2)
boutons6 = customtkinter.CTkButton(bottom_frame, text="fact", command=lambda:button_click("fact("), **params1).grid(row=1, column=0, padx=2, pady=2)
boutons7 = customtkinter.CTkButton(bottom_frame, text="ln", command=lambda:button_click("ln("), **params1).grid(row=1, column=1, padx=2, pady=2)
boutons8 = customtkinter.CTkButton(bottom_frame, text="log", command=lambda:button_click("log("), **params1).grid(row=1, column=2, padx=2, pady=2)
boutons9 = customtkinter.CTkButton(bottom_frame, text="√", command=lambda:button_click("√"), **params1).grid(row=1, column=3, padx=2, pady=2)
boutons10 = customtkinter.CTkButton(bottom_frame, text="3√", command=lambda:button_click("**1/3"), **params1).grid(row=1, column=4, padx=2, pady=2)
boutons11 = customtkinter.CTkButton(bottom_frame, text="sin", command=lambda:button_click("sin("), **params1).grid(row=2, column=0, padx=2, pady=2)
boutons12 = customtkinter.CTkButton(bottom_frame, text="cos", command=lambda:button_click("cos("), **params1).grid(row=2, column=1, padx=2, pady=2)
boutons13 = customtkinter.CTkButton(bottom_frame, text="tan", command=lambda:button_click("tan("), **params1).grid(row=2, column=2, padx=2, pady=2)
boutons14 = customtkinter.CTkButton(bottom_frame, text="e", command=lambda:button_click("e"), **params1).grid(row=2, column=3, padx=2, pady=2)
boutons16 = customtkinter.CTkButton(bottom_frame, text="7", command=lambda:button_click("7"), **params).grid(row=3, column=0, padx=2, pady=2)
boutons17 = customtkinter.CTkButton(bottom_frame, text="8", command=lambda:button_click("8"), **params).grid(row=3, column=1, padx=2, pady=2)
boutons18 = customtkinter.CTkButton(bottom_frame, text="9", command=lambda:button_click("9"), **params).grid(row=3, column=2, padx=2, pady=2)
boutons19 = customtkinter.CTkButton(bottom_frame, text="(", command=lambda:button_click("("), **params1).grid(row=3, column=3, padx=2, pady=2)
boutons20 = customtkinter.CTkButton(bottom_frame, text=")", command=lambda:button_click(")"), **params1).grid(row=3, column=4, padx=2, pady=2)
boutons21 = customtkinter.CTkButton(bottom_frame, text="4", command=lambda:button_click("4"), **params).grid(row=4, column=0, padx=2, pady=2)
boutons22 = customtkinter.CTkButton(bottom_frame, text="5", command=lambda:button_click("5"), **params).grid(row=4, column=1, padx=2, pady=2)
boutons23 = customtkinter.CTkButton(bottom_frame, text="6", command=lambda:button_click("6"), **params).grid(row=4, column=2, padx=2, pady=2)
boutons24 = customtkinter.CTkButton(bottom_frame, text="X", command=lambda:button_click("*"), **params1)
boutons24.grid(row=4, column=3, padx=2, pady=2)
boutons26 = customtkinter.CTkButton(bottom_frame, text="/", command=lambda:button_click("/"), **params1)
boutons26.grid(row=4, column=4, padx=2, pady=2)
boutons27 = customtkinter.CTkButton(bottom_frame, text="x²", command=lambda:button_click("**2"), **params1).grid(row=2, column=4, padx=2, pady=2)
boutons28 = customtkinter.CTkButton(bottom_frame, text="1",command=lambda:button_click("1"), **params).grid(row=5, column=0, padx=2, pady=2)
boutons29 = customtkinter.CTkButton(bottom_frame, text="2", command=lambda:button_click("2"), **params).grid(row=5, column=1, padx=2, pady=2)
boutons30 = customtkinter.CTkButton(bottom_frame, text="3", command=lambda:button_click("3"), **params).grid(row=5, column=2, padx=2, pady=2)
boutons32 = customtkinter.CTkButton(bottom_frame, text="+ ", command=lambda:button_click("+"), **params1)
boutons32.grid(row=5, column=3, padx=2, pady=2)
boutons34 = customtkinter.CTkButton(bottom_frame, text="-", command=lambda:button_click("-"), **params1)
boutons34.grid(row=5, column=4, padx=2, pady=2)
boutons35 = customtkinter.CTkButton(bottom_frame, text="√", command=lambda:button_click("√"), **params1).grid(row=6, column=4, padx=2, pady=2)
boutons36 = customtkinter.CTkButton(bottom_frame, text="0", command=lambda:button_click("0"), **params).grid(row=6, column=0, padx=2, pady=2)
boutons37 = customtkinter.CTkButton(bottom_frame, text="EXP", command=lambda:button_click("EXP"), **params1).grid(row=6, column=1, padx=2, pady=2)
boutons38 = customtkinter.CTkButton(bottom_frame, text="ANS", command=lambda:button_click("ANS"), **params1).grid(row=6, column=2, padx=2, pady=2)
boutons39 = customtkinter.CTkButton(bottom_frame, text=".", command=lambda:button_click("."), **params1).grid(row=6, column=3, padx=2, pady=2)
boutons40 = customtkinter.CTkButton(bottom_frame, text="=", command=button_equals, **params1)
boutons40.grid(row=6, column=4, padx=2, pady=2)


bottom_frame.grid_rowconfigure(0, weight=1)
bottom_frame.grid_rowconfigure(1, weight=1)
bottom_frame.grid_rowconfigure(2, weight=1)
bottom_frame.grid_rowconfigure(3, weight=1)
bottom_frame.grid_rowconfigure(4, weight=1)
bottom_frame.grid_rowconfigure(5, weight=1)
bottom_frame.grid_rowconfigure(6, weight=1)
bottom_frame.grid_columnconfigure(0, weight=1, pad=0)
bottom_frame.grid_columnconfigure(1, weight=1, pad=0)
bottom_frame.grid_columnconfigure(2, weight=1, pad=0)
bottom_frame.grid_columnconfigure(3, weight=1, pad=0)
bottom_frame.grid_columnconfigure(4, weight=1, pad=0)
bottom_frame.grid_columnconfigure(5, weight=1, pad=0)
bottom_frame.grid_columnconfigure(6, weight=1, pad=0)

calculatrice.mainloop()