import math
import tkinter as tk
from math import *

# Affichage sur l'ecran
def affiche(texte, index):
    texte_affiche = texte
    ecran.insert(index, texte_affiche)

# Calcul
def calculer():
    #Recuperation le valeur sur l'ecran
    calcul = ecran.get()
    #Essayer de calcul de la resultat et afficher
    try:
        resultat = eval(calcul)
        ecran.delete(0, tk.END)
        ecran.insert(0, resultat)
    except:
        ecran.delete(0, tk.END)
        ecran.insert(0, "Error")

# fonction delete
def supprimer_one_one():
    current_text = ecran.get()
    nouveau_texte = current_text[:-1]
    ecran.delete(0, tk.END)
    ecran.insert(tk.END, nouveau_texte)
def supprimer_all():
    current_text = ecran.get()
    nouveau_texte = current_text[:0]
    ecran.delete(0, tk.END)
    ecran.insert(tk.END, nouveau_texte)

# creation fenetre root
root = tk.Tk()
root.title("E-DATE Calculator®")

#creation fenetre
canvas = tk.Canvas(root, width=479, height=700, bg="black")
canvas.pack()

# Marque de la machine
texte = "E-DATE"
position_x = 120
position_y = 30
canvas.create_text(position_x, position_y, text=texte, font=("digital-7", 30, "bold"), fill="white")
texte = "Calculator®"
position_x = 250
position_y = 30
canvas.create_text(position_x, position_y, text=texte, font=("Arial", 20,), fill="white")


# creation d'ecran de calcul
ecran = tk.Entry(canvas, width=22, font=("digital-7", 30, "bold"), bg="olive", bd=10)
ecran.place(x=22, y=50, height=80)

# creation d'ecran en lettre
ecran2 = tk.Text(canvas, width=20, font=("arial", 15, "bold"), bg="olive", bd=10)
ecran2.place(x=22, y=150, height=80)

# creation des boutons
                 # 1ere ligne des boutons
bouton_effacer = tk.Button(canvas, text="On", command=supprimer_one_one, width=3, height=1, bd=10, font=("Arial", 12,"bold", ))
bouton_effacer.config(fg="green")
bouton_effacer.place(x=405, y=180)
bouton_effacer = tk.Button(canvas, text="Off", command=supprimer_one_one, width=3, height=1, bd=10, font=("Arial", 12,"bold"))
bouton_effacer.config(fg="red")
bouton_effacer.place(x=305, y=180)
                 # 2eme ligne des boutons
bouton_cos = tk.Button(canvas, text="cos", command=lambda:  affiche("cos (", '1000'), width=3, height=1, bd=10, font=("Arial", 12,"bold"))
bouton_cos.place(x=20, y=250)
bouton_sin = tk.Button(canvas, text="sin", command=lambda:  affiche("sin (", '1000'), width=3, height=1, bd=10, font=("Arial", 12,"bold"))
bouton_sin.place(x=105, y=250)
bouton_sqrt = tk.Button(canvas, text="x²", command=lambda:  affiche("x²", '1000'), width=3, height=1, bd=10, font=("Arial", 12,"bold"))
bouton_sqrt.place(x=205, y=250)
bouton_racine = tk.Button(canvas, text="√", command=lambda: affiche("sqrt", '1000'), width=3, height=1, bd=10, font=("Arial", 12,"bold"))
bouton_racine.place(x=305, y=250)
bouton_factorielle = tk.Button(canvas, text="x!", command=lambda: affiche("x!²", '1000'), width=3, height=1, bd=10, font=("Arial", 12,"bold"))
bouton_factorielle.place(x=405, y=250)
                 # 3eme ligne des bouton
bouton_tan = tk.Button(canvas, text="tan", command=lambda: affiche("tan(", '1000'), width=3, height=1, bd=10, font=("Alrial", 12,"bold"))
bouton_tan.place(x=20, y=320)
bouton_ln = tk.Button(canvas, text="ln", command=lambda: affiche("ln(", '1000'), width=3, height=1, bd=10, font=("Alrial", 12,"bold"))
bouton_ln.place(x=105, y=320)
bouton_exp = tk.Button(canvas, text="exp", command=lambda: affiche("exp(", '1000'), width=3, height=1, bd=10, font=("Alrial", 12,"bold"))
bouton_exp.place(x=205, y=320)
bouton_puit = tk.Button(canvas, text="π", command=lambda: affiche("pi", '1000'), width=3, height=1, bd=10, font=("Alrial", 12,"bold"))
bouton_puit.place(x=305, y=320)
bouton_division = tk.Button(canvas, text="/", command=lambda: affiche("/", '1000'), width=3, height=1, bd=10, font=("Alrial", 12,"bold"))
bouton_division.place(x=405, y=320)
                 # 4eme ligne des boutons
bouton_parouver = tk.Button(canvas, text="(", command=lambda: affiche("(", '1000'), width=3, height=1, bd=10, font=("Alrial", 12,"bold"))
bouton_parouver.place(x=20, y=390)
bouton_sept = tk.Button(canvas, text="7", command=lambda: affiche("7", '1000'), width=3, height=1, bg="blue", bd=10, font=("Alrial", 12,"bold"))
bouton_sept.config(fg="white")
bouton_sept.place(x=105, y=390)
bouton_huit = tk.Button(canvas, text="8", command=lambda: affiche("8", '1000'), width=3, height=1, bg="blue", bd=10, font=("Alrial", 12,"bold"))
bouton_huit.config(fg="white")
bouton_huit.place(x=205, y=390)
bouton_neuf = tk.Button(canvas, text="9", command=lambda: affiche("9", '1000'), width=3, height=1, bg="blue", bd=10, font=("Alrial", 12,"bold"))
bouton_neuf.config(fg="white")
bouton_neuf.place(x=305, y=390)
bouton_multuple = tk.Button(canvas, text="X", command=lambda: affiche("*", '1000'), width=3, height=1, bd=10, font=("Alrial", 12,"bold"))
bouton_multuple.place(x=405, y=390)
                 # 5eme ligne des boutons
bouton_parfermer = tk.Button(canvas, text=")", command=lambda: affiche(")", '1000'), width=3, height=1, bd=10, font=("Alrial", 12,"bold"))
bouton_parfermer.place(x=20, y=460)
bouton_quatre = tk.Button(canvas, text="4", command=lambda: affiche("4", '1000'), width=3, height=1, bg="blue", bd=10, font=("Alrial", 12,"bold"))
bouton_quatre.config(fg="white")
bouton_quatre.place(x=105, y=460)
bouton_cinq = tk.Button(canvas, text="5", command=lambda: affiche("5", '1000'), width=3, height=1, bg="blue", bd=10, font=("Alrial", 12,"bold"))
bouton_cinq.config(fg="white")
bouton_cinq.place(x=205, y=460)
bouton_six = tk.Button(canvas, text="6", command=lambda: affiche("6", '1000'), width=3, height=1, bg="blue", bd=10, font=("Alrial", 12,"bold"))
bouton_six.config(fg="white")
bouton_six.place(x=305, y=460)
bouton_soustraction = tk.Button(canvas, text="-", command=lambda: affiche("-", '1000'), width=3, height=1, bd=10, font=("Alrial", 12,"bold"))
bouton_soustraction.place(x=405, y=460)
                 # 6eme ligne des boutons
bouton_delete_one = tk.Button(canvas, text="DEL", command=supprimer_one_one, width=3, height=1, bg="red", bd=10, font=("Alrial", 12,"bold"))
bouton_delete_one.config(fg="white")
bouton_delete_one.place(x=20, y=530)
bouton_un = tk.Button(canvas, text="1", command=lambda: affiche("1", '1000'), width=3, height=1, bg="blue", bd=10, font=("Alrial", 12,"bold"))
bouton_un.config(fg="white")
bouton_un.place(x=105, y=530)
bouton_deux = tk.Button(canvas, text="2", command=lambda: affiche("2", '1000'), width=3, height=1, bg="blue", bd=10, font=("Alrial", 12,"bold"))
bouton_deux.config(fg="white")
bouton_deux.place(x=205, y=530)
bouton_trois = tk.Button(canvas, text="3", command=lambda: affiche("3", '1000'), width=3, height=1,bg="blue", bd=10, font=("Alrial", 12,"bold"))
bouton_trois.config(fg="white")
bouton_trois.place(x=305, y=530)
bouton_addition = tk.Button(canvas, text="+", command=lambda: affiche("+", '100'), width=3, height=1, bd=10, font=("AAlrial", 12,"bold"))
bouton_addition.place(x=405, y=530)
                 # 7eme ligne des boutons
bouton_delete_all = tk.Button(canvas, text="AC", command=supprimer_all, width=3, height=1, bg="red", bd=10, font=("Alrial", 12,"bold"))
bouton_delete_all.config(fg="white")
bouton_delete_all.place(x=20, y=600)
bouton_zero = tk.Button(canvas, text="0", command=lambda: affiche("0", '1000'), width=3, height=1,bg="blue", bd=10, font=("Alrial", 12,"bold"))
bouton_zero.config(fg="white")
bouton_zero.place(x=105, y=600)
bouton_virgule = tk.Button(canvas, text=".", command=lambda: affiche(".", '1000'), width=3, height=1, bd=10, font=("Alrial", 12,"bold"))
bouton_virgule.place(x=205, y=600)
bouton_ans = tk.Button(canvas, text="Ans", command=lambda: affiche("Ans", '1000'), width=3, height=1, bd=10, font=("Alrial", 12,"bold"))
bouton_ans.place(x=305, y=600)
bouton_egale = tk.Button(canvas, text="=", bg="white", command=lambda :calculer(), width=3, height=1, bd=10, font=("Alrial", 12,"bold"))
bouton_egale.place(x=405, y=600)




root.mainloop()










