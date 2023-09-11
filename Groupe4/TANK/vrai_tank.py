import tkinter as tk
from PIL import Image, ImageTk
import math
import random

# Constantes
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
TANK_SIZE = 70
CANNON_LENGTH = 80
CANNON_WIDTH = 13
PROJECTILE_RADIUS = 8
TARGET_RADIUS = 30
VELOCITY = 30
GRAVITY = 0.5
DELTA_T = 20

# Variables globales
tank_x = CANVAS_WIDTH // 2
tank_y = CANVAS_HEIGHT - TANK_SIZE // 2
cannon_angle = 0
projectile = None
target_x = None
target_y = None
score = {
    "hit": 0,
    "shots": 0
}

# Chemins d'accès aux images
TANK_IMAGE_PATH = "Tank1.png"
TARGET_IMAGE_PATH = "avion-de-chasse.png"
EXPLOSION_IMAGE_PATH = "explosion.png"

# Redimensionnement des images
TANK_IMAGE_SIZE = (TANK_SIZE * 2, TANK_SIZE * 2)
TARGET_IMAGE_SIZE = (TARGET_RADIUS * 3, TARGET_RADIUS * 3)
EXPLOSION_IMAGE_SIZE = (TARGET_RADIUS * 4, TARGET_RADIUS * 4)

# Images du tank, de la cible et de l'explosion
tank_photo = None
target_photo = None
explosion_photo = None

# Temps d'attente pour afficher une nouvelle cible (en millisecondes)
NEW_TARGET_DELAY = 1000

# Fonction pour déplacer le tank en fonction de la position de la souris
def move_tank(event):
    global tank_x
    tank_x = event.x

# Fonction pour faire tourner le canon en fonction de la rotation de la molette de la souris
def rotate_cannon(event):
    global cannon_angle
    cannon_angle += event.delta / 120
    
    # Limiter la rotation du canon entre 0 et 180 degrés
    if cannon_angle < 0:
        cannon_angle = 0
    elif cannon_angle > 180:
        cannon_angle = 180


# Fonction pour tirer le projectile
def fire(event=None):
    global projectile, score
    if projectile is None:
        cannon_end_x = tank_x + CANNON_LENGTH * math.cos(math.radians(cannon_angle))
        cannon_end_y = tank_y - CANNON_LENGTH * math.sin(math.radians(cannon_angle))
        projectile = {
            "x": cannon_end_x,
            "y": cannon_end_y,
            "vx": VELOCITY * math.cos(math.radians(cannon_angle)),
            "vy": VELOCITY * math.sin(math.radians(cannon_angle))
        }
        score["shots"] += 1

# Fonction pour mettre à jour la position du projectile et détecter les collisions
def update_projectile():
    global projectile, target_x, target_y, score, explosion_photo
    if projectile is not None:
        projectile["x"] += projectile["vx"]
        projectile["y"] -= projectile["vy"]
        projectile["vy"] -= GRAVITY

        if (
            projectile["x"] < 0
            or projectile["x"] > CANVAS_WIDTH
            or projectile["y"] > CANVAS_HEIGHT
            or projectile["y"] <= 0
        ):
            projectile = None
        elif target_x is not None and target_y is not None and (
            math.sqrt((projectile["x"] - target_x)**2 + (projectile["y"] - target_y)**2)
            <= TARGET_RADIUS + PROJECTILE_RADIUS
        ):
            score["hit"] += 1
            # Afficher l'explosion
            canvas.itemconfig(target_image_id, image=explosion_photo)
            # Réinitialiser la position de la cible
            target_x = None
            target_y = None
            # Déclencher la création d'une nouvelle cible après un délai
            canvas.after(NEW_TARGET_DELAY, create_new_target)

# Fonction pour créer une nouvelle cible
def create_new_target():
    global target_x, target_y, target_photo
    target_x = random.randint(TARGET_RADIUS, CANVAS_WIDTH - TARGET_RADIUS)
    target_y = random.randint(TARGET_RADIUS, CANVAS_HEIGHT - TARGET_RADIUS)
    canvas.itemconfig(target_image_id, image=target_photo)

# Fonction pour dessiner les objets du jeu
def draw_objects():
    canvas.delete("all")

    # Dessin du canon
    cannon_end_x = tank_x + CANNON_LENGTH * math.cos(math.radians(cannon_angle))
    cannon_end_y = tank_y - CANNON_LENGTH * math.sin(math.radians(cannon_angle))
    canvas.create_line(tank_x, tank_y, cannon_end_x, cannon_end_y, width=CANNON_WIDTH, fill="#4B5320")

    # Chargement de l'image du tank (si non chargée)
    global tank_photo
    if tank_photo is None:
        tank_image = Image.open(TANK_IMAGE_PATH).resize(TANK_IMAGE_SIZE)
        tank_photo = ImageTk.PhotoImage(tank_image)
    
    # Chargement de l'image de la cible (si non chargée)
    global target_photo
    if target_photo is None:
        target_image = Image.open(TARGET_IMAGE_PATH).resize(TARGET_IMAGE_SIZE)
        target_photo = ImageTk.PhotoImage(target_image)
    
    # Chargement de l'image de l'explosion (si non chargée)
    global explosion_photo
    if explosion_photo is None:
        explosion_image = Image.open(EXPLOSION_IMAGE_PATH).resize(EXPLOSION_IMAGE_SIZE)
        explosion_photo = ImageTk.PhotoImage(explosion_image)

    # Affichage de l'image du tank
    tank_image_id = canvas.create_image(tank_x, tank_y, image=tank_photo)

    # Affichage de l'image de la cible
    global target_image_id
    if target_x is not None and target_y is not None:
        target_image_id = canvas.create_image(target_x, target_y, image=target_photo)

    # Dessin du projectile
    if projectile is not None:
        canvas.create_oval(projectile["x"] - PROJECTILE_RADIUS, projectile["y"] - PROJECTILE_RADIUS,
                           projectile["x"] + PROJECTILE_RADIUS, projectile["y"] + PROJECTILE_RADIUS,
                           fill="black")

    # Affichage du score
    score_text = "Score: {}/{} Projectiles".format(score["hit"], score["shots"])
    canvas.create_text(CANVAS_WIDTH // 2, 20, text=score_text, font=("Digital-7", 16), fill="red")

    # Mise à jour de la position du projectile et détection des collisions
    update_projectile()

    # Appel récursif pour les prochaines images
    canvas.after(DELTA_T, draw_objects)

# Création de la fenêtre principale
root = tk.Tk()
root.title("Tank Game")

# Création du canvas
canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="skyblue")
canvas.pack()

# Constante de la hauteur minimale pour la cible
MIN_TARGET_HEIGHT = 400

# Limite de position en y pour la cible
TARGET_Y_LIMIT = CANVAS_HEIGHT - TANK_SIZE - TARGET_RADIUS

# Génération des coordonnées de la cible
target_x = random.randint(TARGET_RADIUS, CANVAS_WIDTH - TARGET_RADIUS)
target_y = random.randint(MIN_TARGET_HEIGHT, TARGET_Y_LIMIT)

# Liaison des événements
canvas.bind("<Motion>", move_tank)
canvas.bind("<MouseWheel>", rotate_cannon)
canvas.bind("<Button-1>", lambda event: fire())

# Dessin des objets du jeu
draw_objects()

# Lancement de la boucle principale
root.mainloop()
