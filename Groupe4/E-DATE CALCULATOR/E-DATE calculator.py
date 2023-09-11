import tkinter as tk

def effacer():
    ecran.delete('1.0', tk.END)

# creation fenetre root
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

# creation des boutons
bouton_effacer = tk.Button(canvas, text="Effacer", command=effacer)
bouton_effacer.place(x=10, y=10)
                 # 1ere ligne des boutons
bouton_effacer = tk.Button(canvas, text="On", command=effacer, width=3, height=1, bd=10, font=("Algerian", 12,"bold"))
bouton_effacer.place(x=420, y=180)
bouton_effacer = tk.Button(canvas, text="Off", command=effacer, width=3, height=1, bd=10, font=("Algerian", 12,"bold"))
bouton_effacer.place(x=320, y=180)
                 # 2eme ligne des boutons
bouton_effacer = tk.Button(canvas, text="cos", command=effacer, width=3, height=1, bd=10, font=("Algerian", 12,"bold"))
bouton_effacer.place(x=20, y=250)
bouton_effacer = tk.Button(canvas, text="sin", command=effacer, width=3, height=1, bd=10, font=("Algerian", 12,"bold"))
bouton_effacer.place(x=120, y=250)
bouton_effacer = tk.Button(canvas, text="x²", command=effacer, width=3, height=1, bd=10, font=("Algerian", 12,"bold"))
bouton_effacer.place(x=220, y=250)
bouton_effacer = tk.Button(canvas, text="√", command=effacer, width=3, height=1, bd=10, font=("Algerian", 12,"bold"))
bouton_effacer.place(x=320, y=250)
bouton_effacer = tk.Button(canvas, text="x!", command=effacer, width=3, height=1, bd=10, font=("Algerian", 12,"bold"))
bouton_effacer.place(x=420, y=250)
                 # 3eme ligne des bouton
bouton_effacer = tk.Button(canvas, text="tan", command=effacer, width=3, height=1, bd=10, font=("Algerian", 12,"bold"))
bouton_effacer.place(x=20, y=320)
bouton_effacer = tk.Button(canvas, text="ln", command=effacer, width=3, height=1, bd=10, font=("Algerian", 12,"bold"))
bouton_effacer.place(x=120, y=320)
bouton_effacer = tk.Button(canvas, text="exp", command=effacer, width=3, height=1, bd=10, font=("Algerian", 12,"bold"))
bouton_effacer.place(x=220, y=320)
bouton_effacer = tk.Button(canvas, text="π", command=effacer, width=3, height=1, bd=10, font=("Algerian", 12,"bold"))
bouton_effacer.place(x=320, y=320)
bouton_effacer = tk.Button(canvas, text="%", command=effacer, width=3, height=1, bd=10, font=("Algerian", 12,"bold"))
bouton_effacer.place(x=420, y=320)
                 # 4eme ligne des boutons
bouton_effacer = tk.Button(canvas, text="(", command=effacer, width=3, height=1, bd=10, font=("Algerian", 12,"bold"))
bouton_effacer.place(x=20, y=390)
bouton_effacer = tk.Button(canvas, text="7", command=effacer, width=3, height=1, bg="blue", bd=10, font=("Algerian", 12,"bold"))
bouton_effacer.place(x=120, y=390)
bouton_effacer = tk.Button(canvas, text="8", command=effacer, width=3, height=1, bg="blue", bd=10, font=("Algerian", 12,"bold"))
bouton_effacer.place(x=220, y=390)
bouton_effacer = tk.Button(canvas, text="9", command=effacer, width=3, height=1, bg="blue", bd=10, font=("Algerian", 12,"bold"))
bouton_effacer.place(x=320, y=390)
bouton_effacer = tk.Button(canvas, text="X", command=effacer, width=3, height=1, bd=10, font=("Algerian", 12,"bold"))
bouton_effacer.place(x=420, y=390)
                 # 5eme ligne des boutons
bouton_effacer = tk.Button(canvas, text=")", command=effacer, width=3, height=1, bd=10, font=("Algerian", 12,"bold"))
bouton_effacer.place(x=20, y=460)
bouton_effacer = tk.Button(canvas, text="4", command=effacer, width=3, height=1, bg="blue", bd=10, font=("Algerian", 12,"bold"))
bouton_effacer.place(x=120, y=460)
bouton_effacer = tk.Button(canvas, text="5", command=effacer, width=3, height=1, bg="blue", bd=10, font=("Algerian", 12,"bold"))
bouton_effacer.place(x=220, y=460)
bouton_effacer = tk.Button(canvas, text="6", command=effacer, width=3, height=1, bg="blue", bd=10, font=("Algerian", 12,"bold"))
bouton_effacer.place(x=320, y=460)
bouton_effacer = tk.Button(canvas, text="-", command=effacer, width=3, height=1, bd=10, font=("Algerian", 12,"bold"))
bouton_effacer.place(x=420, y=460)
                 # 6eme ligne des boutons
bouton_effacer = tk.Button(canvas, text="DEL", command=effacer, width=3, height=1, bg="red", bd=10, font=("Algerian", 12,"bold"))
bouton_effacer.place(x=20, y=530)
bouton_effacer = tk.Button(canvas, text="1", command=effacer, width=3, height=1, bg="blue", bd=10, font=("Algerian", 12,"bold"))
bouton_effacer.place(x=120, y=530)
bouton_effacer = tk.Button(canvas, text="2", command=effacer, width=3, height=1, bg="blue", bd=10, font=("Algerian", 12,"bold"))
bouton_effacer.place(x=220, y=530)
bouton_effacer = tk.Button(canvas, text="3", command=effacer, width=3, height=1, bg="blue", bd=10, font=("Algerian", 12,"bold"))
bouton_effacer.place(x=320, y=530)
bouton_effacer = tk.Button(canvas, text="+", command=effacer, width=3, height=1, bd=10, font=("Algerian", 12,"bold"))
bouton_effacer.place(x=420, y=530)
                 # 7eme ligne des boutons
bouton_effacer = tk.Button(canvas, text="AC", command=effacer, width=3, height=1, bg="red", bd=10, font=("Algerian", 12,"bold"))
bouton_effacer.place(x=20, y=600)
bouton_effacer = tk.Button(canvas, text="0", command=effacer, width=3, height=1, bd=10, font=("Algerian", 12,"bold"))
bouton_effacer.place(x=120, y=600)
bouton_effacer = tk.Button(canvas, text=".", command=effacer, width=3, height=1, bd=10, font=("Algerian", 12,"bold"))
bouton_effacer.place(x=220, y=600)
bouton_effacer = tk.Button(canvas, text="Ans", command=effacer, width=3, height=1, bd=10, font=("Algerian", 12,"bold"))
bouton_effacer.place(x=320, y=600)
bouton_effacer = tk.Button(canvas, text="=", command=effacer, width=3, height=1, bd=10, font=("Algerian", 12,"bold"))
bouton_effacer.place(x=420, y=600)





root.mainloop()










