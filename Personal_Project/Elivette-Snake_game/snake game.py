import pygame
import random #permet de travailler avec des nombres aléatoires de différentes manières
import pygame.mixer as mixer

# Initialisation de jeux
pygame.init()

# Dimensions de la fenêtre du jeu
largeur = 800
hauteur = 600

# initialisation des couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)
rouge = (255, 0, 0)
bleu_ciel = (135, 206, 235)
jaune = (255, 255, 0)
gris_clair = (200, 200, 200)
gris_fonce = (150, 150, 150)

# Création de la fenêtre
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Snake Game")

# entrer la musique dans le jeux
mixer.init()
mixer.music.load("hc.mp3")
mixer.music.play(-1)

def jeu():
    game_over = False # Variable pour contrôler si le jeu est terminé (True) ou non (False)
    game_quit = False # Variable pour contrôler si le joueur souhaite quitter le jeu (True) ou non (False)
    vitesse_serpent = 8 # Vitesse du serpent, qui peut être ajustée pour déterminer la rapidité

    # Position initiale du serpent
    x = largeur / 2
    y = hauteur / 2

    # Mouvement initial du serpent (ne bouge pas)
    deplacement_x = 0
    deplacement_y = 0

    # Liste des segments du serpent
    serpent = [] # cette code est qui peut stocke la liste de serpent à chaque fois qu'il mange la pomme
    longueur_serpent = 1 # initialisation de la longueur du serpent

    # Score initial
    score = 0

    # Position initiale de la pomme
    pomme_x = round(random.randrange(0, largeur - 10) / 10.0) * 10.0
    pomme_y = round(random.randrange(0, hauteur - 10) / 10.0) * 10.0

    # Boucle de jeu
    while not game_over:
        while game_quit:
            fenetre.fill(bleu_ciel)
            message("Appuyez sur Q pour quitter ou sur C pour continuer", noir)
            pygame.display.update()

            # Gestion des événements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_quit = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_quit = False
                    if event.key == pygame.K_c:
                        jeu()

        # Gestion des événements
# une boucle qui peut traiter les evenement de jeux( clavier ,clics,fermeture de jeux)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
# une condition vérifie que le touche du clavier a été enfoncée
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    deplacement_x = -10
                    deplacement_y = 0
                elif event.key == pygame.K_RIGHT:
                    deplacement_x = 10
                    deplacement_y = 0
                elif event.key == pygame.K_UP:
                    deplacement_y = -10
                    deplacement_x = 0
                elif event.key == pygame.K_DOWN:
                    deplacement_y = 10
                    deplacement_x = 0

        # Mise à jour de la position du serpent
        x += deplacement_x
        y += deplacement_y

        fenetre.fill(bleu_ciel)

        # Dessiner l'arrière-plan en carreaux
        for y_coord in range(0, hauteur, 20):
            for x_coord in range(0, largeur, 20):
                if (x_coord // 20 + y_coord // 20) % 2 == 0:
                    pygame.draw.rect(fenetre, gris_clair, [x_coord, y_coord, 20, 20])
                else:
                    pygame.draw.rect(fenetre, gris_fonce, [x_coord, y_coord, 20, 20])

        # Affichage de la pomme
        pygame.draw.rect(fenetre, rouge, [pomme_x, pomme_y, 10, 10])

        # Création du serpent
        serpent_tete = []
        serpent_tete.append(x)
        serpent_tete.append(y)
        serpent.append(serpent_tete)

        if len(serpent) > longueur_serpent:
            del serpent[0]

        # Vérification des collisions
        for segment in serpent[:-1]:
            if segment == serpent_tete:
                game_quit = True

        # Affichage du serpent
        for segment in serpent:
            pygame.draw.rect(fenetre, noir, [segment[0], segment[1], 10, 10])

        # Affichage du score
        font_style = pygame.font.SysFont(None, 30)
        texte = font_style.render("Score: " + str(score), True, noir)
        fenetre.blit(texte, [10, 10])

        pygame.display.update()

        # Gestion de la collision avec la pomme
        if x == pomme_x and y == pomme_y:
            pomme_x = round(random.randrange(0, largeur - 10) / 10.0) * 10.0
            pomme_y = round(random.randrange(0, hauteur - 10) / 10.0) * 10.0
            longueur_serpent += 3
            score += 10

        # Gestion de la collision avec les bords de l'écran
        if x >= largeur or x < 0 or y >= hauteur or y < 0:
            game_quit = True

        # Augmenter la vitesse lorsque le score atteint 50
        if score >= 50:
            vitesse_serpent += 0.04

        pygame.time.Clock().tick(vitesse_serpent)

    pygame.quit()

# Fonction pour afficher un message à l'écran
def message(msg, couleur):
    font_style = pygame.font.SysFont(None, 30)
    texte = font_style.render(msg, True, couleur)
    fenetre.blit(texte, [largeur / 6, hauteur / 3])

# Lancement du jeu
jeu()
