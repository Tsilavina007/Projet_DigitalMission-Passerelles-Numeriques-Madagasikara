import tkinter as tk
import tkinter.messagebox
from tkinter.tix import COLUMN
import customtkinter
import pygame

#fonction son
def main_song():
    # Charger le fichier audio
    sound = pygame.mixer.Sound("./images/jazz2.mp3")
    #son
    sound.set_volume(0.1)
    # Jouer le fichier audio sur le deuxième canal
    channel.play(sound)
def success_song():
    # Charger le fichier audio
    sound = pygame.mixer.Sound("./images/success.mp3")

    # Jouer le fichier audio sur le deuxième canal
    channel1.play(sound)
def decide_song():
    # Charger le fichier audio
    sound = pygame.mixer.Sound("./images/decide.mp3")

    # Jouer le fichier audio sur le deuxième canal
    channel2.play(sound)

window=tk.Tk()
window.title('Morpion')
window.geometry("400x500")
frame=tk.Frame(master=window)
frame.pack(pady=10)
#son
pygame.mixer.init()
channel = pygame.mixer.Channel(0)
channel1 = pygame.mixer.Channel(1)
channel2 = pygame.mixer.Channel(2)
main_song()
label=tk.Label(master=frame,text="MORPION",font=("Arial", 15))
label.pack()

main_font = customtkinter.CTkFont(family="Helvetica", size=12)
params = {
    'font' : main_font,
    'text_color' : "black",
    'hover' : True,
    'hover_color' : "#68aec9",
    'height' : 60,
    'width' : 60,
    'border_width' : 1,
    'corner_radius' : 10,
    'border_color' : "#68aec9",
    'bg_color' : "#dadec3",
    'fg_color' : "white"
    }

frame1=tk.Frame(master=window,borderwidth=2,relief=tk.SUNKEN,bg='#dadec3')
frame1.pack(padx=10,pady=10)

button1=customtkinter.CTkButton(master=frame1,**params,text="",command=lambda : buttonclick(1))
button1.grid(row=0,column=0,padx=5,pady=5)

button2=customtkinter.CTkButton(master=frame1,text="",**params,command=lambda : buttonclick(2))
button2.grid(row=0,column=1,padx=5,pady=5)

button3=customtkinter.CTkButton(master=frame1,text="",**params,command=lambda : buttonclick(3))
button3.grid(row=0,column=2,padx=5,pady=5)

button4=customtkinter.CTkButton(master=frame1,text="",**params,command=lambda : buttonclick(4))
button4.grid(row=1,column=0,padx=5,pady=5)

button5=customtkinter.CTkButton(master=frame1,text="",**params,command=lambda : buttonclick(5))
button5.grid(row=1,column=1,padx=5,pady=5)

button6=customtkinter.CTkButton(master=frame1,text="",**params,command=lambda : buttonclick(6))
button6.grid(row=1,column=2,padx=5,pady=5)

button7=customtkinter.CTkButton(master=frame1,text="",**params,command=lambda : buttonclick(7))
button7.grid(row=2,column=0,padx=5,pady=5)

button8=customtkinter.CTkButton(master=frame1,text="",**params,command=lambda : buttonclick(8))
button8.grid(row=2,column=1,padx=5,pady=5)

button9=customtkinter.CTkButton(master=frame1,text="",**params,command=lambda : buttonclick(9))
button9.grid(row=2,column=2,padx=5,pady=5)

frame2=tk.Frame(master=window,border=2,relief=tk.SUNKEN,bg='#dadec3')
frame2.pack()
label1=tk.Label(master=frame2,text="Joueur 1 --> X\nJoueur 2 --> O",width=10)
label1.grid(row=0,column=0,padx=5)
button_restart=tk.Button(master=frame2,text="Restart",width=10,height=3,relief=tk.GROOVE,command=lambda: restart_button())
button_restart.grid(row=0,column=1,padx=10,pady=10)
label2=tk.Label(master=frame2,text='Tour Joueur-1',bg="skyblue",width=10,height=3,relief=tk.SUNKEN)
label2.grid(row=0,column=2,padx=5)

def disable_buttons():
    for button in buttons:
        button['state'] = tk.DISABLED
buttons = [button1, button2, button3, button4, button5, button6, button7, button8, button9]

def restart_button():
    global a, b, c
    a = 1
    b = 0
    c = 0
    label2['bg'] = "skyblue"
    label2['text'] = 'Tour Joueur-1 '
    for button in buttons:
        button.configure(text='')
        button.configure(fg_color='white')
        button.configure(border_color='#68aec9')
        button['state'] = tk.NORMAL
a = 1
b = 0
c = 0
def buttonclick(x):
    global a, b, c
    decide_song()
    button = buttons[x-1]
    if button.cget('text') == "":
        player = 'X' if a == 1 else 'O'
        button.configure(text=str(player))
        button.configure(fg_color='skyblue')  if player == 'X' else  button.configure(fg_color='#e8956f') 
        button.configure(border_color = '#68aec9')   if player == 'X' else button.configure(border_color = '#e8956f')
        label2['bg'] = '#e8956f' if player == 'X' else 'skyblue'
        label2['text'] = 'Tour Joueur-2 ' if player == 'X' else 'Tour Joueur-1'
        a = 1 - a
        b += 1

        vainqueur_combinaison = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9],  # ligne
            [1, 4, 7], [2, 5, 8], [3, 6, 9],  # colomn
            [1, 5, 9], [3, 5, 7]  # diagonal
        ]

        for combinaison in vainqueur_combinaison:
            if all(buttons[i-1].cget('text') == player for i in combinaison):
                disable_buttons()
                c = 1
                success_song()
                tkinter.messagebox.showinfo("Tic Tac Toe", f"le vainqueur est le Joueur {player}")
                return

        if b == 9:
            disable_buttons()
            c = 1
            tkinter.messagebox.showinfo("Morpion", "Match est Nul.")

window.mainloop()