"""this is just a file containing the old version of our game, this one doesn't really work"""
"""It worked but there's no 6x6 version"""

from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkfont
from music import music_class
from customtkinter import *
import pygame
import random
pygame.mixer.init()
music_obj = music_class()


class audio:
    def __init__(self):

        self.i = random.randint(0, 3)

    def music(self):
        if self.i == 0:
            music_obj.play_music1()
        if self.i == 1:
            music_obj.play_music2()
        if self.i == 2:
            music_obj.play_music3()
        if self.i == 3:
            music_obj.play_music4()


sound = audio()
sound.music()


class Morpion:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Morpion game")
        self.window.configure(bg="#3c0384")
        self.current_player = "X"
        self.score_X = 0
        self.score_O = 0

        self.buttons = []
        self.create_gui()

    def create_gui(self):

        # frame for button
        self.frame1 = CTkFrame(
            self.window, fg_color="#4ffaff", width=380, height=380, corner_radius=24)
        self.frame1.grid(row=0, column=1, pady=16, padx=16)

        for i in range(3):
            row = []
            for j in range(3):
                button = CTkButton(self.frame1, text=" ", width=150, height=150,
                                   command=lambda i=i, j=j: self.button_click(i, j), fg_color="#5801c6", corner_radius=24, font=("Rubik bold", 32))
                button.grid(row=i, column=j, padx=5, pady=5)
                row.append(button)
            self.buttons.append(row)

        # frame for score and button
        score_frame = CTkFrame(self.window, corner_radius=16, width=450)
        score_frame.configure(fg_color="#2e0266")
        score_frame.grid(row=0, column=4, rowspan=5, padx=20)

        CTkLabel(score_frame, text="Dashboard", font=("Rubik black", 50)).grid(
            row=0, column=0, columnspan=2, pady=30)
        CTkLabel(score_frame, text="Score", font=("Rubik bold", 30)).grid(
            row=2, column=0, columnspan=2)
        CTkLabel(score_frame, text="Player X:", font=(
            "Rubik bold", 20)).grid(row=3, column=0, pady=16)
        self.label_score_X = CTkLabel(
            score_frame, text="0", font=("Rubik bold", 20))
        self.label_score_X.grid(row=3, column=1)
        CTkLabel(score_frame, text="Player O:", font=(
            "Rubik bold", 20)).grid(row=4, column=0, pady=16)
        self.label_score_O = CTkLabel(
            score_frame, text="0", font=("Rubik bold", 20))
        self.label_score_O.grid(row=4, column=1)

        # button for new game et refaire
        CTkButton(score_frame, text="new game", command=self.new_game, width=250,
                  height=70, font=("Rubik bold", 20), fg_color="#e773ff").grid(row=5+2, column=0, columnspan=2, pady=3)

        CTkButton(score_frame, text="Restart", command=self.reset_scores, width=250,
                  height=70, font=("Rubik bold", 20), fg_color="#e773ff").grid(row=6+2, column=0, columnspan=2, padx=60, pady=30)

    def check_lines(self):

        board = [[button.cget("text") for button in row]
                 for row in self.buttons]
        for row in board:
            if row[0] == row[1] == row[2] != " ":
                return True
        return False

    def check_columns(self):

        board = [[button.cget("text") for button in row]
                 for row in self.buttons]
        for j in range(3):
            if board[0][j] == board[1][j] == board[2][j] != " ":
                return True
        return False

    def check_diagonals(self):

        board = [[button.cget("text") for button in row]
                 for row in self.buttons]
        if board[0][0] == board[1][1] == board[2][2] != " ":
            return True
        if board[0][2] == board[1][1] == board[2][0] != " ":
            return True

        return False

    def button_click(self, i, j):

        global text
        button = self.buttons[i][j]
        text = button.cget("text")

        if text == " ":
            if self.current_player == "X":
                music_obj.play_soundX()
            if self.current_player == "O":
                music_obj.play_soundO()
            button.configure(text=self.current_player)

            if self.check_winner():
                music_obj.win()
                messagebox.showinfo(
                    "We have a winner", f"Player {self.current_player} won !")
                if self.current_player == "X":
                    self.score_X += 1
                    self.label_score_X.configure(text=str(self.score_X))

                else:
                    self.score_O += 1
                    self.label_score_O.configure(text=str(self.score_O))

                self.new_game()
            elif self.check_draw():
                self.new_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        return self.check_lines() or self.check_columns() or self.check_diagonals()

    def check_draw(self):
        board = [[text for button in row] for row in self.buttons]
        return all(board[i][j] != " " for i in range(3) for j in range(3))

    def new_game(self):
        music_obj.clic()
        self.current_player = "X"
        for row in self.buttons:
            for button in row:
                button.configure(text=" ")

    def reset_scores(self):
        music_obj.clic()
        self.score_X = 0
        self.score_O = 0
        self.label_score_X.configure(text="0")
        self.label_score_O.configure(text="0")

    def run(self):
        self.window.mainloop()


morpion_game = Morpion()
morpion_game.run()
