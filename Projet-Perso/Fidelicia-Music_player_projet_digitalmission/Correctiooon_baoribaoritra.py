import os  # Module pour travailler avec le système d'exploitation
import pickle  # Module pour la sérialisation des objets Python
import tkinter as tk  # Module pour la création de l'interface graphique
import random  # Module pour la génération de nombres aléatoires
from tkinter import (
    filedialog,
)  # Sous-module pour la boîte de dialogue de sélection de fichier/dossier
from tkinter import (
    PhotoImage,
)  # Sous-module pour charger des images dans l'interface graphique
from pygame import mixer  # Module pour la lecture de fichiers audio


# Classe principale pour le lecteur de musique
class Player(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="brown")
        self.master = master
        self.pack()

        mixer.init()

        if os.path.exists("songs.pickle"):
            with open("songs.pickle", "rb") as f:
                try:
                    self.playerlist = pickle.load(f)
                except EOFError:
                    self.playerlist = []

        else:
            self.playerlist = []

        self.current = 0
        self.paused = True
        self.played = False
        self.animate = True

        self.playerlist = []  # liste des chansons

        self.create_frames()  # Créer les cadres de l'interface
        self.track_widgets()  # Ajouter les éléments d'affichage de la piste
        self.control_widgets()  # Ajouter les éléments de contrôle
        self.tracklist_widgets()  # Ajouter la liste des chansons
        self.animate_text()  # Animer le texte de la piste

    def create_frames(self):
        # Crée le cadre pour la lecture de la piste
        self.track = tk.LabelFrame(
            self,
            text="Player music Fidelicia",
            font=("times new roman", 15, "bold"),
            bg="brown",
            fg="white",
            bd=5,
            relief=tk.GROOVE,
        )
        self.track.config(width=9000, height=200)
        self.track.grid(row=1, column=0)

        # Crée le cadre pour la liste de pistes
        self.tracklist = tk.LabelFrame(
            self,
            text=f"Liste de music - {str(len(self.playerlist))}",
            font=("times new roman", 15, "bold"),
            bg="brown",
            fg="white",
            bd=5,
            relief=tk.GROOVE,
        )

        self.tracklist.config(width=5000, height=500)
        self.tracklist.grid(row=1, column=2, rowspan=2, pady=10)

        # Crée le cadre pour les contrôles
        self.controls = tk.LabelFrame(
            self,
            font=("times new roman", 15, "bold"),
            bg="black",
            fg="white",
            bd=5,
            relief=tk.GROOVE,
        )
        self.controls.config(width=50, height=70)
        self.controls.grid(row=2, column=0, pady=3, padx=10)

        # Crée un trackbar pour suivre la lecture de la musique
        self.progressbar = tk.Scale(
            self.track,
            from_=0,
            to=100,
            orient=tk.HORIZONTAL,
            length=650,
            sliderlength=10,
            showvalue=False,
            command=self.set_music_position,
        )
        self.progressbar.grid(row=2, column=0, pady=10)

    def track_widgets(self):
        # Crée une étiquette pour l'affichage de la piste
        self.canvas = tk.Label(self.track, image=img)
        self.canvas.configure(width=550, height=240)
        self.canvas.grid(row=0, column=0)

        # Crée une étiquette pour afficher le nom de la piste en cours de lecture
        self.songtrack = tk.Label(
            self.track,
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="blue",
        )
        self.songtrack["text"] = "Music MP3 Player"
        self.songtrack.configure(width=40, height=2)
        self.songtrack.grid(row=1, column=0)

    def control_widgets(self):
        # Crée un bouton pour charger des chansons
        self.loadSongs = tk.Button(self.controls, bg="aqua", fg="black", font=5)
        self.loadSongs["text"] = "Charger des chansons"
        self.loadSongs["command"] = self.retrieve_songs
        self.loadSongs.grid(row=0, column=0, padx=10)

        # Crée un bouton pour passer à la chanson précédente
        self.prev = tk.Button(self.controls, image=prev)
        self.prev["command"] = self.prev_song
        self.prev.grid(row=0, column=1)

        # Crée un bouton pour mettre en pause/lecture de la chanson
        self.pause = tk.Button(self.controls, image=pause)
        self.pause["command"] = self.pause_song
        self.pause.grid(row=0, column=2)

        # Crée un bouton pour passer à la chanson suivante
        self.next_ = tk.Button(self.controls, image=next_)
        self.next_["command"] = self.next_song
        self.next_.grid(row=0, column=3)

        # Crée une échelle pour ajuster le volume
        self.volume = tk.DoubleVar()
        self.slider = tk.Scale(self.controls, from_=0, to=10, orient=tk.HORIZONTAL)
        self.slider["variable"] = self.volume
        self.slider.set(8)
        mixer.music.set_volume(0.8)
        self.slider["command"] = self.change_volume
        self.slider.grid(row=0, column=4, padx=10)

    def tracklist_widgets(self):
        # Crée une barre de défilement pour la liste de pistes
        self.scrollbar = tk.Scrollbar(self.tracklist, orient=tk.VERTICAL)
        self.scrollbar.grid(row=0, column=1, rowspan=5, sticky="ns")

        # Crée une liste pour afficher les noms des pistes
        self.list = tk.Listbox(
            self.tracklist,
            selectmode=tk.SINGLE,
            yscrollcommand=self.scrollbar.set,
            selectbackground="sky blue",
        )

        self.enumerate_songs()
        self.list.config(height=25)
        self.list.bind("<Double-1>", self.play_song)
        self.scrollbar.config(command=self.list.yview)
        self.list.grid(row=0, column=0, rowspan=5)

    def enumerate_songs(self):
        # Parcourt la liste des pistes et les ajoute à la liste
        for index, song in enumerate(self.playerlist):
            self.list.insert(index, os.path.basename(song))

    def retrieve_songs(self):
        # Demande à l'utilisateur de sélectionner un répertoire contenant des fichiers .mp3
        self.songlist = []
        directory = filedialog.askdirectory()
        for root_, dirs, files in os.walk(
            directory
        ):  # Parcourt le répertoire et ajoute les fichiers .mp3 à la liste des chansons
            for file in files:
                if os.path.splitext(file)[1] == ".mp3":
                    path = (root_ + "/" + file).replace("\\", "/")
                    self.songlist.append(path)

        with open(
            "songs.pickle", "wb"
        ) as f:  # Sauvegarde la liste des chansons dans un fichier pickle
            pickle.dump(self.songlist, f)

        self.playerlist = self.songlist
        self.tracklist["text"] = f"Playlist - {str(len(self.playerlist))}"
        self.list.delete(0, tk.END)
        self.enumerate_songs()

    def play_song(self, event=None):  # Joue la chanson sélectionnée
        if event is not None:
            self.current = self.list.curselection()[0]
        for i in range(len(self.playerlist)):
            self.list.itemconfigure(i, bg="white")

        mixer.music.load(self.playerlist[self.current])

        self.pause["image"] = play
        self.paused = False
        self.played = True
        self.songtrack["anchor"] = "w"
        self.songtrack["text"] = os.path.basename(self.playerlist[self.current])
        self.list.activate(self.current)
        self.list.itemconfigure(self.current, bg="sky blue")
        mixer.music.play()
        # Met à jour la position du trackbar en fonction de la position de la musique
        self.update_trackbar()

    # Méthode pour mettre à jour la position du trackbar en fonction de la position de la musique
    def update_trackbar(self):
        # Récupère la position de la musique en millisecondes
        current_position = mixer.music.get_pos()

        # Récupère la durée totale de la musique en millisecondes
        total_duration = mixer.Sound(self.playerlist[self.current]).get_length() * 1000

        # Calcule la position du trackbar en pourcentage
        progress = (current_position / total_duration) * 100

        # Met à jour la position du trackbar
        self.progressbar.set(progress)

        # Actualise la position du trackbar toutes les 1000 millisecondes (1 seconde)
        self.after(1000, self.update_trackbar)

    # Méthode pour définir la position de la musique en fonction de la position du trackbar
    def set_music_position(self, position):
        # Récupère la durée totale de la musique en millisecondes
        total_duration = mixer.Sound(self.playerlist[self.current]).get_length() * 1000

        # Calcule la nouvelle position de la musique en millisecondes
        new_position = (float(position) / 100) * total_duration

        # Définit la nouvelle position de la musique
        mixer.music.set_pos(new_position / 1000)

    def pause_song(self):  # Met en pause ou reprend la lecture de la chanson en cours
        if not self.paused:
            self.paused = True
            mixer.music.pause()
            self.pause["image"] = pause

        else:
            if self.played == False:
                self.play_song()
            self.paused = False
            mixer.music.unpause()
            self.pause["image"] = play

    def prev_song(self):  # Passe à la chanson précédente dans la liste
        if self.current > 0:
            self.current -= 1

        else:
            self.current = 0
        self.list.itemconfigure(self.current, bg="white")
        self.play_song()

    def next_song(self):  # Passe à la chanson suivante dans la liste
        if self.current < len(self.playerlist) - 1:
            self.current += 1

        else:
            self.current = 0
        self.list.itemconfigure(self.current + 1, bg="white")
        self.play_song()

    def change_volume(self, event=None):  # Modifie le volume de lecture de la musique
        self.v = self.volume.get()
        mixer.music.set_volume(self.v / 10)

    def animate_text(self):  # Anime le texte de la piste en cours de lecture
        current_text = self.songtrack["text"]
        new_text = current_text[1:] + current_text[:1]
        # Déplace le premier caractère à la fin
        self.songtrack["text"] = new_text
        self.songtrack.after(200, self.animate_text)


root = tk.Tk()
root.geometry("790x460")
root.configure(bg="brown")

root.wm_title("Lecteur MP3")

# Charge les images nécessaires pour les boutons et l'affichage de la piste
img = PhotoImage(file="Images/Fond1.gif")
next_ = PhotoImage(file="Images/next.png")
prev = PhotoImage(file="Images/preuv.png")
play = PhotoImage(file="Images/play.png")
pause = PhotoImage(file="Images/pause.png")

# Crée une instance de la classe Player
app = Player(master=root)
app.mainloop()
