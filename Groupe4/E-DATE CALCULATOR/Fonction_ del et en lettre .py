# Fonction en lettre

"""import tkinter as tk

root = tk.Tk()
root.title("E-DATE Calculator®")

#creation fenetre
canvas = tk.Canvas(root, width=480, height=700, bg="black")
canvas.pack()

# Marque de la machine
texte = "E-DATE Calculator®"
position_x = 200
position_y = 30
canvas.create_text(position_x, position_y, text=texte, font=("Arial", 20), fill="white")

# creation d'ecran
ecran = tk.Text(canvas, width=41, height=3, font=("Algerian", 14), bg="olive", bd=5)
ecran.place(x=15, y=50)

def colorerTxt1(Text1):
    Text1.config(fg='blue')

bou1 = tk.Button(root,text='Colorer Y',command=colorerTxt1)
bou1.config(fg='red')
bou1.place(x=200, y=250)
root.mainloop() """

"""from math import *

premier = ["ZERO", "UN", "DEUX", "TROIS", "QUATRE", "CINQ", " SIX", "SEPT", "HUIT", "NEUF"]
deuxieme = ["DIX", "ONZE", "DOUZE", "TREIZE", "QUATORZE", "QUINZE", "SEIZE", "DIX-SEPT", "DIX-HUIT", "DIX-NEUF"]
troisieme = ["", "DIX", "VINGT", "TRENTE","QUARANTE","CINQUANTE"," SOIXANTE","SOIXANTE-DIX","QUATRE-VINGT","QUATRE-VINGT-DIX"]

def conversion(nombre):
    s= ""
    reste = nombre
    i = 1000000000
    while i > 0:
        y = reste/i
        if y != 0:
            centaine = y / 100
            dizaine = (y - centaine * 100) / 10
            unite = y - centaine * 100 - dizaine * 10
            if centaine == 1:
                s+= "CENT"
            elif centaine != 0:
                s += premier[centaine] + "CENT"
                if dizaine == 0 and unite == 0: s=s[:1]+ "S"
            if dizaine not in [0,1] : s += troisieme[dizaine]
            if unite == 0:
                if dizaine in [1,7,9] : s+= "DIX "
                elif dizaine == 8: s = s[:-1] + "S"
            elif unite == 1:
                if dizaine in [1,9] : s += "ONZE "
                elif dizaine == 7 : s+= "ET ONZE"
                if dizaine in [2,3,4,5,6]: s += "ET UN "
                if dizaine in [0, 8]: s += "UN "
            elif unite in [2,3,4,5,6,7,8,9]:
                if dizaine in [1,7,9]: s+= deuxieme[unite]
                else: s += premier[unite]
            if i == 1000000000:
                if y > 1:s+= "MILLIARDS"
                else: s+= "MILLIARD"
            if i == 100000000:
                if y > 1:
                    s += "MILLIONS"
                else:
                    s += "MILLION"
            if i ==1000:
                s += "MILLe"

            #end if y!=0
        reste -= y*i
        dix = False
        i /= 1000
    #end while
    if len(s) == 0: s +="ZERO"
    return s


#conversion(12)
print(conversion(12))"""

from num2words import num2words
#Install it by using pip install num2words
nombre = 3
n = 2000
texte = num2words(nombre,lang="fr").upper()
print(texte)
print(num2words(n, lang="fr").upper())

"""def numToWords:
    n=int(input("Entrez la somme:"))
    print(num2words(n))"""
