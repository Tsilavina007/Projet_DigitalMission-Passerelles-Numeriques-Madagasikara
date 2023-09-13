import pygame
from pygame.locals import *
import random

pygame.init()

# créer la fenêtre
largeur = 500
hauteur = 500
taille_ecran = (largeur, hauteur)
ecran = pygame.display.set_mode(taille_ecran)
pygame.display.set_caption('Jeu de Voiture')

# couleurs
gris = (100, 100, 100)
vert = (76, 208, 56)
rouge = (200, 0, 0)
blanc = (255, 255, 255)
jaune = (255, 232, 0)

# tailles de la route et des marqueurs
largeur_route = 300
largeur_marqueur = 10
hauteur_marqueur = 50

# coordonnées des voies
voie_gauche = 150
voie_centre = 250
voie_droite = 350
voies = [voie_gauche, voie_centre, voie_droite]

# route et marqueurs d'extrémité
route = (100, 0, largeur_route, hauteur)
marqueur_gauche = (95, 0, largeur_marqueur, hauteur)
marqueur_droit = (395, 0, largeur_marqueur, hauteur)

# pour animer le mouvement des marqueurs de voie
deplacement_y_marqueur_voie = 0

# coordonnées de départ du joueur
joueur_x = 250
joueur_y = 400

# paramètres du cadre
horloge = pygame.time.Clock()
fps = 120

# paramètres du jeu
partie_terminee = False
vitesse = 2
score = 0
#Véhicule dans le jeu
class Vehicule(pygame.sprite.Sprite):

    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)

        # redimensionner l'image pour qu'elle ne dépasse pas la largeur de la voie
        echelle_image = 45 / image.get_rect().width
        nouvelle_largeur = image.get_rect().width * echelle_image
        nouvelle_hauteur = image.get_rect().height * echelle_image
        self.image = pygame.transform.scale(image, (nouvelle_largeur, nouvelle_hauteur))

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
#Véhicule du joueur
class VehiculeJoueur(Vehicule):

    def __init__(self, x, y):
        image = pygame.image.load('images/car.png')
        super().__init__(image, x, y)

# groupes de sprites
groupe_joueur = pygame.sprite.Group()
groupe_vehicules = pygame.sprite.Group()

# créer la voiture du joueur
joueur = VehiculeJoueur(joueur_x, joueur_y)
groupe_joueur.add(joueur)

# charger les images des véhicules
noms_fichiers_images = ['pickup_truck.png', 'semi_trailer.png', 'taxi.png', 'van.png']
images_vehicules = []
for nom_fichier_image in noms_fichiers_images:
    image = pygame.image.load('images/' + nom_fichier_image)
    images_vehicules.append(image)

# charger l'image du crash
crash = pygame.image.load('images/crash.png')
rect_crash = crash.get_rect()

# boucle du jeu
en_cours = True
while en_cours:

    horloge.tick(fps)

    for evenement in pygame.event.get():
        if evenement.type == QUIT:
            en_cours = False

        # déplacer la voiture du joueur avec les touches gauche/droite du clavier
        if evenement.type == KEYDOWN:

            if evenement.key == K_LEFT and joueur.rect.center[0] > voie_gauche:
                joueur.rect.x -= 100
            elif evenement.key == K_RIGHT and joueur.rect.center[0] < voie_droite:
                joueur.rect.x += 100

            # vérifier s'il y a une collision latérale après avoir changé de voie
            for vehicule in groupe_vehicules:
                if pygame.sprite.collide_rect(joueur, vehicule):

                    partie_terminee = True

                    # placer la voiture du joueur à côté de l'autre véhicule
                    # et déterminer où positionner l'image du crash
                    if evenement.key == K_LEFT:
                        joueur.rect.left = vehicule.rect.right
                        rect_crash.center = [joueur.rect.left, (joueur.rect.center[1] + vehicule.rect.center[1]) / 2]
                    elif evenement.key == K_RIGHT:
                        joueur.rect.right = vehicule.rect.left
                        rect_crash.center = [joueur.rect.right, (joueur.rect.center[1] + vehicule.rect.center[1]) / 2]

    # dessiner l'herbe
    ecran.fill(vert)

    # dessiner la route
    pygame.draw.rect(ecran, gris, route)

    # dessiner les marqueurs d'extrémité
    pygame.draw.rect(ecran, jaune, marqueur_gauche)
    pygame.draw.rect(ecran, jaune, marqueur_droit)

    # dessiner les marqueurs de voie
    deplacement_y_marqueur_voie += vitesse * 2
    if deplacement_y_marqueur_voie >= hauteur_marqueur * 2:
        deplacement_y_marqueur_voie = 0
    for y in range(hauteur_marqueur * -2, hauteur, hauteur_marqueur * 2):
        pygame.draw.rect(ecran, blanc, (voie_gauche + 45, y + deplacement_y_marqueur_voie, largeur_marqueur, hauteur_marqueur))
        pygame.draw.rect(ecran, blanc, (voie_centre + 45, y + deplacement_y_marqueur_voie, largeur_marqueur, hauteur_marqueur))

    # dessiner la voiture du joueur
    groupe_joueur.draw(ecran)

    # ajouter un véhicule
    if len(groupe_vehicules) < 2:

        # s'assurer qu'il y a suffisamment d'espace entre les véhicules
        ajouter_vehicule = True
        for vehicule in groupe_vehicules:
            if vehicule.rect.top < vehicule.rect.height * 1.5:
                ajouter_vehicule = False

        if ajouter_vehicule:
            # choisir une voie aléatoire
            voie = random.choice(voies)

            # choisir une image de véhicule aléatoire
            image = random.choice(images_vehicules)
            vehicule = Vehicule(image, voie, hauteur / -2)
            groupe_vehicules.add(vehicule)

    # faire bouger les véhicules
    for vehicule in groupe_vehicules:
        vehicule.rect.y += vitesse

        # supprimer le véhicule une fois qu'il sort de l'écran
        if vehicule.rect.top >= hauteur:
            vehicule.kill()

            # ajouter au score
            score += 1

            # accélérer le jeu après avoir passé 10 véhicules
            if score > 0 and score % 10 == 0:
                vitesse += 1

    # dessiner les véhicules
    groupe_vehicules.draw(ecran)

    # afficher le score
    police = pygame.font.Font(pygame.font.get_default_font(), 16)
    texte = police.render('Score : ' + str(score), True, blanc)
    rect_texte = texte.get_rect()
    rect_texte.center = (50, 400)
    ecran.blit(texte, rect_texte)

    # vérifier s'il y a une collision frontale
    if pygame.sprite.spritecollide(joueur, groupe_vehicules, True):
        partie_terminee = True
        rect_crash.center = [joueur.rect.center[0], joueur.rect.top]

    # afficher "game over"
    if partie_terminee:
        ecran.blit(crash, rect_crash)

        pygame.draw.rect(ecran, rouge, (0, 50, largeur, 100))

        police = pygame.font.Font(pygame.font.get_default_font(), 16)
        texte = police.render('Partie terminée. Jouer de nouveau ? (Appuyez sur Y ou N)', True, blanc)
        rect_texte = texte.get_rect()
        rect_texte.center = (largeur / 2, 100)
        ecran.blit(texte, rect_texte)

    pygame.display.update()

    # attendre la saisie de l'utilisateur pour rejouer ou quitter
    while partie_terminee:

        horloge.tick(fps)

        for evenement in pygame.event.get():

            if evenement.type == QUIT:
                partie_terminee = False
                en_cours = False

            # obtenir la saisie de l'utilisateur (y ou n)
            if evenement.type == KEYDOWN:
                if evenement.key == K_y:
                    # réinitialiser le jeu
                    partie_terminee = False
                    vitesse = 2
                    score = 0
                    groupe_vehicules.empty()
                    joueur.rect.center = [joueur_x, joueur_y]
                elif evenement.key == K_n:
                    # quitter la boucle du jeu
                    partie_terminee = False
                    en_cours = False

pygame.quit()
