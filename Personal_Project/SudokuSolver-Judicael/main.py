"""
    I do not own some part of the code,
    especially generator.py
"""

"""It use the backtracking algorithm"""




import tkinter as tk
from tkinter import messagebox
from random import randint
from isvalid import is_num_valid, is_valid_sudoku
from generator import _gen
import time
from PIL import ImageGrab
class SudokuSolver:
    def __init__(self, master):
        self.master = master
        self.master.title("Sudoku Solver")
        self.master.resizable(False, False)
        self.grid = [[None for _ in range(9)] for _ in range(9)]
        self.difficulty = "Easy"
        self.generated_list = []
        self.default_color = "#bbdefb"
        self.grid_clicked_color = "#bbdefd"
        self.grid_affected_color = "#ffffff"
        self.grid_unaffected_color = "#e2ebf3"
        self.generated_color = "#e2ebf3"
        self.fg_white = "white"
        self.fg_black = "black"
        self.grid_clicked = None
        self.buttons_can_be_clicked = True
        self._create_grid()
        self._create_menu()
        self._buttons()

    def _create_grid(self):
        # Create the grid
        self.grid = []
        for i in range(9):
            row = []
            for j in range(9):
                entry = tk.Entry(
                    width=3,
                    font=("Helvetica", 30),
                    justify="center",
                    bd=1,
                    relief=tk.RIDGE,
                )
                entry.grid(row=i, column=j, padx=1, pady=1)
                row.append(entry)
                entry.config(bg=self.default_color)
                entry.config(fg=self.fg_black)

            self.grid.append(row)

    def _clickable_buttons(self):
        self.buttons_can_be_clicked = True
        # rendre le bouton clicable
        self.solve_button.config(state=tk.NORMAL)
        self.generate_button.config(state=tk.NORMAL)
        self.clear_button.config(state=tk.NORMAL)

    def _unclickable_buttons(self):
        self.buttons_can_be_clicked = False
        # rendre les boutons incliquable
        self.solve_button.config(state=tk.DISABLED)
        self.generate_button.config(state=tk.DISABLED)
        self.clear_button.config(state=tk.DISABLED)

    def _menu_unclickable(self):
        self.file_menu.entryconfig("Exit(E)", state=tk.DISABLED)
        self.puzzle_menu.entryconfig("Solve(S)", state=tk.DISABLED)
        self.puzzle_menu.entryconfig("Generate(G)", state=tk.DISABLED)
        self.puzzle_menu.entryconfig("Clear(C)", state=tk.DISABLED)

    def _menu_clickable(self):
        self.file_menu.entryconfig("Exit(E)", state=tk.NORMAL)
        self.puzzle_menu.entryconfig("Solve(S)", state=tk.NORMAL)
        self.puzzle_menu.entryconfig("Generate(G)", state=tk.NORMAL)
        self.puzzle_menu.entryconfig("Clear(C)", state=tk.NORMAL)

    def _toggle_buttons(self):
        if self.buttons_can_be_clicked:
            self._unclickable_buttons()
            self._menu_unclickable()
        else:
            self._clickable_buttons()
            self._menu_clickable()

    def _create_menu(self):
        # créer le menu
        self.menu = tk.Menu(self.master)
        self.master.config(menu=self.menu)

        # remplir le menu
        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        # menu dropdown pour les difficultés
        self.difficulty_menu = tk.Menu(self.file_menu, tearoff=0)
        self.file_menu.add_cascade(
            label="Difficulty", menu=self.difficulty_menu)
        self.difficulty_menu.add_command(
            label="Easy (1)", command=lambda: self._toggle_difficulty("Easy")
        )
        self.difficulty_menu.add_command(
            label="Medium (2)", command=lambda: self._toggle_difficulty("Medium")
        )
        self.difficulty_menu.add_command(
            label="Hard (3)", command=lambda: self._toggle_difficulty("Hard")
        )
        self.file_menu.add_command(label="Save(S)", command=self.save)
        self.file_menu.add_command(
            label="Exit(E)", command=self.master.destroy)

        # Puzzle menu
        self.puzzle_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Puzzle", menu=self.puzzle_menu)
        self.puzzle_menu.add_command(label="Solve(S)", command=self.solve)
        self.puzzle_menu.add_command(
            label="Generate(G)", command=lambda: self.generate("Easy")
        )
        self.puzzle_menu.add_command(label="Clear(C)", command=self.clear)

        # menu help
        self.help_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="About", menu=self.help_menu)
        self.help_menu.add_command(label="About", command=self._about)

    def _about(self):
        messagebox.showinfo(
            "About",
            "Sudoku Solver\n"
            "Using backtracking algorithm\n"

            "Created by: \n"
            "    - Judicaël with the help of the internet, somme website, Github, and of course Youtube :D \n",

        )

    def _buttons(self):
        # Create "Solve" button
        self.solve_button = tk.Button(
            self.master,
            text="Solve",
            command=self.solve,
            bg="green",
            fg="white",
            width=13,
        )
        self.solve_button.grid(row=9, column=0, columnspan=2)

        # créer generate button
        self.generate_button = tk.Button(
            self.master,
            text="Generate",
            command=lambda: self.generate(self.difficulty),
            bg="purple",
            fg="white",
            width=13,
        )
        self.generate_button.grid(row=9, column=2, columnspan=2)

        # créer les difficulté
        self.difficulty_button = tk.Menubutton(
            self.master,
            text="Difficulty",
            relief=tk.RAISED,
            bg="yellow",
            fg="black",
            width=15,
        )
        self.difficulty_button.grid(row=9, column=5, columnspan=2)
        self.difficulty_menu = tk.Menu(self.difficulty_button, tearoff=0)
        # ajouter une command pour le difficulté easy
        self.difficulty_menu.add_command(
            label="Easy", command=lambda: self._toggle_difficulty("Easy")
        )
        self.difficulty_menu.add_command(
            label="Medium", command=lambda: self._toggle_difficulty("Medium")
        )
        self.difficulty_menu.add_command(
            label="Hard", command=lambda: self._toggle_difficulty("Hard")
        )
        self.difficulty_button["menu"] = self.difficulty_menu

        # creation du bouton claire
        self.clear_button = tk.Button(
            self.master,
            text="Clear",
            command=self.clear,
            bg="#F44336",
            fg="white",
            width=12,
        )
        self.clear_button.grid(row=9, column=7, columnspan=2)

    def _toggle_difficulty(self, difficulty):
        self.difficulty = difficulty
        self.difficulty_button.config(text="Difficulty: " + difficulty)

    def solve(self):
        # rendre les boutons uncliquable
        self._toggle_buttons()

        puzzle = [[0 for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                try:
                    puzzle[i][j] = int(self.grid[i][j].get())
                except ValueError:
                    pass

        # print(puzzle)

        if is_valid_sudoku(puzzle):
            if self.backtrack(puzzle):
                for i in range(9):
                    for j in range(9):
                        self.grid[i][j].delete(0, tk.END)
                        self.grid[i][j].insert(0, puzzle[i][j])
                        print(self.grid[i][j].get())
                        # sleep for 0.05 seconds
                        time.sleep(randint(1, 10) / 100)
                        self.master.update()
            else:
                messagebox.showerror("Error", "No solution exists")
        else:
            messagebox.showerror("Error", "Invalid Sudoku")

        # rendre les boutons cliquables
        self._toggle_buttons()

    def backtrack(self, puzzle):
        for i in range(9):
            for j in range(9):
                if puzzle[i][j] == 0:
                    for num in range(1, 10):
                        if is_num_valid(puzzle, i, j, num):
                            puzzle[i][j] = num
                            if self.backtrack(puzzle):
                                return True
                            puzzle[i][j] = 0
                    return False
        return True

    def generate(self, difficulty):
        board = _gen()
        for i in range(9):
            for j in range(9):
                self.grid[i][j].delete(0, tk.END)
                self.grid[i][j].insert(0, board[i][j])
                self.grid[i][j].config(bg="white")
        if difficulty == "Easy":
            for i in range(9):
                for j in range(9):
                    if randint(0, 1) != 1:
                        self.grid[i][j].delete(0, tk.END)
                        self.grid[i][j].config(bg=self.generated_color)
                        self.generated_list.append((i, j))
        elif difficulty == "Medium":
            for i in range(9):
                for j in range(9):
                    if randint(0, 3) != 1:
                        self.grid[i][j].delete(0, tk.END)
                        self.grid[i][j].config(bg=self.generated_color)
                        self.generated_list.append((i, j))
        elif difficulty == "Hard":
            for i in range(9):
                for j in range(9):
                    if randint(0, 5) != 1:
                        self.grid[i][j].delete(0, tk.END)
                        self.grid[i][j].config(bg=self.generated_color)
                        self.generated_list.append((i, j))

    def save(self):
        # sauvegarder l'image en png
        # get the coordinates of the puzzle grid
        x = self.grid[0][0].winfo_rootx()
        y = self.grid[0][0].winfo_rooty()
        x1 = self.grid[8][8].winfo_rootx() + 50
        y1 = self.grid[8][8].winfo_rooty() + 50
        # wait for 0.5 seconds
        time.sleep(0.5)
        # save the image as ./assets/sudoku-[current time].png
        ImageGrab.grab().crop((x, y, x1, y1)).save(
            "./assets/sudoku-" + str(time.time()) + ".png"
        )

    def clear(self):
        for i in range(9):
            for j in range(9):
                self.grid[i][j].delete(0, tk.END)
                self.grid[i][j].config(bg=self.default_color)


if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuSolver(root)
    root.mainloop()
