import tkinter as tk
import random

# Fenetre
root = tk.Tk()
root.geometry("600x600")
root.title('Ballon creation')

#Zone de  dessin
canvas = tk.Canvas(root, width= 500, height=500, bg='black')
canvas.pack(anchor=tk.CENTER ,expand=True)

#Amplacement aléatoir du ballon au début:
i = 0
x = random.randint(0, 500)
y = random.randint(0, 200)
rainbow = ['#ff0000', '#ff7f00', '#ffff00', '#7fff00', '#00ff00', '#00ff7f', '#00ffff', '#007fff', '#0000ff', '#7f00ff']
ov = canvas.create_oval((x, y), (x + 30, y+ 30), fill=rainbow[i])

#Fonction tirer le ballon et le ballon 1 disparait
def shoot():
    global  ov, i
    x = random.randint(0, 500)
    y = random.randint(0, 200)
    canvas.moveto(ov,x,y)
    canvas.itemconfigure(ov, fill=rainbow[i%10])
    i+=1


bouton1 = tk.Button(root, text='SHOOT',command=shoot)
bouton1.place(x=250, y=450)
bouton1.pack()

root.mainloop()