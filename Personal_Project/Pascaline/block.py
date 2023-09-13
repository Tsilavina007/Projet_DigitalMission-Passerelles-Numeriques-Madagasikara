from colors import Colors
import pygame
from position import Position

class Block:
    def __init__(self, id):
        self.id = id  # Identifiant du bloc
        self.cells = {}  # Dictionnaire des cellules constituant le bloc
        self.cell_size = 30  # Taille d'une cellule
        self.row_offset = 0  # Décalage de lignes du bloc
        self.column_offset = 0  # Décalage de colonnes du bloc
        self.rotation_state = 0  # État de rotation actuel du bloc
        self.colors = Colors.get_cell_colors()  # Couleurs des cellules du bloc

    def move(self, rows, columns):
        # Déplace le bloc en ajoutant le nombre de lignes et de colonnes spécifié
        self.row_offset += rows
        self.column_offset += columns

    def get_cell_positions(self):
        # Renvoie les positions des cellules du bloc dans la grille
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for position in tiles:
            position = Position(position.row + self.row_offset, position.column + self.column_offset)
            moved_tiles.append(position)
        return moved_tiles
    
    def rotate(self):
        # Effectue une rotation du bloc
        self.rotation_state += 1
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0

    def undo_rotation(self):
        # Annule la rotation du bloc
        self.rotation_state -= 1
        if self.rotation_state == 0:
            self.rotation_state = len(self.cells) - 1

    def draw(self, screen, offset_x, offset_y):
        # Dessine le bloc sur l'écran avec un décalage spécifié
        tiles = self.get_cell_positions()
        for tile in tiles:
            tile_rect = pygame.Rect(offset_x + tile.column * self.cell_size, 
                                    offset_y + tile.row * self.cell_size, 
                                    self.cell_size - 1, self.cell_size - 1)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)
