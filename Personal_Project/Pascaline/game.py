from grid import Grid
from blocks import *
import random
import pygame.mixer as mixer

class Game:
    def __init__(self):
        self.grid = Grid()  # Crée une instance de la grille de jeu
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]  # Liste des blocs disponibles
        self.current_block = self.get_random_block()  # Bloc actuel en jeu
        self.next_block = self.get_random_block()  # Prochain bloc à venir
        self.game_over = False  # Indicateur de fin de jeu
        self.score = 0  # Score du joueur

        mixer.music.load("Sounds/music.mp3")  
        mixer.music.play(-1)  

    def update_score(self, lines_cleared, move_down_points):
        # Met à jour le score du joueur en fonction du nombre de lignes effacées et des points gagnés en déplacement vers le bas
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 300
        elif lines_cleared == 3:
            self.score += 500
        self.score += move_down_points

    def get_random_block(self):
        # Sélectionne un bloc aléatoire parmi ceux disponibles
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]  # Réinitialise les blocs s'ils ont tous été utilisés
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block
    
    def move_left(self):
        # Déplace le bloc actuel vers la gauche s'il est possible de le faire
        self.current_block.move(0, -1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, 1)  # Annule le déplacement si le bloc est hors de la grille ou ne s'adapte pas

    def move_right(self):
        self.current_block.move(0, 1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, -1) 

    def move_down(self):
        self.current_block.move(1, 0)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(-1, 0) 
            self.lock_block()  # Verrouille le bloc en place s'il ne peut plus descendre

    def lock_block(self):
        # Verrouille le bloc actuel en place dans la grille
        tiles = self.current_block.get_cell_positions()
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id
        self.current_block = self.next_block  # Définit le bloc suivant comme le nouveau bloc actuel
        self.next_block = self.get_random_block()  # Sélectionne un nouveau bloc pour le bloc suivant
        rows_cleared = self.grid.clear_full_rows()  # Efface les lignes complètes et retourne le nombre de lignes effacées
        self.update_score(rows_cleared, 0)  # Met à jour le score en fonction du nombre de lignes effacées
        if self.block_fits() == False:
            self.game_over = True  # Si le nouveau bloc ne s'adapte pas dans la grille, le jeu est terminé
            mixer.music.load("Sounds/gmo.mp3")
            mixer.music.play()

    def reset(self):
        # Réinitialise le jeu à son état initial
        self.grid.reset()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0

    def block_fits(self):
        # Vérifie si le bloc actuel s'adapte correctement dans la grille
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_empty(tile.row, tile.column) == False:
                return False
        return True

    def rotate(self):
        # Effectue une rotation du bloc actuel s'il est possible de le faire
        self.current_block.rotate()
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.undo_rotation()  # Annule la rotation si le bloc est hors de la grille ou ne s'adapte pas

    def block_inside(self):
        # Vérifie si le bloc actuel est entièrement à l'intérieur de la grille
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_inside(tile.row, tile.column) == False:
                return False
        return True
    
    def draw(self, screen):
        # Dessine les éléments du jeu sur l'écran
        self.grid.draw(screen)  # Dessine la grille
        self.current_block.draw(screen, 11, 11)  # Dessine le bloc actuel

        if self.next_block.id == 3:
            self.next_block.draw(screen, 255, 510)  # Dessine le bloc suivant à la position spécifiée
        elif self.next_block.id == 4:
            self.next_block.draw(screen, 255, 500)
        else:
            self.next_block.draw(screen, 255, 490)
