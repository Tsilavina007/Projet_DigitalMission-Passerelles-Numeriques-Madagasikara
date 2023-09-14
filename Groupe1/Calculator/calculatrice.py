from tkinter import *
import math
import customtkinter as ctk

# insertion de la valeur des boutons dans l'entrée


def nombre(nbr):
    # x=nbr
    formule.insert(END, nbr)

# affichage des valeurs calculés dans l'entrée


def calcul():
    global resultat
    global Ans
    try:

        # remplacement des caractères en caractères reconnue par python

        resultat = formule.get()
        resultat = resultat.replace(")(", ")*(")
        resultat = resultat.replace("cos(", "math.cos(")
        resultat = resultat.replace("sin(", "math.sin(")
        resultat = resultat.replace("^", "**")
        resultat = resultat.replace("log(", "math.log10(")
        resultat = resultat.replace("tan(", "math.tan(")
        resultat = resultat.replace("÷", "/")
        resultat = resultat.replace("e(", "math.exp(")
        resultat = resultat.replace("ln(", "math.log(")
        resultat = resultat.replace("√(", "math.sqrt(")
        resultat = resultat.replace("!(", "math.factorial(")
        resultat = resultat.replace("%", "/100")
        resultat = resultat.replace("π", "math.pi")

        if "∛" in resultat:
            resultat = resultat.replace("∛", "")
            resultat = resultat+"** (1/3)"

        formule.delete(0, END)

        # insertion de la valeur de resultat dans l'entrée

        formule.insert(0, eval(resultat))


# gestion des erreurs

    except SyntaxError:
        formule.delete(0, END)
        formule.insert(0, "Syntax Error")
    except ZeroDivisionError:
        resultat = "Math Error"
        formule.delete(0, END)
        formule.insert(0, resultat)


# fonction du bouton ANS


def ANS():
    formule.insert(0, eval(resultat))

# Fonction effacer tout les valeurs dans l'entrée


def effacer_tout():
    formule.delete(0, END)

# fonction effacer le dernier caractère dans l'entrée


def effacer_dernier():
    y = formule.get()
    z = y[:-1]
    if y == "Syntax Error":
        formule.delete(0, END)
    if y == "Math Error":
        formule.delete(0, END)
    else:
        formule.delete(0, END)
        formule.insert(0, z)

# création du bouton OFF et de l'entrée unitilisable


def create_off():
    global bouton_off
    global x
    global formule
    global police_entry
# destruction du bouton ON et de l'entrée existante

    formule.delete(0, END)
    formule.destroy()
    bouton_on.destroy()

# création du nouvelle entrée morte (unitilisable "OFF")

    police_entry = ("Arial", 45)
    x = ctk.CTkEntry(maitre, textvariable=equation,
                     font=police_entry, width=170, fg_color="gray30", bg_color="black", corner_radius=5, state='disabled')
    x.grid(row=1, columnspan=7, pady=30, padx=30, ipadx=200, ipady=10)

# création du bouton OFF

    bouton_off = ctk.CTkButton(maitre, text='OFF', command=lambda: create_on(
    ),  height=70, width=80, bg_color="black", fg_color="red", hover_color='red2', corner_radius=10, font=("times", 30))
    bouton_off.grid(row=2, column=3, padx=5, pady=5)


# recréation de l'entrée utilisable et du bouton ON

def create_on():

    # destruction du bouton OFF et de l'entrée morte

    bouton_off.destroy()
    x.destroy()
    global formule
    global police_entry
# recréation de l'entrée utilisable

    formule = ctk.CTkEntry(maitre, textvariable=equation,
                           font=police_entry, width=170, fg_color="gray50", bg_color="black", corner_radius=5)

    formule.grid(row=1, columnspan=7, pady=30, padx=30, ipadx=200, ipady=10)

# création du nouveau bouton ON

    bouton_on = ctk.CTkButton(maitre, text='ON', command=lambda: create_off(
    ),  height=70, width=80,  fg_color="red", hover_color='red2', bg_color="black", corner_radius=10, font=("times", 30))
    bouton_on.grid(row=2, column=3, padx=5, pady=5)
    police_entry = ("Arial", 45)

# Front-End design


maitre = Tk()
maitre.title("Calculatrice")
maitre.configure(bg="#000000")
maitre.geometry("620x630")
equation = StringVar()

police_entry = ("Arial", 45)
titre = ctk.CTkLabel(maitre, text="1+1=2", font=("DS-Digital Italic", 72))
titre.grid(row=2, column=0, rowspan=1, columnspan=3)
formule = ctk.CTkEntry(maitre, textvariable=equation,
                       font=police_entry, width=170, fg_color="gray50", bg_color="black", corner_radius=5)
formule.grid(row=1, columnspan=7, pady=30, padx=30, ipadx=200, ipady=10)

racine_cubique = "∛"
label_text = "x\u207F"

# bouton 2em ligne

bouton_on = ctk.CTkButton(maitre, text='ON', command=lambda: create_off(
),  height=70, width=80,  fg_color="red", bg_color="black", corner_radius=10, font=("times", 30), hover_color="red3")
bouton_on.grid(row=2, column=3, padx=5, pady=5)
bouton1 = ctk.CTkButton(maitre, text='⌫', command=lambda: effacer_dernier(
),  height=70, width=80, bg_color="black", fg_color="red", corner_radius=10, font=("times", 30), hover_color="red3")
bouton1.grid(row=2, column=4, padx=5, pady=5)
bouton1 = ctk.CTkButton(maitre, text='AC', command=lambda: effacer_tout(
),  height=70, width=80, bg_color="black", fg_color="red", corner_radius=10, font=("times", 30), hover_color="red3")
bouton1.grid(row=2, column=5, padx=5, pady=5)

# bouton 3em ligne

bouton_parenthese1 = ctk.CTkButton(maitre, text='π', command=lambda: nombre(
    "π"), height=70, width=80, fg_color="ivory4", bg_color="black", font=("times", 30), hover_color="gray35")
bouton_parenthese1.grid(row=3, column=0, padx=5, pady=5)
bouton1 = ctk.CTkButton(maitre, text='(', command=lambda: nombre(
    "("),  height=70, width=80, fg_color="ivory4",  bg_color="black", corner_radius=10, font=("times", 30), hover_color="gray35")
bouton1.grid(row=3, column=1, padx=5, pady=5)
bouton1 = ctk.CTkButton(maitre, text=')', command=lambda: nombre(
    ")"),  height=70, width=80, fg_color="ivory4", bg_color="black", corner_radius=10, font=("times", 30), hover_color="gray35")
bouton1.grid(row=3, column=2, padx=5, pady=5)
bouton1 = ctk.CTkButton(maitre, text='%', command=lambda: nombre(
    "%"),  height=70, width=80, fg_color="ivory4", bg_color="black", corner_radius=10, font=("times", 30), hover_color="gray35")
bouton1.grid(row=3, column=3, padx=5, pady=5)
bouton1 = ctk.CTkButton(maitre, text=racine_cubique, fg_color="ivory4",  command=lambda: nombre(
    "∛"),  height=70, width=80, bg_color="black", corner_radius=10, font=("times", 30), hover_color="gray35")
bouton1.grid(row=3, column=4, padx=5, pady=5)
bouton1 = ctk.CTkButton(maitre, text='ANS', fg_color="brown1", hover_color='firebrick3', command=lambda: ANS(
),  height=70, width=80, bg_color="black", corner_radius=10, font=("times", 30))
bouton1.grid(row=3, column=5, padx=5, pady=5)

# bouton 4em ligne

bouton_parenthese1 = ctk.CTkButton(maitre, text='sin', command=lambda: nombre(
    "sin("), height=70, width=80, fg_color="ivory4", bg_color="black", font=("times", 30), hover_color="gray35")
bouton_parenthese1.grid(row=4, column=0, padx=5, pady=5)
bouton1 = ctk.CTkButton(maitre, text='√', fg_color="ivory4", command=lambda: nombre("√("
                                                                                    ),  height=70, width=80, bg_color="black", corner_radius=10, font=("times", 30), hover_color="gray35")
bouton1.grid(row=4, column=1, padx=5, pady=5)
bouton1 = ctk.CTkButton(maitre, text='7', command=lambda: nombre(
    "7"),  height=70, width=80, bg_color="black", corner_radius=10, font=("times", 30))
bouton1.grid(row=4, column=2, padx=5, pady=5)
bouton1 = ctk.CTkButton(maitre, text='8', command=lambda: nombre(
    "8"),  height=70, width=80, bg_color="black", corner_radius=10, font=("times", 30))
bouton1.grid(row=4, column=3, padx=5, pady=5)
bouton1 = ctk.CTkButton(maitre, text='9', command=lambda: nombre(
    "9"),  height=70, width=80, bg_color="black", corner_radius=10, font=("times", 30))
bouton1.grid(row=4, column=4, padx=5, pady=5)
bouton1 = ctk.CTkButton(maitre, text='÷', command=lambda: nombre(
    "÷"),  height=70, width=80, fg_color="brown1", hover_color='firebrick3', bg_color="black", corner_radius=10, font=("times", 30))
bouton1.grid(row=4, column=5, padx=5, pady=5)

# bouton 5em ligne

bouton_parenthese1 = ctk.CTkButton(maitre, text='cos', command=lambda: nombre(
    "cos("), height=70, width=80, fg_color="ivory4", bg_color="black", font=("times", 30), hover_color="gray35")
bouton_parenthese1.grid(row=5, column=0, padx=5, pady=5)
bouton1 = ctk.CTkButton(maitre, text='ln', command=lambda: nombre(
    "ln("),  height=70, width=80, fg_color="ivory4", bg_color="black", corner_radius=10, font=("times", 30), hover_color="gray35")
bouton1.grid(row=5, column=1, padx=5, pady=5)
bouton1 = ctk.CTkButton(maitre, text='4', command=lambda: nombre(
    "4"),  height=70, width=80, bg_color="black", corner_radius=10, font=("times", 30))
bouton1.grid(row=5, column=2, padx=5, pady=5)
bouton1 = ctk.CTkButton(maitre, text='5', command=lambda: nombre(
    "5"),  height=70, width=80, bg_color="black", corner_radius=10, font=("times", 30))
bouton1.grid(row=5, column=3, padx=5, pady=5)
bouton1 = ctk.CTkButton(maitre, text='6', command=lambda: nombre(
    "6"),  height=70, width=80, bg_color="black", corner_radius=10, font=("times", 30))
bouton1.grid(row=5, column=4, padx=5, pady=5)
bouton1 = ctk.CTkButton(maitre, text='x', command=lambda: nombre(
    "*"),  height=70, width=80, fg_color="brown1", hover_color='firebrick3',  bg_color="black", corner_radius=10, font=("times", 30))
bouton1.grid(row=5, column=5, padx=5, pady=5)

# bouton 6em ligne

bouton_parenthese1 = ctk.CTkButton(maitre, text='tan', command=lambda: nombre(
    "tan("), height=70, width=80, fg_color="ivory4", bg_color="black", font=("times", 30), hover_color="gray35")
bouton_parenthese1.grid(row=6, column=0, padx=5, pady=5)
bouton1 = ctk.CTkButton(maitre, text="log", command=lambda: nombre(
    "log("),  height=70, width=80, fg_color="ivory4",  bg_color="black", corner_radius=10, font=("times", 30), hover_color="gray35")
bouton1.grid(row=6, column=1, padx=5, pady=5)
bouton1 = ctk.CTkButton(maitre, text='1', command=lambda: nombre(
    "1"),  height=70, width=80, bg_color="black", corner_radius=10, font=("times", 30))
bouton1.grid(row=6, column=2, padx=5, pady=5)
bouton1 = ctk.CTkButton(maitre, text='2', command=lambda: nombre(
    "2"),  height=70, width=80, bg_color="black", corner_radius=10, font=("times", 30))
bouton1.grid(row=6, column=3, padx=5, pady=5)
bouton1 = ctk.CTkButton(maitre, text='3', command=lambda: nombre(
    "3"),  height=70, width=80, bg_color="black", corner_radius=10, font=("times", 30))
bouton1.grid(row=6, column=4, padx=5, pady=5)
bouton1 = ctk.CTkButton(maitre, text='-', command=lambda: nombre(
    "-"),  height=70, width=80, fg_color="brown1", hover_color='firebrick3', bg_color="black", corner_radius=10, font=("times", 30))
bouton1.grid(row=6, column=5, padx=5, pady=5)

# bouton 7em ligne

bouton_parenthese1 = ctk.CTkButton(maitre, text='x!', command=lambda: nombre("!("
                                                                             ), height=70, width=80, fg_color="ivory4", bg_color="black", font=("times", 30), hover_color="gray35")
bouton_parenthese1.grid(row=7, column=0, padx=5, pady=5)
bouton1 = ctk.CTkButton(maitre, text=label_text, command=lambda: nombre(
    "^"),  height=70, width=80, fg_color="ivory4",  bg_color="black", corner_radius=10, font=("times", 30), hover_color="gray35")
bouton1.grid(row=7, column=1, padx=5, pady=5)
bouton1 = ctk.CTkButton(maitre, text=' 0', command=lambda: nombre(
    "0"),  height=70, width=80, bg_color="black", corner_radius=10, font=("times", 30))
bouton1.grid(row=7, column=2, padx=5, pady=5)
bouton1 = ctk.CTkButton(maitre, text='.', command=lambda: nombre(
    "."),  height=70, width=80, bg_color="black", corner_radius=10, font=("times", 30))
bouton1.grid(row=7, column=3, padx=5, pady=5)
bouton1 = ctk.CTkButton(maitre, text='=', command=lambda: calcul(
),  height=70, width=80, bg_color="black", fg_color="RoyalBlue4", corner_radius=10, font=("times", 30))
bouton1.grid(row=7, column=4, padx=5, pady=5)
bouton1 = ctk.CTkButton(maitre, text='+', command=lambda: nombre(
    "+"),  height=70, width=80, fg_color="brown1", hover_color='firebrick3',  bg_color="black", corner_radius=10, font=("times", 30))
bouton1.grid(row=7, column=5, padx=5, pady=5)

maitre.mainloop()
