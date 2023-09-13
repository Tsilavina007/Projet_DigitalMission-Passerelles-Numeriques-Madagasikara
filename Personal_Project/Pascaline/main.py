import pygame
import sys
from game import Game
from colors import Colors
from bgcolors import BGcolors

#code initialise pygame
pygame.init()

# la police pour le texte du jeu.
font_path = "fonts/freaks-of-nature-massive.ttf"
title_font = pygame.font.Font(font_path, 40)
title_font2 = pygame.font.Font(None, 40)

#Définition des surfaces de texte et des boutons 
texte_surface = title_font.render("TETRIS", True, Colors.white, BGcolors.chocolat)
score_surface = title_font.render("Score", True, Colors.white, BGcolors.black)
next_surface = title_font.render("Next", True, Colors.white, BGcolors.black)
game_over_surface = title_font.render("XXX", True, Colors.red)

score_rect = pygame.Rect(320, 200, 170, 60)
next_rect = pygame.Rect(320, 450, 170, 160)

# Initialiser l'écran et la fenêtre du jeu
screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Python Tetris")

# Initialiser l'horloge pour limiter la fréquence d'affichage
clock = pygame.time.Clock()

# Initialiser l'objet de jeu Tetris
game = Game()

# Définir un événement personnalisé pour mettre à jour le jeu périodiquement
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

# Définir les rectangles pour les boutons "power", "replay", et "pause"
power_button_rect = pygame.Rect(400, 5, 40, 40)
replay_button_rect = pygame.Rect(455, 5, 40, 40)
pause_button_rect = pygame.Rect(345, 5, 40, 40)

# Variable pour contrôler l'état de la musique
is_music_playing = True

# Boucle principale du jeu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            # Vérifier les touches enfoncées pour déplacer, tourner ou réinitialiser le jeu
            if game.game_over == True:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()
                game.update_score(0, 1)
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate()
        if event.type == GAME_UPDATE and game.game_over == False:
            # Mise à jour du jeu périodiquement
            game.move_down()

    # Dessin du jeu sur l'écran
    score_value_surface = title_font.render(str(game.score), True, Colors.white)
    screen.fill(Colors.dark_blue)

    # Dessiner les boutons power
    x = 40
    y = 40
    background_image = pygame.image.load("Image/power.jpg")
    background_image = pygame.transform.scale(background_image, (x, y))
    screen.blit(background_image, (400, 5))

    # Création bouton replay
    x = 40
    y = 40
    replay_image = pygame.image.load("Image/replay.jpg")
    replay_image = pygame.transform.scale(replay_image, (x, y))
    screen.blit(replay_image, (455, 5))

    # Création bouton pause music
    x = 40
    y = 40
    pause_image = pygame.image.load("Image/P.jpg")
    pause_image = pygame.transform.scale(pause_image, (x, y))
    screen.blit(pause_image, (345, 5))
    
    # Dessiner le texte du jeu
    screen.blit(texte_surface, (320, 60, 50, 50))
    screen.blit(score_surface, (340, 145, 50, 50))
    screen.blit(next_surface, (330, 390, 50, 50))

    if game.game_over == True:
        screen.blit(game_over_surface, (340, 300, 50, 50))
    
    # Dessiner le rectangle pour afficher le score et la pièce suivante
    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx=score_rect.centerx,
                                                                centery=score_rect.centery))
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
    
    # Dessiner les éléments du jeu (la grille, les pièces, etc.)
    game.draw(screen)

    # Vérifier si le bouton power est cliqué
    if pygame.mouse.get_pressed()[0] and power_button_rect.collidepoint(pygame.mouse.get_pos()):
        game.game_over = False
        game.reset()

    # Vérifier si le bouton replay est cliqué
    if game.game_over == True and replay_button_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        if pygame.mouse.get_pressed()[0]:
            game.game_over = False
            game.reset()

    # Vérifier si le bouton pause est cliqué
    if pygame.mouse.get_pressed()[0] and pause_button_rect.collidepoint(pygame.mouse.get_pos()):
        if is_music_playing:
            pygame.mixer.music.pause()  # Mettre en pause la musique
        else:
            pygame.mixer.music.unpause()  # Reprendre la musique
        is_music_playing = not is_music_playing  # Inverser l'état de la musique

    pygame.display.update()
    # Limiter la fréquence d'affichage à 60 images par seconde
    clock.tick(60)
