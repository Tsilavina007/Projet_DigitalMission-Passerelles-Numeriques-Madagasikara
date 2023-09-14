import tkinter as tk  # Importation du module tkinter pour créer une interface graphique
import math  # Importation du module math pour effectuer des opérations mathématiques
import tkinter.messagebox

calcul = ""  # Variable pour stocker les calculs en cours
historique = []  # Liste pour stocker l'historique des calculs
previous_result = 0.0

# Fonction pour afficher la fenêtre de l'historique
def afficher_historique():
    historique_window = tk.Toplevel(fenetre)  # Création d'une nouvelle fenêtre
    historique_window.title("Historique")  # Définition du titre de la fenêtre
    historique_window.geometry("300x400")  # Définition des dimensions de la fenêtre

    historique_text = tk.Text(historique_window, height=20, width=30,font=("Arial", 12))
    # Création d'un widget Text pour afficher le contenu de l'historique
    historique_text.pack(padx=10, pady=10)

    for item in historique:
        historique_text.insert("end", item + "\n")  # Insertion de chaque élément de l'historique dans le widget Text

# Fonction pour ajouter un calcul à l'historique
def ajouter_historique(expression, resultat):
    historique.append(expression + " = " + resultat)

def faire_le_calcul():
    global calcul, previous_result  # Déclare les variables "calcul" et "previous_result" comme variables globales
    try:
        calcul = calcul.replace("^", "**")  # Remplace "^" par "**" pour évaluer correctement l'exponentiation
        calcul = calcul.replace("pi", "math.pi")  # Remplace "pi" par "math.pi"
        calcul = calcul.replace("sqrt", "math.sqrt")  # Remplace "sqrt" par "math.sqrt"
        calcul = calcul.replace("cos", "math.cos")  # Remplace "cos" par "math.cos"
        calcul = calcul.replace("sin", "math.sin")  # Remplace "sin" par "math.sin"
        #calcul = calcul.replace("cosh", "math.cosh")  # Remplace "cosh" par "cmath.cosh"
        calcul = calcul.replace("tan", "math.tan")  # Remplace "tan" par "math.tan"
        calcul = calcul.replace("exp", "math.exp")  # Remplace "exp" par "math.exp"
        calcul = calcul.replace("log10", "math.log10")  # Remplace "log10" par "math.log10"
        calcul = calcul.replace("ln", "math.log")  # Remplace "ln" par "math.log"
        calcul = calcul.replace("acos", "acos")
        calcul = calcul.replace("amath.cos", "math.acos")
        calcul = calcul.replace("asin", "asin")  # Remplace "sin⁻¹" par "math.asin"
        calcul = calcul.replace("amath.sin", "math.asin")
        print (f"calcul : {calcul}")
        resultat = str(eval(calcul))  # Évalue l'expression arithmétique contenue dans la variable "calcul" et convertit le résultat en une chaîne de caractères
        ajouter_historique(calcul, resultat)  # Appelle une fonction "ajouter_historique" avec les arguments "calcul" et "resultat" pour enregistrer le calcul dans l'historique
        calcul = resultat  # Met à jour la variable "calcul" avec le résultat du calcul
        text_resultat.delete(1.0, "end")  # Efface le contenu du widget Text
        text_resultat.insert(1.0, calcul)  # Insère le résultat du calcul dans le widget Text
        previous_result = float(calcul)  # Met à jour la variable "previous_result" avec la valeur numérique du résultat du calcul (convertie en flottant)
    except:
        effacer()  # Appelle une fonction "effacer" pour effacer le calcul en cours
        text_resultat.insert(1.0, "Syntaxe Error")  # Affiche "Syntaxe Error" dans le widget Text si une erreur se produit lors de l'évaluation du calcul


def ajout_calcul(symbol):
    global calcul  # Déclare la variable "calcul" comme une variable globale

    if symbol == "cos":  # Si le symbole est "cos"
        calcul = calcul + "cos("  # Ajoute "cos(" à la variable "calcul"
    elif symbol == "sin":  # Sinon, si le symbole est "sin"
        calcul = calcul + "sin("  # Ajoute "sin(" à la variable "calcul"
    elif symbol == "sqrt":  # Sinon, si le symbole est "sqrt"
        calcul = calcul + "sqrt("  # Ajoute "sqrt(" à la variable "calcul"
    elif symbol == "**":  # Sinon, si le symbole est "**"
        calcul = calcul + "**"  # Ajoute "**" à la variable "calcul"
    elif symbol == "\u03C0":  # Sinon, si le symbole est le caractère unicode représentant "pi"
        calcul = calcul + "pi"  # Ajoute "pi" à la variable "calcul"
    elif symbol == "tan":  # Sinon, si le symbole est "tan"
        calcul = calcul + "tan("  # Ajoute "tan(" à la variable "calcul"
    elif symbol == "log10":  # Sinon, si le symbole est "log10"
        calcul = calcul + "log10("  # Ajoute "log10(" à la variable "calcul"
    elif symbol == "ln":  # Sinon, si le symbole est "ln"
        calcul = calcul + "ln("  # Ajoute "ln(" à la variable "calcul"
    elif symbol == "asin":  # Sinon, si le symbole est "sin⁻¹"
        calcul = calcul + "asin"  # Ajoute "asin(" à la variable "calcul"
    elif symbol == "acos":  # Sinon, si le symbole est "cosh"
        calcul = calcul + "acos"  # Ajoute "cosh(" à la variable "calcul"
    elif symbol == "Ans":  # Sinon, si le symbole est "Ans"
        calcul = calcul + str(previous_result)  # Ajoute la valeur précédente du résultat à la variable "calcul"

    else:  # Sinon (aucune des conditions précédentes n'est satisfaite)
        calcul = calcul + str(symbol)  # Ajoute le symbole (converti en chaîne de caractères) à la variable "calcul"

    text_resultat.delete(1.0, "end")  # Supprime le contenu actuel de la zone de texte "text_resultat"
    text_resultat.insert(1.0, calcul)  # Insère le contenu de la variable "calcul" à la position 1.0 dans la zone de texte "text_resultat"



# Fonction pour calculer la moyenne
def moyenne():
    global calcul
    nums = [float(num) for num in calcul.split(",")]  # Sépare les nombres du calcul et les convertit en flottants
    avg = sum(nums) / len(nums)  # Calcule la moyenne des nombres
    calcul = str(avg)  # Convertit la moyenne en chaîne de caractères
    text_resultat.delete(1.0, "end")  # Efface le contenu du widget Text
    text_resultat.insert(1.0, calcul)  # Insère la moyenne dans le widget Text

# Fonction pour calculer la factorielle
def factorielle():
    global calcul
    num = int(calcul)  # Convertit le nombre du calcul en entier
    fact = 1
    for i in range(1, num + 1):
        fact *= i  # Calcule la factorielle
    calcul = str(fact)  # Convertit la factorielle en chaîne de caractères
    text_resultat.delete(1.0, "end")  # Efface le contenu du widget Text
    text_resultat.insert(1.0, calcul)  # Insère la factorielle dans le widget Text

# Fonction pour effacer le calcul en cours
def effacer():
    global calcul  # Déclare la variable "calcul" comme une variable globale
    calcul = ""  # Réinitialise la variable "calcul" en une chaîne de caractères vide
    text_resultat.delete(1.0, "end")  # Efface le contenu du widget Text à partir de la position 1.0 jusqu'à la fin
   
def effacer_un():
    global calcul  # Déclare la variable "calcul" comme une variable globale
    text_resultat.delete("end-2c")  # Efface les deux derniers caractères du widget Text
    calcul = text_resultat.get("1.0", "end-1c")  # Récupère le contenu du widget Text de la position 1.0 jusqu'au caractère avant la fin
   
def iExit():
    iExit = tkinter.messagebox.askyesno("Scientific Calculator", "Do you want to exit ?")
    # Affiche une boîte de dialogue avec la question "Do you want to exit ?" et les boutons "Yes" et "No"
    if iExit > 0:  # Si l'utilisateur clique sur "Yes"
        fenetre.destroy()  # Détruit la fenêtre principale de l'application
        return  # Quitte la fonction iExit()



fenetre = tk.Tk()  # Création de la fenêtre principale
fenetre.geometry("330x665")  # Définition des dimensions de la fenêtre
fenetre.configure(background='black')

fenetre.resizable(width = False, height = False)#////////////////////////////////////////

menu_bar = tk.Menu(fenetre)  # Création d'une barre de menu
fenetre.config(menu=menu_bar)  # Configuration de la fenêtre pour utiliser cette barre de menu

menu_file = tk.Menu(menu_bar, tearoff = 0)
menu_bar.add_cascade(label="File", menu = menu_file)
menu_file.add_command(label = "Exit", command = iExit)

menu_historique = tk.Menu(menu_bar, tearoff=0)  # Création d'un menu déroulant pour l'historique
menu_bar.add_cascade(label="Historique", menu=menu_historique)  # Ajout du menu déroulant à la barre de menu
menu_historique.add_command(label="Afficher", command=afficher_historique)  # Ajout d'une option pour afficher l'historique


label_titre = tk.Label(fenetre, text="Calculatrice", font=("Arial", 16), bg='black', fg='white')
label_titre.grid(row=0, columnspan=5, pady=10)

# ...
text_resultat = tk.Text(fenetre, height=1.5, width=17, bg="green", font=("Arial", 24))
text_resultat.grid(row=1, column=0, columnspan=5, pady=20, padx=10, sticky="se")

btn_1 = tk.Button(fenetre, text = "1",bd=5,relief="raised",bg="gray" ,command = lambda:ajout_calcul(1), width = 5, font=("Arial", 14))
btn_1.grid(row = 2,column = 0, pady = 5, padx = 5) # row = 1 est prise par l'ecran alors 2
# lambda : collecter la variable 1 et l'ajouter dans command


btn_2 = tk.Button(fenetre, text="2",bd=5,relief="raised", bg="gray" , command=lambda: ajout_calcul(2), width=5, font=("Arial", 14))
# Crée un bouton dans la fenêtre 'fenetre' avec le texte "2"
# Lorsque le bouton est cliqué, la fonction lambda est exécutée, qui appelle la fonction 'ajout_calcul' avec l'argument 2
# La largeur du bouton est définie sur 5 et la police de caractères utilisée est Arial avec une taille de 14

btn_2.grid(row=2, column=1, padx=5)
# Place le bouton dans la fenêtre en utilisant la méthode grid (positionnement en grille)
# Le bouton est positionné à la 2ème ligne



btn_3 = tk.Button(fenetre, text = "3", bd=5,relief="raised", bg="gray" ,command = lambda:ajout_calcul(3), width = 5, font=("Arial", 14))
btn_3.grid(row = 2,column = 2, padx = 5)


btn_som = tk.Button(fenetre, text = "+",bd=5,relief="raised", bg="silver" ,command = lambda:ajout_calcul("+"), width = 5, font=("Arial", 14))
btn_som.grid(row = 2,column = 3, padx = 5)


# deuxième ligne de boutton
btn_4 = tk.Button(fenetre, text = "4", bd=5,relief="raised",bg="gray" , command = lambda:ajout_calcul(4), width = 5, font=("Arial", 14))
btn_4.grid(row = 3,column = 0, pady = 5, padx = 5)

btn_5 = tk.Button(fenetre, text = "5",bd=5,relief="raised", bg="gray" , command = lambda:ajout_calcul(5), width = 5, font=("Arial", 14))
btn_5.grid(row = 3,column = 1, padx = 5)

btn_6 = tk.Button(fenetre, text = "6", bd=5,relief="raised", bg="gray" ,command = lambda:ajout_calcul(6), width = 5, font=("Arial", 14))
btn_6.grid(row = 3,column = 2, padx = 5)


btn_sous = tk.Button(fenetre, text = "-",bd=5,relief="raised", bg="silver" ,  command = lambda:ajout_calcul("-"), width = 5, font=("Arial", 14))
btn_sous.grid(row = 3,column = 3, padx = 5)

# troisième ligne de boutton
btn_7 = tk.Button(fenetre, text = "7",bd=5,relief="raised", bg="gray" , command = lambda:ajout_calcul(7), width = 5, font=("Arial", 14))
btn_7.grid(row = 4,column = 0, pady = 5, padx = 5)

btn_8 = tk.Button(fenetre, text = "8",bd=5,relief="raised", bg="gray" , command = lambda:ajout_calcul(8), width = 5, font=("Arial", 14))
btn_8.grid(row = 4,column = 1, padx = 5)

btn_9 = tk.Button(fenetre, text = "9",bd=5,relief="raised", bg="gray" , command = lambda:ajout_calcul(9), width = 5, font=("Arial", 14))
btn_9.grid(row = 4,column = 2, padx = 5)

btn_multi = tk.Button(fenetre, text = "x", bd=5,relief="raised",  bg="silver" ,command = lambda:ajout_calcul("*"), width = 5, font=("Arial", 14))
btn_multi.grid(row = 4,column = 3, padx = 5)


# quatrième ligne de boutton
btn_0 = tk.Button(fenetre, text = "0",bd=5,relief="raised", bg="gray" , command = lambda:ajout_calcul(0), width = 5, font=("Arial", 14))
btn_0.grid(row = 5,column = 1, pady = 5, padx = 5)

btn_open = tk.Button(fenetre, text = "(",bd=5,relief="raised",  bg="silver" , command = lambda:ajout_calcul("("), width = 5, font=("Arial", 14))
btn_open.grid(row = 5,column = 0, padx = 5)

btn_close = tk.Button(fenetre, text = ")",bd=5,relief="raised",  bg="silver" , command = lambda:ajout_calcul(")"), width = 5, font=("Arial", 14))
btn_close.grid(row = 5,column = 2, padx = 5)

btn_div = tk.Button(fenetre, text = "/",bd=5,relief="raised",  bg="silver" , command = lambda:ajout_calcul("/"), width = 5, font=("Arial", 14))
btn_div.grid(row = 5,column = 3, padx = 5)


#cinquième ligne de boutton

btn_eff = tk.Button(fenetre, text = "Effacer", bd=5,relief="raised", command = effacer,bg="red",width = 5, font=("Arial", 8))
btn_eff.grid(row = 6,column = 2, pady = 5, padx = 5, ipadx = 10, ipady = 7)

btn_effacer = tk.Button(fenetre, text = "C",bd=5,relief="raised",  command = effacer_un, width = 5,bg="red", font=("Arial", 14))
btn_effacer.grid(row = 6, column = 3, padx = 5)

btn_virg = tk.Button(fenetre, text = ".",bd=5,relief="raised",  bg="silver" , command = lambda:ajout_calcul("."), width = 5, font=("Arial", 14))
btn_virg.grid(row = 6,column = 0, padx = 5)

btn_mod = tk.Button(fenetre, text = "Mod",bd=5,relief="raised",  bg="silver" , command = lambda:ajout_calcul("%"), width = 5, font=("Arial", 14))
btn_mod.grid(row = 6,column = 1, padx = 5)

#sixième ligne de boutton
# Ajout des boutons pour les fonctions mathématiques
btn_cos = tk.Button(fenetre, text="cos",bd=5,relief="raised",  bg="silver" , command=lambda: ajout_calcul("cos"), width=5, font=("Arial", 14))
btn_cos.grid(row=7, column=0, pady = 5, padx = 5)

btn_sin = tk.Button(fenetre, text="sin", bd=5,relief="raised", bg="silver" , command=lambda: ajout_calcul("sin("), width=5, font=("Arial", 14))
btn_sin.grid(row=7, column=1, padx = 5)



btn_tan = tk.Button(fenetre, text="tan",bd=5,relief="raised",  bg="silver" , command=lambda: ajout_calcul("tan"), width=5, font=("Arial", 14))
btn_tan.grid(row=7, column=2, padx = 5)

btn_fact = tk.Button(fenetre, text="!", bd=5,relief="raised", bg="silver" , command=factorielle, width=5, font=("Arial", 14))
btn_fact.grid(row=7, column=3, padx = 5)


# septième ligne de boutton


btn_ln = tk.Button(fenetre, text="ln", bd=5,relief="raised", bg="silver" , command=lambda: ajout_calcul("ln"), width=5, font=("Arial", 14))
btn_ln.grid(row=8, column=2, padx = 5)

btn_log = tk.Button(fenetre, text="log",bd=5,relief="raised",  bg="silver" , command=lambda: ajout_calcul("log10"), width=5, font=("Arial", 14))
btn_log.grid(row=8, column=3, padx = 5)


btn_cosh = tk.Button(fenetre, text="cos⁻¹", bd=5,relief="raised", bg="silver" , command=lambda: ajout_calcul("acos("), width=5, font=("Arial", 14))
btn_cosh.grid(row=8, column=1, pady = 5)

btn_asin = tk.Button(fenetre, text="sin⁻¹", bd=5,relief="raised",  bg="silver" ,command=lambda: ajout_calcul("asin("), width=5, font=("Arial", 14))
btn_asin.grid(row=8, column=0, padx=5)


# huitième ligne de boutton

btn_puissance = tk.Button(fenetre, text="^",bd=5,relief="raised",  bg="silver" , command=lambda: ajout_calcul("**"), width=5, font=("Arial", 14))
btn_puissance.grid(row=9, column=1, padx = 5)

btn_exponentielle = tk.Button(fenetre, text = "e", bd=5,relief="raised", bg="silver" , command = lambda: ajout_calcul("exp"), width = 5, font = ("Arial", 14))
btn_exponentielle.grid(row = 9, column = 2, padx = 5)


#neuvième ligne de boutton
btn_pi = tk.Button(fenetre, text = "\u03C0",bd=5,relief="raised",  bg="silver" , command = lambda: ajout_calcul("pi"), width = 5, font = ("Arial", 14))
btn_pi.grid(row = 9, column = 3, pady = 4, padx = 5)

btn_sqrt = tk.Button(fenetre, text="√",bd=5,relief="raised",  bg="silver" , command=lambda: ajout_calcul("sqrt"), width=5, font=("Arial", 14))
btn_sqrt.grid(row=9, column=0, pady = 5, padx = 5)


btn_carré = tk.Button(fenetre, text = "x²",bd=5,relief="raised",  bg="silver" , command = lambda: ajout_calcul("**2"), width = 5, font=("Arial", 14))
btn_carré.grid(row = 9, column = 2, padx = 5)


btn_cube = tk.Button(fenetre, text = "x^3", bd=5,relief="raised", bg="silver" , command = lambda: ajout_calcul("**3"), width = 5, font=("Arial", 14))
btn_cube.grid(row = 9, column = 1, padx = 5)


# dixieme ligne


btn_egal = tk.Button(fenetre, text = "=",bd=5,relief="raised", bg="yellow" ,command = faire_le_calcul, width = 5, font=("Arial", 14))
btn_egal.grid(row = 10,column = 3, padx = 5)

btn_exponentielle = tk.Button(fenetre, text = "e", command = lambda: ajout_calcul("exp"), width = 5,bd=5,relief="raised", bg="silver", font = ("Arial", 14))
btn_exponentielle.grid(row = 10, column = 0, padx = 6)


btn_puissance = tk.Button(fenetre, text="^", command=lambda: ajout_calcul("**"),bd=5,relief="raised", bg="silver", width=5, font=("Arial", 14))
btn_puissance.grid(row=10, column=1, padx = 6)


btn_ans = tk.Button(fenetre, text= "Ans", bd=5,relief="raised", bg="yellow" , command = lambda: ajout_calcul("Ans"), width = 5, font = ("Arial", 14))
btn_ans.grid(row = 10, column = 2, pady = 5, padx = 5)

fenetre.mainloop()


