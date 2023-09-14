import tkinter as tk
import customtkinter
import random
import pygame

# Fonction pour vérifier s'il y a une victoire
def check_win(board, player):
    # Vérification des lignes
    for row in board:
        if set(row) == {player}:
            return True

    # Vérification des colonnes
    for col in range(3):
        if {board[0][col], board[1][col], board[2][col]} == {player}:
            return True

    # Vérification des diagonales
    if {board[0][0], board[1][1], board[2][2]} == {player}:
        return True
    if {board[0][2], board[1][1], board[2][0]} == {player}:
        return True

    return False

# Fonction pour choisir le coup de l'ordinateur (avec Minimax et Alpha-Beta Pruning)
def computer_move(board):
    best_score = float('-inf')
    best_move = None

    for row in range(3):
        for col in range(3):
            if board[row][col] == "":
                board[row][col] = "O"
                score = minimax(board, 0, False, float('-inf'), float('inf'))
                board[row][col] = ""

                if score > best_score:
                    best_score = score
                    best_move = (row, col)

    return best_move

# Fonction de l'algorithme Minimax avec élagage alpha-bêta
def minimax(board, depth, is_maximizing, alpha, beta):
    if check_win(board, "X"):
        return -1
    elif check_win(board, "O"):
        return 1
    elif "" not in [cell for row in board for cell in row]:
        return 0

    if is_maximizing:
        max_eval = float('-inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == "":
                    board[row][col] = "O"
                    eval_score = minimax(board, depth + 1, False, alpha, beta)
                    board[row][col] = ""
                    max_eval = max(max_eval, eval_score)
                    alpha = max(alpha, eval_score)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == "":
                    board[row][col] = "X"
                    eval_score = minimax(board, depth + 1, True, alpha, beta)
                    board[row][col] = ""
                    min_eval = min(min_eval, eval_score)
                    beta = min(beta, eval_score)
                    if beta <= alpha:
                        break
        return min_eval

#Fonction son loss
def loss_song():
    # Charger le fichier audio
    sound = pygame.mixer.Sound("./images/loss.mp3")

    # Jouer le fichier audio sur le deuxième canal
    channel1.play(sound)

# Fonction pour gérer le clic sur une case
def on_click(row, col):
    global game_over
    decide_song()
    if board[row][col] == "" and not game_over:
        board[row][col] = "X"
        buttons[row][col].configure(text="X",state=tk.DISABLED,text_color="red")
        if check_win(board, "X"):
            status_label.config(text="Vous avez gagné !")
            game_over = True
        else:
            if "" not in [cell for row in board for cell in row]:
                status_label.configure(text="Match nul !")
                game_over = True
            else:
                comp_row, comp_col = computer_move(board)
                board[comp_row][comp_col] = "O"
                buttons[comp_row][comp_col].configure(text="O", state=tk.DISABLED)
                if check_win(board, "O"):
                    loss_song()
                    status_label.configure(text="L'ordinateur a gagné !")
                    game_over = True
def main_song():
    # Charger le fichier audio
    sound = pygame.mixer.Sound("./images/jazz1.mp3")
    #volume
    sound.set_volume(0.1)
    # Jouer le fichier audio sur le deuxième canal
    channel.play(sound)
def decide_song():
    # Charger le fichier audio
    sound = pygame.mixer.Sound("./images/decide.mp3")

    # Jouer le fichier audio sur le deuxième canal
    channel2.play(sound)
# Création de la fenêtre principale
window = tk.Tk()
window.title("Morpion")
window.geometry("400x300")
#son
pygame.mixer.init()
channel = pygame.mixer.Channel(0)
channel1 = pygame.mixer.Channel(1)
channel2 = pygame.mixer.Channel(2)
main_song()
#Label MORPION
label=tk.Label(master=window,text="MORPION",font=("Arial", 15))
label.pack()
#Frame
frame1=tk.Frame(master=window,borderwidth=2,relief=tk.SUNKEN,bg='#dadec3')
frame1.pack(padx=10,pady=10)

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
# Création du tableau de jeu
board = [["" for _ in range(3)] for _ in range(3)]

# Création des boutons de jeu
buttons = []
for row in range(3):
    row_buttons = []
    for col in range(3):
        button = customtkinter.CTkButton(frame1, text="",
                          command=lambda r=row, c=col: on_click(r, c),**params)
        button.grid(row=row, column=col,padx=5,pady=5)
        row_buttons.append(button)
    buttons.append(row_buttons)
# Étiquette pour afficher l'état du jeu
status_label = tk.Label(window, text="")
status_label.pack()

# Variable pour suivre l'état du jeu
game_over = False

# Lancement de la boucle principale de la fenêtre
window.mainloop()
