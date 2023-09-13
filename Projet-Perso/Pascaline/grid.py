import pygame
from colors import Colors

class Grid:
    def __init__(self):
        self.num_rows = 20  # Nombre de lignes de la grille
        self.num_cols = 10  # Nombre de colonnes de la grille
        self.cell_size = 30  # Taille d'une cellule de la grille
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]  # Grille représentée par une liste de listes
        self.colors = Colors.get_cell_colors()  # Couleurs des cellules de la grille

    def print_grid(self):
        # Affiche la grille sur la console
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end=" ")
            print()

    def is_inside(self, row, column):
        # Vérifie si une cellule est à l'intérieur de la grille
        if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_cols:
            return True
        return False
    
    def is_empty(self, row, column):
        # Vérifie si une cellule est vide
        if self.grid[row][column] == 0:
            return True
        return False
    
    def is_row_full(self, row):
        # Vérifie si une ligne est pleine
        for column in range(self.num_cols):
            if self.grid[row][column] == 0:
                return False
        return True
    
    def clear_row(self, row):
        # Vide une ligne en la remplissant de zéros
        for column in range(self.num_cols):
            self.grid[row][column] = 0

    def move_row_down(self, row, num_rows):
        # Déplace une ligne vers le bas en la remplaçant par la ligne précédente
        for column in range(self.num_cols):
            self.grid[row+num_rows][column] = self.grid[row][column]
            self.grid[row][column] = 0

    def clear_full_rows(self):
        # Supprime les lignes pleines de la grille et renvoie le nombre de lignes supprimées
        completed = 0
        for row in range(self.num_rows-1, 0, -1):
            if self.is_row_full(row):
                self.clear_row(row)
                completed += 1
            elif completed > 0:
                self.move_row_down(row, completed)
        return completed
    
    def reset(self):
        # Réinitialise la grille en la remplissant de zéros
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                self.grid[row][column] = 0
    
    def draw(self, screen):
        # Dessine la grille sur l'écran
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]  # Valeur de la cellule (indice de couleur)
                cell_rect = pygame.Rect(column*self.cell_size + 11, row*self.cell_size + 11,
                                        self.cell_size - 1, self.cell_size - 1)  # Rectangle représentant la cellule
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)  # Dessine le rectangle avec la couleur correspondante                                                                                                                                           