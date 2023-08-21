
"""
import tkinter as tk
import math
import time

class Tank:
    def __init__(self):
        self.root = tk.Tk()
        self.root.resizable(width=False, height=False)
        self.canvas = tk.Canvas(self.root, width=800, height=450)
        self.canvas.pack()

        self.stick_length = 50
        self.stick_angle = 90

        self.tank_length = 100
        self.tank_width = 50
        self.tank_x = 430
        self.tank_y = 430

        self.caneau_y = self.tank_y - self.tank_width/2

        self.stick = self.canvas.create_line(self.tank_x, self.caneau_y, self.tank_x, self.caneau_y-50, width=7)  # Crée le bâton initial
        self.canvas.bind("<MouseWheel>", self.rotate_stick)  # Lier la molette de la souris à la fonction rotate_stick
        self.canvas.bind("<Button-1>", self.shoot)  # Lier le clic gauche de la souris à la fonction shoot

        # Dessiner la tourelle du réservoir
        self.reservoir = self.canvas.create_oval(self.tank_x -20, self.tank_y-50, self.tank_x+20, self.tank_y, fill="gray")

        self.tank = self.canvas.create_rectangle(self.tank_x - self.tank_length / 2, self.tank_y - self.tank_width / 2,
                                                 self.tank_x + self.tank_length / 2, self.tank_y + self.tank_width / 2,
                                                 fill="gray")  # Crée le tank initial

    def rotate_stick(self, event):
        delta = event.delta  # Obtient le déplacement de la molette de la souris
        angle = delta / 120  # Convertit le déplacement en angle

        self.stick_angle += angle  # Met à jour l'angle du bâton
        print(self.stick_angle)
        if self.stick_angle > 144:  # Limite l'inclinaison
            self.stick_angle = 144
        elif self.stick_angle < 36:
            self.stick_angle = 36

        new_x2 = self.tank_x - self.stick_length * math.cos(math.radians(self.stick_angle))
        new_y2 = self.caneau_y - self.stick_length * math.sin(math.radians(self.stick_angle))

        self.canvas.coords(self.stick, self.tank_x, self.caneau_y, new_x2, new_y2)  # Met à jour les coordonnées du bâton

    def shoot(self, event):
        ball_radius = 2
        ball_x = self.tank_x
        ball_y = self.caneau_y

        velocity = 12  # Vitesse initiale de la balle
        angle = self.stick_angle  # Angle du bâton
        angle_radians = math.radians(angle)  # Convertir l'angle en radians

        time_interval = 0.1  # Intervalle de temps entre les mises à jour de la position du boulet
        gravity = 9.8  # Accélération due à la gravité en m/s^2
        time1 = 0
        while ball_y <= 450 and ball_x <= 800:
            ball_x -= velocity * math.cos(angle_radians) * time1
            ball_y -= velocity * math.sin(angle_radians) * time1 - 0.5 * gravity * time1**2
            self.canvas.create_oval(ball_x - ball_radius, ball_y - ball_radius, ball_x + ball_radius, ball_y + ball_radius, fill="red", outline="")
            time1 += time_interval
            self.canvas.update()
            time.sleep(time_interval)  # Pause de 0.08 seconde pour ralentir le mouvement de la balle


    def start(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = Tank()
    app.start()
"""
"""
import tkinter as tk
import math
import time

class TrajectoryApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.resizable(width=False, height=False)
        self.canvas = tk.Canvas(self.root, width=800, height=450)
        self.canvas.pack()

        self.g = 9.8  # Accélération due à la gravité en m/s^2
        self.delta_t = 0.05  # Intervalle de temps entre les mises à jour de la position du boulet

    def calculate_trajectory(self, initial_velocity, launch_angle):
        x0 = 0  # Coordonnée x initiale du boulet
        y0 = self.canvas.winfo_height()  # Coordonnée y initiale du boulet

        velocity_x = initial_velocity * math.cos(math.radians(launch_angle))  # Vitesse selon l'axe x (constante)
        velocity_y = initial_velocity * math.sin(math.radians(launch_angle))  # Vitesse initiale selon l'axe y

        time1 = 0  # Temps écoulé depuis le tir du boulet

        while y0 > 0:
            x = x0 + velocity_x * time1
            y = y0 - velocity_y * time1 + 0.5 * self.g * time1**2

            self.canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill="black")  # Dessine le boulet

            time1 += self.delta_t
            self.canvas.update()
            time.sleep(self.delta_t)

    def start(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = TrajectoryApp()
    app.calculate_trajectory(initial_velocity=30, launch_angle=45)  # Exemple de trajectoire avec une vitesse initiale de 30 m/s et un angle de tir de 45 degrés
    app.start()
"""