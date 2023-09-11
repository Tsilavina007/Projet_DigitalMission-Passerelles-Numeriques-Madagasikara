# Bibliothes
import tkinter as tk
from math import *
from num2words import num2words
import math

#The fonction
                    # " pi "
def calculer_pi():
    e_date = En_num.get()
    ed = int(e_date)
    result = math.pi * float(ed)
    En_num.delete(0, tk.END)
    En_num.insert(tk.END, str(result))
    date = num2words(result, lang='fr')
    En_lettre.delete(tk.END)
    En_lettre.insert(tk.END, date)

                    #Convertir en lettre
def convertir_en_lettre(nombre):
    resultat_en_lettres = num2words(nombre, lang='fr')
    return resultat_en_lettres

                    # Racine carre
def calculer_carre(self):
    try:
        nombre = float(self.En_num.get())
        resultat = calculer_carre(nombre)
        self.En_lettre.delete(0, tk.END)
        self.En_lettre.insert(tk.END, str(resultat))
    except ValueError:
        # Gérer une entrée invalide (par exemple, non numérique)
        self.En_lettre.delete(0, tk.END)
        self.En_lettre.insert(tk.END, "Erreur")

                    # Fonction "factorielle"
def calculer_factorielle():
    e_date = En_num.get()
    ed = int(e_date)
    result = math.factorial(ed)
    En_num.delete(0, tk.END)
    En_num.insert(tk.END, str(result))
    date = num2words(result, lang='fr')
    En_lettre.delete(0.1, tk.END)
    En_lettre.insert(tk.END,str(date))

                    # Fonction "exponentielle"
def calculer_exponentielle():
    e_date = En_num.get()
    ed = int(e_date)
    result = math.exp(float(ed))
    En_num.delete(0, tk.END)
    En_num.insert(tk.END, str(result))
    date = num2words(result, lang='fr')
    En_lettre.delete(0.1, tk.END)
    En_lettre.insert(tk.END,str(date))

                    # Fonction "longarithme"
def calculer_logarithme():
    e_date = En_num.get()
    ed = int(e_date)
    result = math.log(float(ed))
    En_num.delete(0, tk.END)
    En_num.insert(tk.END, str(result))
    date = num2words(result, lang='fr')
    En_lettre.delete(0.1, tk.END)
    En_lettre.insert(tk.END,str(date))

# Bouton "Ans"
global ans
ans = ""
def recallAns():
    global ans
    En_num.delete(0, tk.END)
    En_num.insert(0, ans)

# The scrole
# Up
def scroll_up():
    En_lettre.yview_scroll(-1, "units")
# Down
def scroll_down():
    En_lettre.yview_scroll(1, "units")

# The On/Off
bouton_etat = False
def change_etat():
    global bouton_etat
    if bouton_etat == True:
        bouton_etat = False
    else:
        bouton_etat = True
def etat_change():
    bouton_list=[bouton_scroll_down,bouton_scroll_up,bouton_cos,bouton_sin,bouton_sqrt,bouton_racine,bouton_factorielle,bouton_tan,bouton_ln,bouton_exp,bouton_puit,bouton_division,bouton_parouver,bouton_sept,bouton_huit,bouton_neuf,bouton_multuple,bouton_parfermer,bouton_quatre,bouton_cinq,bouton_six,bouton_soustraction,bouton_delete_one,bouton_un, bouton_deux,bouton_trois, bouton_addition, bouton_delete_all,bouton_zero,bouton_virgule,bouton_ans,bouton_egale]
    if bouton_etat==True:
        for x in range(0,32):
            bouton_list[x].config(state='normal')
    else:
        for x in range(0,32):
            bouton_list[x].config(state='disable')

# Relation des deux ecrans
def calculate_and_display():
# Récupérer la valeur de l'entrée
    e_date = En_num.get()

# Effectuer le calcul
    result = eval(e_date)
# Afficher le résultat dans l'écran numérique
    En_num.delete(0, tk.END)
    En_num.insert(0, str(result))
# Convertir le résultat en lettres
    result_in_words = convertir_en_lettre(result)
# Afficher le résultat dans l'écran de texte
    En_lettre.delete("1.0", tk.END)
    En_lettre.insert(tk.END, result_in_words)

# Affichage sur l'ecran
def affiche(chiffre, index):
    En_num.insert(index, chiffre)

# Calcul
def calculer():
 #Recuperation le valeur sur l'ecran
    calcul = En_num.get()
 #Essayer de calcul de la resultat et afficher
    try:
        global ans
        resultat = eval(calcul)
        ans = resultat
        En_num.delete(0, tk.END)
        En_num.insert(0, resultat)
    except:
        En_num.delete(0, tk.END)
        En_num.insert(0, "Error")

# The delete
def supprimer_one_one():
# Ecran principal/ delete one by one bouton (DEL)
    current_text = En_num.get()
    nouveau_texte = current_text[:-1]
    En_num.delete(0, tk.END)
    En_num.insert(tk.END, nouveau_texte)
def supprimer_all():
# Ecran principal/ delete all bouton (AC)
    current_text = En_num.get()
    nouveau_texte = current_text[:0]
    En_num.delete(0, tk.END)
    En_num.insert(tk.END, nouveau_texte)

                        # The body
                        # creation fenetre root

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
position_x = 260
position_y = 35
canvas.create_text(position_x, position_y, text=texte, font=("Arial", 20,"bold"), fill="white")

                    # Text top ecran " En_lettre "
texte = "The result in letter"
position_x = 130
position_y = 140
canvas.create_text(position_x, position_y, text=texte, font=("Arial", 12,"bold"), fill="blue")

                        # creation d'ecran
# 1er ecran
En_num = tk.Entry(canvas, width=22, font=("digital-7", 30, "bold"), bg="olive", bd=10)
En_num.place(x=22, y=50, height=80)

                            # 2eme ecran
En_lettre = tk.Text(canvas, width=18, font=("Arial", 16, "bold"), bg="olive", bd=10)
En_lettre.place(x=22, y=150, height=80)

                    # creation des boutons
                 # 1ere ligne des boutons
bouton_On_Off = tk.Button(canvas, text="On/Off", command=lambda: [change_etat(), etat_change(),supprimer_all()],width=5, height=1, bg="lime",bd=10, font=("Arial", 12,"bold", ))
bouton_On_Off.config(fg="red")
bouton_On_Off.place(x=385, y=165)

            # Créez les boutons pour le Up/Down
bouton_scroll_up = tk.Button(canvas, text="▲", command=scroll_up, width=1, height=0, bd=10,bg="grey", font=("Arial", 7, "bold"))
bouton_scroll_up.place(x=265, y=150)
bouton_scroll_down = tk.Button(canvas, text="▼", command=scroll_down, width=1, height=0, bd=10, bg="grey", font=("Arial", 7, "bold"))
bouton_scroll_down.place(x=265, y=195)
                 # 2eme ligne des boutons
bouton_cos = tk.Button(canvas, text="cos", command=lambda:  affiche("cos (", '1000'), width=3, height=1, bd=10, font=("Arial", 12,"bold"))
bouton_cos.place(x=20, y=260)
bouton_sin = tk.Button(canvas, text="sin", command=lambda:  affiche("sin (", '1000'), width=3, height=1, bd=10, font=("Arial", 12,"bold"))
bouton_sin.place(x=105, y=260)
bouton_sqrt = tk.Button(canvas, text="x²", command=lambda:  affiche("**", "1000"), width=3, height=1, bd=10, font=("Arial", 12,"bold"))
bouton_sqrt.place(x=205, y=260)
bouton_racine = tk.Button(canvas, text="√", command=lambda: affiche("sqrt(", '1000'), width=3, height=1, bd=10, font=("Arial", 12,"bold"))
bouton_racine.place(x=305, y=260)
bouton_factorielle = tk.Button(canvas, text="x!", command=lambda: calculer_factorielle(), width=3, height=1, bd=10, font=("Arial", 12,"bold"))
bouton_factorielle.place(x=405, y=260)

                 # 3eme ligne des bouton
bouton_tan = tk.Button(canvas, text="tan", command=lambda: affiche("tan(", '1000'), width=3, height=1, bd=10, font=("Alrial", 12,"bold"))
bouton_tan.place(x=20, y=330)
bouton_ln = tk.Button(canvas, text="ln", command=lambda: calculer_logarithme(), width=3, height=1, bd=10, font=("Alrial", 12,"bold"))
bouton_ln.place(x=105, y=330)
bouton_exp = tk.Button(canvas, text="exp", command=lambda: calculer_exponentielle(), width=3, height=1, bd=10, font=("Alrial", 12,"bold"))
bouton_exp.place(x=205, y=330)
bouton_puit = tk.Button(canvas, text="π", command=lambda: calculer_pi(), width=3, height=1, bd=10, font=("Alrial", 12,"bold"))
bouton_puit.place(x=305, y=330)
bouton_division = tk.Button(canvas, text="/", command=lambda: affiche("/", '1000'), width=3, height=1, bd=10, font=("Alrial", 12,"bold"))
bouton_division.place(x=405, y=330)

                 # 4eme ligne des boutons
bouton_parouver = tk.Button(canvas, text="(", command=lambda: affiche("(", '1000'), width=3, height=1, bd=10, font=("Alrial", 12,"bold"))
bouton_parouver.place(x=20, y=400)
bouton_sept = tk.Button(canvas, text="7", command=lambda: affiche("7", '1000'), width=3, height=1, bg="blue", bd=10, font=("Alrial", 12,"bold"))
bouton_sept.config(fg="white")
bouton_sept.place(x=105, y=400)
bouton_huit = tk.Button(canvas, text="8", command=lambda: affiche("8", '1000'), width=3, height=1, bg="blue", bd=10, font=("Alrial", 12,"bold"))
bouton_huit.config(fg="white")
bouton_huit.place(x=205, y=400)
bouton_neuf = tk.Button(canvas, text="9", command=lambda: affiche("9", '1000'), width=3, height=1, bg="blue", bd=10, font=("Alrial", 12,"bold"))
bouton_neuf.config(fg="white")
bouton_neuf.place(x=305, y=400)
bouton_multuple = tk.Button(canvas, text="X", command=lambda: affiche("*", '1000'), width=3, height=1, bd=10, font=("Alrial", 12,"bold"))
bouton_multuple.place(x=405, y=400)

                 # 5eme ligne des boutons
bouton_parfermer = tk.Button(canvas, text=")", command=lambda: affiche(")", '1000'), width=3, height=1, bd=10, font=("Alrial", 12,"bold"))
bouton_parfermer.place(x=20, y=470)
bouton_quatre = tk.Button(canvas, text="4", command=lambda: affiche("4", '1000'), width=3, height=1, bg="blue", bd=10, font=("Alrial", 12,"bold"))
bouton_quatre.config(fg="white")
bouton_quatre.place(x=105, y=470)
bouton_cinq = tk.Button(canvas, text="5", command=lambda: affiche("5", '1000'), width=3, height=1, bg="blue", bd=10, font=("Alrial", 12,"bold"))
bouton_cinq.config(fg="white")
bouton_cinq.place(x=205, y=470)
bouton_six = tk.Button(canvas, text="6", command=lambda: affiche("6", '1000'), width=3, height=1, bg="blue", bd=10, font=("Alrial", 12,"bold"))
bouton_six.config(fg="white")
bouton_six.place(x=305, y=470)
bouton_soustraction = tk.Button(canvas, text="-", command=lambda: affiche("-", '1000'), width=3, height=1, bd=10, font=("Alrial", 12,"bold"))
bouton_soustraction.place(x=405, y=470)

                 # 6eme ligne des boutons
bouton_delete_one = tk.Button(canvas, text="DEL", command=supprimer_one_one, width=3, height=1, bg="red", bd=10, font=("Alrial", 12,"bold"))
bouton_delete_one.config(fg="white")
bouton_delete_one.place(x=20, y=540)
bouton_un = tk.Button(canvas, text="1", command=lambda: affiche("1", '1000'), width=3, height=1, bg="blue", bd=10, font=("Alrial", 12,"bold"))
bouton_un.config(fg="white")
bouton_un.place(x=105, y=540)
bouton_deux = tk.Button(canvas, text="2", command=lambda: affiche("2", '1000'), width=3, height=1, bg="blue", bd=10, font=("Alrial", 12,"bold"))
bouton_deux.config(fg="white")
bouton_deux.place(x=205, y=540)
bouton_trois = tk.Button(canvas, text="3", command=lambda: affiche("3", '1000'), width=3, height=1,bg="blue", bd=10, font=("Alrial", 12,"bold"))
bouton_trois.config(fg="white")
bouton_trois.place(x=305, y=540)
bouton_addition = tk.Button(canvas, text="+", command=lambda: affiche("+", '1000'), width=3, height=1, bd=10, font=("AAlrial", 12,"bold"))
bouton_addition.place(x=405, y=540)

                 # 7eme ligne des boutons
bouton_delete_all = tk.Button(canvas, text="AC", command=supprimer_all, width=3, height=1, bg="red", bd=10, font=("Alrial", 12,"bold"))
bouton_delete_all.config(fg="white")
bouton_delete_all.place(x=20, y=610)
bouton_zero = tk.Button(canvas, text="0", command=lambda: affiche("0", '1000'), width=3, height=1,bg="blue", bd=10, font=("Alrial", 12,"bold"))
bouton_zero.config(fg="white")
bouton_zero.place(x=105, y=610)
bouton_virgule = tk.Button(canvas, text=".", command=lambda: affiche(".", '1000'), width=3, height=1, bd=10, font=("Alrial", 12,"bold"))
bouton_virgule.place(x=205, y=610)
bouton_ans = tk.Button(canvas, text="Ans", command=lambda: recallAns(), width=3, height=1, bd=10, font=("Alrial", 12,"bold"))
bouton_ans.place(x=305, y=610)
bouton_egale = tk.Button(canvas, text="=", command=lambda: [calculer(), calculate_and_display()], width=3, height=1, bd=10,bg="white", font=("Arial", 12, "bold"))
bouton_egale.place(x=405, y=610)

root.mainloop()
