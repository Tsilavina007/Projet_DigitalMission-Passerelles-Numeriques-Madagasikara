import pygame

pygame.init()

# Chargement du fichier audio
pygame.mixer.music.load("canoon+4.mp3")
pygame.mixer.music.set_volume(0.5)  # Réglage du volume de song1
pygame.mixer.music.play(-1)  # Répéter le morceau en continu

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Votre code supplémentaire ici

    pygame.time.Clock().tick(30)

