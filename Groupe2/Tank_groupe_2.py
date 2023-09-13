import tkinter as tk
import math
import random

# Constantes
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 700
TARGET_RADIUS = 18
CANNON_LENGTH = 50
BALL_RADIUS = 5
INITIAL_VELOCITY = 450  # Augmentez cette valeur pour une vitesse de boulet plus rapide
GRAVITY = 1
DELTA_T = 30
MAX_BULLETS = 5

# Variables
tank_x = CANVAS_WIDTH / 2
tank_y = CANVAS_HEIGHT - 20
cannon_angle = 45
target_x = random.randint(TARGET_RADIUS, CANVAS_WIDTH - TARGET_RADIUS)
target_y = random.randint(TARGET_RADIUS, CANVAS_HEIGHT - TARGET_RADIUS)
target_hit = False
score = 0
shots_fired = 0
bullets = []
is_bullet_fired = False

# Variable pour le compte à rebours en secondes
countdown_timer = 30

# Variable pour stocker le temps ajouté à chaque cible touchée
time_added_per_target = 3  # Ajoutez 3 secondes à chaque cible touchée

root = tk.Tk()
root.title("Tank Game")
root.geometry("1000x800")

canvas = tk.Canvas(root, width=1000, height=700, bg="white")
canvas.pack()

canvas.focus_set()

# Liste pour stocker les balles et leurs angles initiaux
bullets = []

# Fonction pour dessiner le tank
def draw_tank():
    tank_top_x = tank_x - 20
    tank_top_y = tank_y - 10
    tank_bottom_x = tank_x + 20
    tank_bottom_y = tank_y + 10

    cannon_x = tank_x + CANNON_LENGTH * math.cos(math.radians(cannon_angle))
    cannon_y = tank_y - CANNON_LENGTH * math.sin(math.radians(cannon_angle))

    canvas.delete("tank")
    canvas.create_rectangle(tank_top_x, tank_top_y, tank_bottom_x, tank_bottom_y, fill="gray", tags="tank")
    canvas.create_line(tank_x, tank_y, cannon_x, cannon_y, width=5, fill="black", tags="tank")

# Fonction pour dessiner la cible
def draw_target():
    global target_x, target_y, target_hit
    fill_color = "red" if target_hit else "green"
    canvas.delete("target")
    canvas.create_oval(target_x - TARGET_RADIUS, target_y - TARGET_RADIUS, target_x + TARGET_RADIUS, target_y + TARGET_RADIUS, fill=fill_color, tags="target")

# Fonction pour dessiner le boulet
def draw_bullet(x, y):
    bullet = canvas.create_oval(x - BALL_RADIUS, y - BALL_RADIUS, x + BALL_RADIUS, y + BALL_RADIUS, fill="black", tags="bullet")
    return bullet

# Fonction pour dessiner la trajectoire du boulet avec des petits traits
def draw_trajectory(cannon_x, cannon_y, x, y):
    # Dessiner une ligne reliant le bout du canon au boulet
    canvas.create_line(cannon_x, cannon_y, x, y, fill="blue", tags="trajectory")

# Fonction pour effacer la trajectoire du boulet
def clear_trajectory():
    canvas.delete("trajectory")

def calculate_trajectory():
    global tank_x, tank_y, cannon_angle, target_x, target_y, target_hit, score, shots_fired, is_bullet_fired, countdown_timer

    if not is_bullet_fired:
        is_bullet_fired = True
        initial_x = tank_x + CANNON_LENGTH * math.cos(math.radians(cannon_angle))
        initial_y = tank_y - CANNON_LENGTH * math.sin(math.radians(cannon_angle))
        # Sauvegarder l'angle initial dans une liste
        bullets.append([initial_x, initial_y, cannon_angle])

    time_counter = 0

    while bullets:
        bullet = bullets[0]
        x = bullet[0] + INITIAL_VELOCITY * time_counter / 1000 * math.cos(math.radians(bullet[2]))
        y = bullet[1] - (INITIAL_VELOCITY * time_counter / 1000 * math.sin(math.radians(bullet[2])) - 0.5 * GRAVITY * (time_counter / 1000) ** 2)

        # Créer une nouvelle balle s'il n'y a pas déjà de boulet dessiné
        if len(bullet) < 4:
            bullet.append(draw_bullet(x, y))
            draw_trajectory(bullet[0], bullet[1], x, y)

        canvas.coords(bullet[3], x - BALL_RADIUS, y - BALL_RADIUS, x + BALL_RADIUS, y + BALL_RADIUS)

        if x < 0 or x > CANVAS_WIDTH or y < 0 or y > CANVAS_HEIGHT:
            canvas.delete(bullet[3])
            bullets.pop(0)
            is_bullet_fired = False
            clear_trajectory()  # Effacer la trajectoire si le boulet dépasse les limites du canvas
            break
            
        if math.sqrt((x - target_x) ** 2 + (y - target_y) ** 2) <= TARGET_RADIUS:
            target_hit = True
            score += 1
            canvas.delete(bullet[3])
            bullets.pop(0)
            is_bullet_fired = False
            draw_target()
            # Changer la position de la cible après un impact
            target_x = random.randint(TARGET_RADIUS, CANVAS_WIDTH - TARGET_RADIUS)
            target_y = random.randint(TARGET_RADIUS, CANVAS_HEIGHT - TARGET_RADIUS)
            draw_target()
            clear_trajectory()  # Effacer la trajectoire après un impact

            # Ajouter le temps au compteur
            countdown_timer += time_added_per_target

            # Mettre à jour l'affichage du score et du temps
            canvas.itemconfig(score_text, text="Score: {}".format(score))
            canvas.itemconfig(timer_text, text="Time: {} s".format(countdown_timer))

            break

        time_counter += DELTA_T
        canvas.update()
        canvas.after(DELTA_T)

    # Défaite si le compteur atteint 0
    if countdown_timer <= 0:
        canvas.create_text(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2, text="Game Over! You Lose!", font=("Helvetica", 30), fill="red")
        is_bullet_fired = True  # Pour bloquer les tirs après le Game Over




def update_timer():
    global countdown_timer, is_bullet_fired
    if countdown_timer > 0:
        countdown_timer -= 1
        canvas.itemconfig(timer_text, text="Time: {} s".format(countdown_timer))
        canvas.after(1000, update_timer)  # Appeler la fonction après 1 seconde (1000 ms)
    else:
        canvas.create_text(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2, text="Game Over! You Lose!", font=("Helvetica", 30), fill="red")
        is_bullet_fired = True  # Pour bloquer les tirs après le Game Over


def mouse_click(event):
    global countdown_timer, is_bullet_fired, shots_fired
    if countdown_timer > 0 and not is_bullet_fired and len(bullets) < MAX_BULLETS:
        calculate_trajectory()
        shots_fired += 1  # Compteur de balles tirées

# Fonction pour gérer le déplacement vers la gauche
def move_left(event):
    global tank_x
    tank_x -= 10
    draw_tank()

# Fonction pour gérer le déplacement vers la droite
def move_right(event):
    global tank_x
    tank_x += 10
    draw_tank()

# Fonction pour gérer le mouvement de la molette de la souris pour changer l'angle du canon
def mouse_wheel(event):
    global cannon_angle
    if event.delta > 0:  
        if cannon_angle < 180:  
            cannon_angle += 3
    else:  
        if cannon_angle > 0:  
            cannon_angle -= 3
    draw_tank()

timer_text = canvas.create_text(40, 40, text="Time: {} s".format(countdown_timer), font=("Helvetica", 12), anchor=tk.W)

score_text = canvas.create_text(40, 60, text="Score: {}".format(score), font=("Helvetica", 12), anchor=tk.W)

draw_tank()
draw_target()

canvas.bind("<Left>", move_left)
canvas.bind("<Right>", move_right)

canvas.bind("<Button-1>", mouse_click)
canvas.bind("<MouseWheel>", mouse_wheel)

# Lancer le compte à rebours
update_timer()

root.mainloop()

