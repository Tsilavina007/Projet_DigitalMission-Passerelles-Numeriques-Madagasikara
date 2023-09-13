import pygame
import pygame_gui
import cv2
import numpy as np
import random

# Initialisez la capture vidéo à partir de la caméra
cap = cv2.VideoCapture(0)

# Fonction pour capturer l'image de la caméra
def capture_camera():
    ret, frame = cap.read()
    if ret:
        # Réajustez la taille de l'image de la caméra pour s'adapter à l'aperçu
        cam_image = cv2.resize(frame, (140, 120))
        return cv2.cvtColor(cam_image, cv2.COLOR_BGR2RGB)

# Initialisez le jeu Pygame
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Définition des constantes du jeu comme les dimensions, les couleurs,le temps
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CAR_WIDTH = 70
CAR_HEIGHT = 80
OBSTACLE_WIDTH = 30
OBSTACLE_HEIGHT = 30
FPS = 60
CAR_SPEED = 5
OBSTACLE_SPEED = 5
OBSTACLE_INTERVAL = 100
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Chargement des images de la voiture et de l'explosion
car_img = pygame.image.load("car.png")
car_img = pygame.transform.scale(car_img, (CAR_WIDTH, CAR_HEIGHT))
explosion_img = pygame.image.load("explosion.png") # l'imge de l'explosion
explosion_img = pygame.transform.scale(explosion_img, (100, 100)) # Coordonnee de l'image de l'explosion

# Liste des images d'explosion pour l'animation
explosion_frames = []
for i in range(8):
    x = i * 100
    if x + 100 <= explosion_img.get_width():
        explosion_frames.append(explosion_img.subsurface(pygame.Rect(x, 0, 100, 100)))

# Définition de la classe pour la voiture
class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = car_img
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= CAR_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += CAR_SPEED
        self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - CAR_WIDTH))

# Définition de la classe pour les obstacles
class Obstacle(pygame.sprite.Sprite):
    # Initialize des obstacles avec leurs dimensions
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
        self.image.fill(random.choice([RED, GREEN, BLUE]))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - OBSTACLE_WIDTH)
        self.rect.y = random.randint(-OBSTACLE_HEIGHT, 0)
    # l'adaptation des osbstacles
    def update(self):
        self.rect.y += OBSTACLE_SPEED
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.x = random.randint(0, SCREEN_WIDTH - OBSTACLE_WIDTH)
            self.rect.y = random.randint(-OBSTACLE_HEIGHT, 0)

class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = explosion_frames[0]
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.frame = 0
        self.animation_speed = 5  # Vitesse de l'animation (plus grand = plus lent)

    def update(self):
        # Gérer le changement d'images pour l'animation
        self.frame += 1
        if self.frame // self.animation_speed < len(explosion_frames):
            self.image = explosion_frames[self.frame // self.animation_speed]
        else:
            self.kill()  # Supprimer l'animation lorsque l'animation est terminée
            
# Définition de la classe pour l'écran d'accueil
class HomeScreen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.manager = pygame_gui.UIManager((width, height))
        self.intro_text = " Bienvenue chez M'Dôla !\n Appuyez sur le bouton pour commencer le jeu"  # Le \n signifie que en mettre à la ligne le texte apres
        self.start_button = None
        self.game_started = False  # Initialize game_started to False

    def create_ui(self):
        self.start_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((self.width // 2 - 100, self.height // 3), (200, 50)),
        text="Jouer",
        manager=self.manager)

    def update(self, time_delta):
        self.manager.update(time_delta)

    def draw(self, surface):
        surface.fill((99, 205, 227))
        self.manager.draw_ui(surface)
        font = pygame.font.SysFont("Kratos TrueType", 40)
        intro_text_render = font.render(self.intro_text, True, BLACK)
        screen.blit(
            intro_text_render, (width // 2 - intro_text_render.get_width() // 2, height // 2,)
        )


# Création de l'écran d'accueil (home screen)
home_screen = HomeScreen(width, height)
home_screen.create_ui()

# Création des groupes de sprites
all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()

# Création du joueur (voiture)
car = Car()
all_sprites.add(car)

# Définition des variables pour la détection de mouvement
bg_subtractor = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=16, detectShadows=False)
car_direction = None
car_speed = 5

# Boucle principale du jeu
running = True
clock = pygame.time.Clock()
obstacle_counter = 0
game_over = False

# Obtenir la liste des polices de caractères disponibles
pygame.font.init()
available_fonts = pygame.font.get_fonts()
font_name = "Super Salad"  # Vous pouvez changer le nom de la police selon celle disponible

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.USEREVENT and event.ui_element == home_screen.start_button:
            home_screen.game_started = True

        home_screen.manager.process_events(event)

    if not home_screen.game_started:
        home_screen.update(clock.get_time() / 1000)
        home_screen.draw(screen)
        pygame.display.flip()
        continue

    # Le jeu a commencé, exécutez le reste du code du jeu
    # Capturez l'image de la caméra
    ret, cam_image = cap.read()
    if not ret:
        continue

    # Capturez l'image de la caméra
    cam_image = capture_camera()

    # Convertir l'image en niveau de gris pour la détection de mouvement
    gray_cam_image = cv2.cvtColor(cam_image, cv2.COLOR_RGB2GRAY)

    # Appliquer un soustracteur de fond pour détecter le mouvement
    fg_mask = bg_subtractor.apply(gray_cam_image)

    # Identifier les contours pour détecter le mouvement
    contours, _ = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:
        # Trouver le plus grand contour (le plus grand mouvement détecté)
        largest_contour = max(contours, key=cv2.contourArea)

        # Trouver le rectangle englobant pour le plus grand contour
        x, y, w, h = cv2.boundingRect(largest_contour)

        # Déterminer la direction du mouvement de la voiture par rapport au centre de l'image
        cam_center_x = cam_image.shape[1] // 2
        if x + w // 2 < cam_center_x - 20:
            car_direction = "left"
        elif x + w // 2 > cam_center_x + 20:
            car_direction = "right"
        else:
            car_direction = None

    # Appliquer les actions de la caméra pour contrôler la voiture
    if car_direction == "left":
        car.rect.x += car_speed
    elif car_direction == "right":
        car.rect.x -= car_speed

    # Assurez-vous que la voiture reste dans les limites de l'écran
    car.rect.x = max(0, min(car.rect.x, SCREEN_WIDTH - CAR_WIDTH))

    # Gestion des obstacles
    obstacle_counter += 1
    if obstacle_counter >= OBSTACLE_INTERVAL:
        obstacle_counter = 0
        obstacle = Obstacle()
        all_sprites.add(obstacle)
        obstacles.add(obstacle)

    # Vérification des collisions entre la voiture et les obstacles
    hits = pygame.sprite.spritecollide(car, obstacles, False)
    if hits:
        if not game_over:
            game_over = True  # Le jeu est terminé en cas de collision

            # Explosion de la voiture
            car.kill()  # Retirer la voiture du groupe "all_sprites"
            explosion = Explosion(car.rect.centerx, car.rect.centery)
            all_sprites.add(explosion)  # Ajouter l'animation d'explosion au groupe "all_sprites"

    # Mise à jour des sprites
    all_sprites.update()

       # Affichage
    cam_surface = pygame.surfarray.make_surface(cam_image)

    # Rotation de l'image de la caméra de 90 degrés vers la droite
    cam_surface = pygame.transform.rotate(cam_surface, -90)

    screen.fill(BLACK)
    # Afficher le jeu Racing dans la partie gauche de l'écran
    all_sprites.draw(screen)

    # Afficher l'aperçu de la caméra centrée en haut
    cam_x = (width - cam_surface.get_width()) // 2
    cam_y = 30
    screen.blit(cam_surface, (cam_x, cam_y))

    # Afficher "Game Over" lorsque la collision se produit
    if game_over:
        font = pygame.font.SysFont("Super Salad", 100)
        game_over_text = font.render("Game Over", True, WHITE)
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 3))
        pygame.display.flip()
        pygame.time.delay(5000)  # Attendre 2 secondes avant de quitter le jeu
        running = False  # Exit the game loop after showing "Game Over"

    pygame.display.flip()
    clock.tick(FPS)

# Quitter Pygame
pygame.quit()
cap.release()
cv2.destroyAllWindows()
