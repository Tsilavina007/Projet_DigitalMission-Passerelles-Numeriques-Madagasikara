import tkinter as tk  # Importation du module Tkinter pour créer l'interface graphique
from tkinter import messagebox, ttk  # Importation de classes spécifiques de Tkinter (boîtes de dialogue et styles)
import random  # Importation du module random pour la génération de nombres aléatoires
from PIL import Image, ImageTk  # Importation de classes spécifiques de PIL (traitement d'images)

class Morpion:
    def __init__(self, master):
        self.master = master  # Stockage de la référence à la fenêtre principale dans l'attribut self.master
        self.master.title("Morpion")  # Définition du titre de la fenêtre principale
        self.master.geometry("600x600")  # Définition de la taille de la fenêtre principale
        self.master.config(background="#41b77F")

        self.home_frame = None  # Initialisation de l'attribut self.home_frame à None
        self.game_frame = None  # Initialisation de l'attribut self.game_frame à None

        self.show_home()  # Appel de la méthode show_home pour afficher l'écran d'accueil du jeu

    def show_home(self):
        if self.game_frame:
            self.game_frame.destroy()  # Destruction du frame du jeu s'il existe déjà

        self.home_frame = tk.Frame(self.master, bg= "#41b77F")  # Création d'un nouveau frame pour l'écran d'accueil
        self.home_frame.pack()  # Placement du frame sur la fenêtre principale

        self.master.title("Morpion - Accueil")  # Définition du titre de la fenêtre principale

        style = ttk.Style()  # Création d'une instance de la classe Style pour personnaliser les widgets

        style.configure("TitleLabel.TLabel", font=("Arial", 20, "bold"), background= "#41b77F")  # Configuration du style du label du titre

        self.title_label = ttk.Label(self.home_frame, text="Bienvenue dans le jeu du Morpion !", style="TitleLabel.TLabel")
        self.title_label.pack(pady=5)  # Création et placement du label du titre dans le frame de l'accueil

        background_image = Image.open("img.png")  # Ouverture de l'image de fond
        background_photo = ImageTk.PhotoImage(background_image)  # Création d'un objet PhotoImage à partir de l'image

        background_label = tk.Label(self.home_frame, image=background_photo, background= "#41b77F")  # Création du label avec l'image de fond
        background_label.pack(fill="both", expand=True)  # Placement du label pour remplir le frame

        background_label.image = background_photo  # Conservation d'une référence à l'image pour éviter sa suppression

        self.mode_label = tk.Label(self.home_frame, text="Choisissez le mode de jeu :", font=("Verdana", 16), fg="tomato",  background= "#41b77F")
        self.mode_label.pack(pady=10)  # Création et placement du label du mode de jeu dans le frame de l'accueil

        style.configure("Custom.TButton", font=("Arial", 12), background="turquoise", width=20)  # Configuration du style des boutons

        self.joueur_vs_joueur_button = ttk.Button(self.home_frame, text="Joueur contre Joueur", style="Custom.TButton", command=self.start_joueur_vs_joueur)
        self.joueur_vs_joueur_button.pack(pady=10)  # Création et placement du bouton Joueur contre Joueur

        self.joueur_vs_ordi_button = ttk.Button(self.home_frame, text="Joueur contre Ordinateur", style="Custom.TButton", command=self.start_joueur_vs_ordi)
        self.joueur_vs_ordi_button.pack(pady=10)  # Création et placement du bouton Joueur contre Ordinateur

    def return_to_home(self):
        confirmed = messagebox.askyesno("Confirmation", "Êtes-vous sûr de vouloir revenir à l'accueil ?")
        if confirmed:
            self.show_home()  # Appel de la méthode show_home pour afficher l'écran d'accueil lorsque le joueur confirme

    def start_joueur_vs_joueur(self):
        if self.home_frame:
            self.home_frame.destroy()  # Destruction du frame de l'accueil s'il existe

        self.game_frame = tk.Frame(self.master,  background= "#41b77F")  # Création d'un nouveau frame pour le jeu
        self.game_frame.pack()  # Placement du frame sur la fenêtre principale

        self.mode = "joueur_vs_joueur"    # Définition du mode de jeu

        self.other_player = "O"  # Initialisation du symbole du joueur autre que l'ordinateur
        self.computer_player = "X"  # Initialisation du symbole de l'ordinateur
        self.score_o = 0  # Initialisation du score du joueur O
        self.score_x = 0  # Initialisation du score du joueur X

        self.current_player = self.other_player  # Initialisation du joueur courant avec le joueur autre que l'ordinateur
        self.board = [[" " for _ in range(3)] for _ in range(3)]  # Initialisation de la grille de jeu
        self.buttons = []  # Liste pour stocker les boutons du jeu
        for row in range(3):
            button_row = []
            for col in range(3):
                button = tk.Button(self.game_frame, text=" ", borderwidth=5, width=3, height=0, font=("Arial", 50, "bold"), bg="khaki", highlightbackground="red", command=lambda row=row, col=col: self.make_move(row, col))
                button.grid(row=row, column=col, sticky="nsew")  # Placement des boutons dans une grille
                button_row.append(button)
            self.buttons.append(button_row)
        self.message_label = tk.Label(self.game_frame, text="C'est à vous de jouer !", font=("Verdana", 14), fg="tomato",  background= "#41b77F")
        self.message_label.grid(row=3, column=0, columnspan=3)  # Placement du label du message de jeu

        style = ttk.Style()
        style.configure("Custom.TButton", font=("Arial", 12), background="turquoise", width=15)  # Configuration du style des boutons

        self.reset_button = ttk.Button(self.game_frame, text="Rejouer", style="Custom.TButton", command=self.reset_game)
        self.reset_button.grid(row=5, column=0, columnspan=1)  # Création et placement du bouton Rejouer

        self.return_button = ttk.Button(self.game_frame, text="Retour à l'accueil", style="Custom.TButton", command=self.return_to_home)
        self.return_button.grid(row=5, column=2, columnspan=1)  # Création et placement du bouton Retour à l'accueil

        style.configure("ScoreLabel.TLabel", font=("Arial", 16, "bold"), foreground="black",  background= "#41b77F")  # Configuration du style du label du score

        self.score_label = ttk.Label(self.game_frame, text="Joueur O   O ⇄ O   Joueur X", style="ScoreLabel.TLabel")
        self.score_label.grid(row=4, column=0, columnspan=3, pady=20)  # Création et placement du label du score

    def start_joueur_vs_ordi(self):
        if self.home_frame:
            self.home_frame.destroy()  # Destruction du frame de l'accueil s'il existe

        self.game_frame = tk.Frame(self.master,  background= "#41b77F")  # Création d'un nouveau frame pour le jeu
        self.game_frame.pack()  # Placement du frame sur la fenêtre principale

        self.mode = "joueur_vs_ordi"  # Définition du mode de jeu

        self.master.title("Morpion")  # Définition du titre de la fenêtre principale

        self.other_player = "O"  # Initialisation du symbole du joueur autre que l'ordinateur
        self.computer_player = "X"  # Initialisation du symbole de l'ordinateur
        self.score_o = 0  # Initialisation du score du joueur O
        self.score_x = 0  # Initialisation du score du joueur X

        self.current_player = self.other_player  # Initialisation du joueur courant avec le joueur autre que l'ordinateur
        self.board = [[" " for _ in range(3)] for _ in range(3)]  # Initialisation de la grille de jeu
        self.buttons = []  # Liste pour stocker les boutons du jeu
        for row in range(3):
            button_row = []
            for col in range(3):
                button = tk.Button(self.game_frame, text=" ", borderwidth=5, width=3, height=0, font=("Arial", 50, "bold"), bg="khaki", highlightbackground="red", command=lambda row=row, col=col: self.make_move(row, col))
                button.grid(row=row, column=col, sticky="nsew")  # Placement des boutons dans une grille
                button_row.append(button)
            self.buttons.append(button_row)
        self.message_label = tk.Label(self.game_frame, text="C'est à vous de jouer !", font=("Verdana", 14), fg="tomato",  background= "#41b77F")
        self.message_label.grid(row=3, column=0, columnspan=3)  # Placement du label du message de jeu

        style = ttk.Style()
        style.configure("Custom.TButton", font=("Arial", 12), background="turquoise", width=15)  # Configuration du style des boutons

        self.reset_button = ttk.Button(self.game_frame, text="Rejouer", style="Custom.TButton", command=self.reset_game)
        self.reset_button.grid(row=5, column=0, columnspan=1)  # Création et placement du bouton Rejouer

        self.return_button = ttk.Button(self.game_frame, text="Retour à l'accueil", style="Custom.TButton", command=self.return_to_home)
        self.return_button.grid(row=5, column=2, columnspan=1)  # Création et placement du bouton Retour à l'accueil

        style.configure("ScoreLabel.TLabel", font=("Arial", 16, "bold"), foreground="black",  background= "#41b77F")  # Configuration du style du label du score

        self.score_label = ttk.Label(self.game_frame, text="Joueur O   O ⇄ O   Joueur X", style="ScoreLabel.TLabel")
        self.score_label.grid(row=4, column=0, columnspan=3, pady=20)  # Création et placement du label du score

        if self.current_player == self.computer_player:
            self.make_computer_move()  # Laisser l'ordinateur jouer en premier s'il commence

    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player  # Mettre à jour la grille avec le symbole du joueur actuel
            self.buttons[row][col].configure(text=self.current_player,
                                             fg="tomato" if self.current_player == self.other_player else "turquoise")  # Mettre à jour le texte et la couleur du bouton correspondant
            if self.check_winner(self.current_player):  # Vérifier s'il y a un gagnant
                if self.current_player == "O":
                    self.score_o += 1  # Incrémenter le score du joueur O
                else:
                    self.score_x += 1  # Incrémenter le score du joueur X
                self.update_score_label()  # Mettre à jour le label du score
                if self.current_player == self.other_player:
                    messagebox.showinfo("Gagné !",
                                        f"Joueur {self.current_player} a gagné !")  # Afficher un message de victoire pour le joueur
                else:
                    messagebox.showinfo("Gagné !",
                                        f"Joueur {self.current_player} a gagné !")  # Afficher un message de victoire pour l'ordinateur
                self.reset_game()  # Réinitialiser le jeu après la fin d'une partie
            elif self.check_draw():  # Vérifier s'il y a un match nul
                messagebox.showinfo("Match nul", "La partie est un match nul.")  # Afficher un message de match nul
                self.reset_game()  # Réinitialiser le jeu après un match nul
            else:
                self.current_player = self.computer_player if self.current_player == self.other_player else self.other_player  # Changer le joueur actuel
                self.message_label.configure(
                    text=f"C'est au tour de joueur {self.current_player}.")  # Mettre à jour le label du message de jeu
                if self.mode == "joueur_vs_ordi" and self.current_player == self.computer_player:
                    self.make_computer_move()  # Laisser l'ordinateur jouer s'il est le joueur actuel

    def update_score_label(self):
        self.score_label.configure(
            text=f"Joueur O    {self.score_o} ⇄ {self.score_x}    Joueur X")  # Mettre à jour le texte du label du score

    def make_computer_move(self):
        available_moves = []
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == " ":
                    available_moves.append((row, col))  # Collecter les mouvements disponibles

        # Vérifier s'il y a une opportunité de gagner
        for move in available_moves:
            row, col = move
            self.board[row][col] = self.computer_player  # Essayer chaque mouvement possible pour l'ordinateur
            if self.check_winner(self.computer_player):
                self.buttons[row][col].configure(text=self.computer_player,
                                                 fg="turquoise")  # Mettre à jour le texte et la couleur du bouton
                self.score_x += 1  # Incrémenter le score du joueur X (ordinateur)
                self.update_score_label()  # Mettre à jour le label du score
                messagebox.showinfo("Perdu !", f"L'ordinateur a gagné !")  # Afficher un message de défaite
                self.reset_game()  # Réinitialiser le jeu après la fin d'une partie
                return

            self.board[row][col] = " "  # Annuler le mouvement

        # Vérifier s'il y a une opportunité de bloquer le joueur
        for move in available_moves:
            row, col = move
            self.board[row][col] = self.other_player  # Essayer chaque mouvement possible pour bloquer le joueur
            if self.check_winner(self.other_player):
                self.board[row][col] = self.computer_player  # Effectuer le mouvement pour bloquer le joueur
                self.buttons[row][col].configure(text=self.computer_player,
                                                 fg="turquoise")  # Mettre à jour le texte et la couleur du bouton
                self.current_player = self.other_player  # Changer le joueur actuel
                self.message_label.configure(
                    text=f"C'est au tour de joueur {self.current_player}.")  # Mettre à jour le label du message de jeu
                return

            self.board[row][col] = " "  # Annuler le mouvement

        # Choisir un mouvement aléatoire parmi les mouvements disponibles
        if available_moves:
            row, col = random.choice(available_moves)
            self.board[row][col] = self.computer_player  # Effectuer un mouvement aléatoire
            self.buttons[row][col].configure(text=self.computer_player,
                                             fg="turquoise")  # Mettre à jour le texte et la couleur du bouton
            self.current_player = self.other_player  # Changer le joueur actuel
            self.message_label.configure(
                text=f"C'est au tour de joueur {self.current_player}.")  # Mettre à jour le label du message de jeu

    def check_winner(self, player):
        # Vérifier les lignes
        for row in self.board:
            if row.count(player) == 3:
                return True

        # Vérifier les colonnes
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] == player:
                return True

        # Vérifier les diagonales
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        if self.board[2][0] == self.board[1][1] == self.board[0][2] == player:
            return True

        return False

    def check_draw(self):
        for row in self.board:
            if " " in row:
                return False
        return True

    def reset_game(self):
        self.current_player = self.other_player  # Réinitialiser le joueur actuel
        self.board = [[" " for _ in range(3)] for _ in range(3)]  # Réinitialiser la grille de jeu
        for row in self.buttons:
            for button in row:
                button.configure(text=" ", fg="black")  # Réinitialiser les boutons du jeu
        self.message_label.configure(text="C'est à vous de jouer !")  # Réinitialiser le label du message de jeu


root = tk.Tk()  # Création de la fenêtre principale
game = Morpion(root)  # Création d'une instance de la classe Morpion avec la fenêtre principale comme argument
root.mainloop()  # Boucle principale de l'interface graphique

