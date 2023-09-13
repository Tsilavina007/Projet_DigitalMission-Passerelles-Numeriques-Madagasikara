import tkinter as tk
import random

player_pions = []  # Liste pour stocker les positions des pions du joueur
computer_pions = []  # Liste pour stocker les positions des pions de l'ordinateur

current_player = "player"  # Variable pour suivre le joueur actuel

def draw_fanoron_telo(canvas):
    width = canvas.winfo_reqwidth()
    height = canvas.winfo_reqheight()

    # Dessiner le carré
    canvas.create_rectangle(width / 4, height / 4, 3 * width / 4, 3 * height / 4, width=2)

    # Dessiner les deux diagonales
    canvas.create_line(width / 4, height / 4, 3 * width / 4, 3 * height / 4, width=2)
    canvas.create_line(width / 4, 3 * height / 4, 3 * width / 4, height / 4, width=2)

    # Dessiner les deux bissectrices du carré
    mid_x = width / 2
    mid_y = height / 2
    canvas.create_line(width / 4, mid_y, 3 * width / 4, mid_y, width=2)
    canvas.create_line(mid_x, height / 4, mid_x, 3 * height / 4, width=2)

def computer_move():
    global current_player
    free_positions = [(x, y) for x in range(1, 7) for y in range(1, 7) if (x, y) not in player_pions and (x, y) not in computer_pions]

    if len(free_positions) > 0:
        # Choisir une position aléatoire pour le pion de l'ordinateur parmi les positions libres
        x, y = random.choice(free_positions)
        canvas.create_text(x*37.5, y*37.5, text="O", fill="red", font=("Helvetica", 20, "bold"))
        computer_pions.append((x, y))
        
    # Vérifier s'il y a un gagnant
    if check_winner(computer_pions):
        canvas.create_text(150, 150, text="L'ordinateur a gagné!", fill="red", font=("Helvetica", 20, "bold"))
        current_player = "finished"
    elif len(computer_pions) + len(player_pions) == 9:
        canvas.create_text(150, 150, text="Match nul!", fill="black", font=("Helvetica", 20, "bold"))
        current_player = "finished"
    else:
        current_player = "player"

def on_canvas_click(event):
    global current_player

    if current_player == "player":
        # Coordonnées du clic
        x = event.x
        y = event.y

        # Vérifier si le clic est sur l'extrémité du plateau (à 1/8 du bord du plateau)
        if 0 <= x <= 300 and 0 <= y <= 300:
            if x < 37.5:
                x = 1
            elif 37.5 <= x < 75:
                x = 2
            elif 75 <= x < 112.5:
                x = 3
            elif 112.5 <= x < 150:
                x = 4
            elif 150 <= x < 187.5:
                x = 5
            elif 187.5 <= x < 225:
                x = 6
            elif 225 <= x < 262.5:
                x = 7
            elif x >= 262.5:
                x = 8

            if y < 37.5:
                y = 1
            elif 37.5 <= y < 75:
                y = 2
            elif 75 <= y < 112.5:
                y = 3
            elif 112.5 <= y < 150:
                y = 4
            elif 150 <= y < 187.5:
                y = 5
            elif 187.5 <= y < 225:
                y = 6
            elif 225 <= y < 262.5:
                y = 7
            elif y >= 262.5:
                y = 8

            # Vérifier si la case est libre avant de placer un pion du joueur
            if (x, y) not in player_pions and (x, y) not in computer_pions:
                # Dessiner un pion du joueur à la position du clic
                canvas.create_text(x*37.5, y*37.5, text="X", fill="green", font=("Helvetica", 20, "bold"))

                # Mettre à jour la position du dernier pion du joueur
                player_pions.append((x, y))

                # Vérifier s'il y a un gagnant
                if check_winner(player_pions):
                    canvas.create_text(150, 150, text="Le joueur a gagné!", fill="green", font=("Helvetica", 20, "bold"))
                    current_player = "finished"
                else:
                    computer_move()

def check_winner(pions):
    # Vérifier les lignes, colonnes et diagonales pour déterminer s'il y a un gagnant
    lines = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    columns = [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
    diagonals = [(1, 5, 9), (3, 5, 7)]

    for line in lines + columns + diagonals:
        if all(p in pions for p in line):
            return True

    return False

def main():
    global canvas

    root = tk.Tk()
    root.title("Morpion sur Fanoron-telo")

    canvas = tk.Canvas(root, width=300, height=300)
    canvas.pack()

    draw_fanoron_telo(canvas)

    # Liaison de l'événement clic de la souris au canevas
    canvas.bind("<Button-1>", on_canvas_click)

    root.mainloop()

if __name__ == "__main__":
    main()
