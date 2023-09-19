from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
import psycopg2
import subprocess
import os

root = Tk()
root.title("S'inscrire")
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)
icon_path = os.path.abspath("logo.ico")

global essai_no
essai_no=0
#Fonction nombre d'essai de connection
def essai():
    global essai_no
    
    essai_no+=1
    print("Essai_no",essai_no)
    if essai_no==3:
        messagebox.showwarning("Erreur","Vous avez atteint le limit d'essai")
        root.destroy()#maty

#fonction retourner se connecter
def return_login():
    connecter = messagebox.askyesno("Se connecter", "Etes vous sur de se connecter")
    if connecter >0:
        root.destroy()
        with open("login.py", encoding="utf-8") as f:
            exec(f.read())
    else:
        pass
#fonction principale login:
def signup():
    username=user.get()
    password=code.get()
    if (username =="" and password=="Mot de pass")or(username=="Nom d'utilisateur" and password==""):
        messagebox.showwarning(title="Erreur d'entrer", message="Veuillez entrer le Nom d'utilisateur et le Mot de Pass")
    else:
        try:
            conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="tsiory2003", port=5432)
            my_cursor = conn.cursor()
            print("Mandeha ny connection")
            
        except:
            messagebox.showerror("Connection","Erreur de connection à la base de donnée")
            return
        command="insert into accounts(nom,mot_de_pass) values (%s,%s)"
        my_cursor.execute(command,(username,password))
        my_cursor.execute("SELECT * FROM accounts")
        myresult = my_cursor.fetchall()
        print(myresult)
        conn.commit()
        conn.close()
        
        if myresult==None:
            messagebox.showinfo("Invalid","Nom d'Utilisateur et Mot de Pass Invalid")
            essai()
            
        else:
            messagebox.showinfo("info","Utilisateur ajouter")
            root.destroy()
            with open("login.py", encoding="utf-8") as f:
                exec(f.read())
            
    # if username=="tsiory" and password=="1234":
    #     root.destroy()
    #     with open("students.py", encoding="utf-8") as f:
    #         exec(f.read())

# Définir l'icône de la fenêtre
root.iconbitmap(icon_path)

# Charger l'image originale
img = Image.open("logo_p.png")

# Créer une nouvelle image blanche de la même taille que l'originale
white_img = Image.new('RGB', img.size, color='white')

# Coller l'image originale sur l'image blanche
white_img.paste(img, (0, 0), img)

# Redimensionner l'image
white_img = white_img.resize((390, 400), Image.LANCZOS)

# Convertir l'image PIL en PhotoImage de Tkinter
photo_img = ImageTk.PhotoImage(white_img)

# Créer un Label et afficher l'image
label = tk.Label(root, image=photo_img, bg="white", highlightthickness=0)#manala anle bordure le farany
label.place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading = Label(frame, text="S'inscrire", fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=90, y=1)

def on_enter(e):
    user.delete(0,'end')
    
def on_leave(e):
    name=user.get()
    if name=="":
        user.insert(0,"Nom d'utilisateur")
#########################################################
userlabel=Label(frame,text="Nom d'utilisateur",fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',14,'bold'))
userlabel.place(x=25,y=55)
user = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light',11))
user.place(x=30, y=100)
user.insert(0,"Entrer votre Nom d'utilisateur")
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=125)
################################################################
def on_enter(e):
    code.delete(0,'end')
    
def on_leave(e):
    name=code.get()
    if name=="":
        code.insert(0,"Mot de pass")
        
userlabel=Label(frame,text="Mot de pass",fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',14,'bold'))
userlabel.place(x=25,y=145)
code=Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft Yahei UI Light',11))
code.place(x=30,y=185)
code.insert(0,'Entrer votre mot de pass')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=208)

####
button_mode=True
def hide():
    global button_mode
    if button_mode:
        eyeButton.config(image=eyeclose,activebackground="white")
        code.config(show="*")
        button_mode=False
    else:
        eyeButton.config(image=openeye,activebackground="white")
        code.config(show="")
        button_mode=True

openeye = Image.open("open.png")
openeye = openeye.resize((25, 25), Image.LANCZOS)
openeye = ImageTk.PhotoImage(openeye)
eyeclose = Image.open("close.png")
eyeclose = eyeclose.resize((25, 25), Image.LANCZOS)
eyeclose = ImageTk.PhotoImage(eyeclose)
eyeButton = Button(frame, image=openeye, bg="white", bd=0,command=hide)
eyeButton.place(x=290,y=180)






###########################################################
Button(frame,width=39,height=2,fg='white',bg='#57a1f8',text="S'inscrire",command=signup,relief=RAISED,bd=1).place(x=25,y=240)
label=Label(frame,text="Vous avez déja une  compte?",fg="black",bg="white",
            font=('Microsoft Yahei UI Light',9))
label.place(x=25,y=300)

sinscrire=Button(frame,width=15,text="Se connecter",border=0,bg='white',cursor='hand2',fg='#57a1f8',command=return_login)
sinscrire.place(x=210,y=300)

root.mainloop()
