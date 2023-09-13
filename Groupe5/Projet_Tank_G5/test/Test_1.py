"""
import tkinter as tk
import random
import math

# Création de la fenêtre
window = tk.Tk()
canvas = tk.Canvas(window, width=800, height=450)
canvas.pack()
window.resizable(width=False, height=False)
window.title("Tank")

# Déclaration de la variable image en tant que globale
image = tk.PhotoImage(file="rocket.png")      # Chargement de l'image PNG
resized_image = image.subsample(10, 10)  # Modifier la taille de l'image


def create_image():
    global resized_image
    # Coordonnées de la fusée
    x = random.randint(10, 200)  # Position aléatoire en x
    y = random.randint(10, 200)  # Position aléatoire en y

    # Affichage de l'image
    canvas.create_image(x, y, image=resized_image)
"""
import tkinter as tk
import math
import time
import random
is_shooting = None

# Variables pour le tank
tank_length = 100
tank_width = 50
tank_x = 400
tank_y = 400

# Variables pour le bâton
stick_length = 50
angle = 90

# Variables pour le ballon
balloon_color = "blue"
balloon_size = 20
balloon_x = random.randint(10, 790)  # Position aléatoire en x
balloon_y = random.randint(200, 400)  # Position aléatoire en y

# Variables de suivi du score et des tirs
score = 0
num_shots = 0

# Objets graphiques dans le canvas
tank = None
stick = None
balloon = None
score_text = None
shot_text = None

def shoot(event):
    global ballon, text, score, tire, nb_tire, ov, new_tank_x, nb_score, canvas, is_shooting
    if is_shooting:  # vérifier la valeur de is_shooting avant d'exécuter le tir
        return

    tire += 1
    print(f"Nombre de tire = {tire}")
    canvas.delete(nb_tire)
    nb_tire = canvas.create_text(70, 20, text=f"Nombre de tires = {tire}", font=("Arial", 10))
    try:
        canvas.delete(ov)
        canvas.delete(text)
    except:
        pass
    try:
        ball_x = new_tank_x - stick_length * math.cos(math.radians(angle))
        ball_y = caneau_y - stick_length * math.sin(math.radians(angle))
    except:
        ball_x = tank_x - stick_length * math.cos(math.radians(angle))
        ball_y = caneau_y - stick_length * math.sin(math.radians(angle))

    ball_radius = 3
    velocity = 11  # Vitesse initiale de la balle
    angle_radians = math.radians(angle)  # Convertir l'angle en radians

    time_interval = 0.053  # Intervalle de temps entre les mises à jour de la position du boulet
    gravity = 9.8  # Accélération due à la gravité en m/s^2
    time1 = 0
    is_shooting = True
    while ball_y <= 450 and ball_x <= 800 and is_shooting == True:
        ball_x -= velocity * math.cos(angle_radians) * time1
        ball_y -= velocity * math.sin(angle_radians) * time1 - 0.5 * gravity * time1 ** 2
        ov = canvas.create_oval(ball_x - ball_radius, ball_y - ball_radius, ball_x + ball_radius,
                                          ball_y + ball_radius, fill="red", outline="")
        time1 += time_interval
        canvas.update()
        time.sleep(time_interval)  # Pause de 0.08 seconde pour ralentir le mouvement de la balle
        canvas.delete(ov)
        if (x < ball_x and (x + 20) > ball_x) and (y < ball_y and (y + 20) > ball_y):
            print("boom")
            score += 1
            canvas.delete(ballon)
            ov = canvas.create_oval(ball_x - ball_radius, ball_y - ball_radius, ball_x + ball_radius,
                                              ball_y + ball_radius, fill="red", outline="")
            canvas.delete(ov)
            explode_balloon(ball_x, ball_y)
            text = canvas.create_text(400, 200, text="Boom!", font=("Arial", 30))
            canvas.delete(nb_score)
            nb_score = canvas.create_text(200, 20, text=f"Score = {score}", font=("Arial", 10))
            create_balloon()
            is_shooting = False

    canvas.delete(ballon)
    create_balloon()
    is_shooting = False  # Réinitialiser la variable de contrôle

def rotate_stick(event):
    global new_tank_x, new_x2, new_y2, ov, angle, nb_angle, stick
    delta = event.delta  # Obtient le déplacement de la molette de la souris
    angle += delta / 120  # Convertit le déplacement en angle

    canvas.delete(nb_angle)
    nb_angle = canvas.create_text(43, 100, text=f"Angle = {angle}", font=("Arial", 10))
    if angle > 144:  # Limite l'inclinaison
        angle = 144
    elif angle < 36:
        angle = 36

    try:  # Mettre à jour les coordonnées du bâton
        new_x2 = new_tank_x - stick_length * math.cos(math.radians(angle))
        new_y2 = caneau_y - stick_length * math.sin(math.radians(angle))
        canvas.coords(stick, new_tank_x, caneau_y, new_x2, new_y2)
    except:
        new_x2 = tank_x - stick_length * math.cos(math.radians(angle))
        new_y2 = caneau_y - stick_length * math.sin(math.radians(angle))
        canvas.coords(stick, tank_x, caneau_y, new_x2, new_y2)

def move_tank(event):
    global new_tank_x, ov, text, resized_image, tank, reservoir
    try:
        canvas.delete(text)
    except:
        pass
    new_tank_x = event.x  # Coordonnée x de la position de la souris
    canvas.coords(tank, new_tank_x - tank_length / 2, tank_y - tank_width / 2,
                       new_tank_x + tank_length / 2,
                       tank_y + tank_width / 2)  # Met à jour les coordonnées du tank
    canvas.coords(reservoir, new_tank_x - 20, tank_y - 50, new_tank_x + 20, tank_y)

    new__x2 = new_tank_x - stick_length * math.cos(math.radians(angle))
    new__y2 = caneau_y - stick_length * math.sin(math.radians(angle))
    canvas.coords(stick, new_tank_x, caneau_y, new__x2, new__y2)

def create_balloon():
    global ballon, av, x, y, color, size, canvas
    try:
        canvas.delete(av)
    except:
        pass
    x = random.randint(10, 790)  # Position aléatoire en x
    y = random.randint(200, 400)  # Position aléatoire en y
    colors = ["red", "blue", "green", "yellow", "orange", "purple"]  # Couleurs disponibles
    sizes = [20]  # Tailles disponibles

    color = random.choice(colors)  # Couleur aléatoire
    size = random.choice(sizes)  # Taille aléatoire

    ballon = canvas.create_oval(x, y, x + size, y + size, fill=color, outline="")  # Création du ballon

def explode_balloon(x, y):
    global ov, canvas
    canvas.delete(ov)  # Supprimer le ballon existant

    # Afficher l'animation d'explosion à la place du ballon
    explosion_radius = 3

    # Créer une liste pour stocker les identifiants des particules d'explosion
    explosion_particles = []

    for i in range(25):
        explosion_radius = explosion_radius + 1
        explosion_particle = canvas.create_oval(x - explosion_radius, y - explosion_radius,
                                                     x + explosion_radius,
                                                     y + explosion_radius, fill=color, outline="")
        explosion_particles.append(explosion_particle)
        canvas.update()

    # Planifier la suppression de toutes les particules après une seconde
    canvas.after(50, delete_explosion_particles, explosion_particles)

def delete_explosion_particles(explosion_particles):
    global canvas
    for particle in explosion_particles:
        canvas.delete(particle)

def shoot(event):
    global ballon, text, score, new_tank_x, ov, av, x, y, color, size, canvas, nb_tire, tire, nb_score, score, is_shooting
    if is_shooting:  # vérifier la valeur de is_shooting avant d'exécuter le tir
        return
    global new_tank_x, ov, av
    tire += 1
    print(f"Nombre de tire = {tire}")
    canvas.delete(nb_tire)
    nb_tire = canvas.create_text(70, 20, text=f"Nombre de tires = {tire}", font=("Arial", 10))
    try:
        canvas.delete(ov)
        canvas.delete(text)
    except:
        pass
    try:
        ball_x = new_tank_x - stick_length * math.cos(math.radians(angle))
        ball_y = caneau_y - stick_length * math.sin(math.radians(angle))
    except:
        ball_x = tank_x - stick_length * math.cos(math.radians(angle))
        ball_y = caneau_y - stick_length * math.sin(math.radians(angle))

    ball_radius = 3
    velocity = 11  # Vitesse initiale de la balle
    angle_radians = math.radians(angle)  # Convertir l'angle en radians

    time_interval = 0.053  # Intervalle de temps entre les mises à jour de la position du boulet
    gravity = 9.8  # Accélération due à la gravité en m/s^2
    time1 = 0
    is_shooting = True
    while ball_y <= 450 and ball_x <= 800 and is_shooting == True:
        ball_x -= velocity * math.cos(angle_radians) * time1
        ball_y -= velocity * math.sin(angle_radians) * time1 - 0.5 * gravity * time1 ** 2
        ov = canvas.create_oval(ball_x - ball_radius, ball_y - ball_radius, ball_x + ball_radius,
                                          ball_y + ball_radius, fill="red", outline="")
        time1 += time_interval
        canvas.update()
        time.sleep(time_interval)  # Pause de 0.08 seconde pour ralentir le mouvement de la balle
        canvas.delete(ov)
        if (x < ball_x and (x + 20) > ball_x) and (y < ball_y and (y + 20) > ball_y):
            print("boom")
            score += 1
            canvas.delete(ballon)
            ov = canvas.create_oval(ball_x - ball_radius, ball_y - ball_radius, ball_x + ball_radius,
                                          ball_y + ball_radius, fill="red", outline="")
            canvas.delete(ov)
            explode_balloon(ball_x, ball_y)
            text = canvas.create_text(400, 200, text="Boom!", font=("Arial", 30))
            canvas.delete(nb_score)
            nb_score = canvas.create_text(200, 20, text=f"Score = {score}", font=("Arial", 10))
            create_balloon()
            is_shooting = False

    canvas.delete(ballon)
    create_balloon()
    is_shooting = False  # Réinitialiser la variable de contrôle

def delete_oval():
    global canvas, ov
    canvas.delete(ov)

def start():
    global root, canvas
    root = tk.Tk()
    root.title("Tir au ballon")
    canvas = tk.Canvas(root, width=800, height=500)
    canvas.pack()
    canvas.create_line(0, 450, 800, 450)
    canvas.create_line(0, 500, 800, 500)
    create_balloon()
    create_balloon()

    canvas.bind("<B1-Motion>", move_tank)  # Déplacer le tank avec la souris
    canvas.bind("<Button-1>", shoot)  # Tirer avec le bouton gauche de la souris
    canvas.bind("<MouseWheel>", rotate_stick)  # Tourner le bâton avec la molette de la souris

    root.mainloop()

start()
