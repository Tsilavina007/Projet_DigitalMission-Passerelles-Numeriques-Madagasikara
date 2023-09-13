import tkinter.messagebox
import tkinter as tk
root = tk.Tk()

translations = {
    "Malgache": {
        "title": "Tank",  # Translation for the title
        "label1": "Anarana",  # Translation for label1
        "label2": "Kaody",  # Translation for label2
        "button": "Ilalao",  # Translation for the button
        "new_player": "Mpilalao vaovao?",  # Translation for new_player
        "language_changed": "Niova Malagasy ny fiteny"  # Translation for language changed message
    },
    "Francais": {
        "title": "Tank",  # Translation for the title
        "label1": "pseudo",  # Translation for label1
        "label2": "mot de passe",  # Translation for label2
        "button": "Jouer",  # Translation for the button
        "new_player": "Nouveau joueur?",  # Translation for new_player
        "language_changed": "Langue changée en Français"  # Translation for language changed message
    },
    "Anglais": {
        "title": "Tank",  # Translation for the title
        "label1": "username",  # Translation for label1
        "label2": "password",  # Translation for label2
        "button": "Play",  # Translation for the button
        "new_player": "New player?",  # Translation for new_player
        "language_changed": "Language changed to English"  # Translation for language changed message
    }
}


current_language = "Malgache"  # Default language


def change_language(language):
    global translation
    global current_language, translation
    if language in translations:
        current_language = language
        update_ui()

def update_ui():
    global translations, bouton, nv
    global label1, label2, root
    # Update the labels and other elements with translations based on the current language
    root.title(translations[current_language]["title"])
    label1['text']=translations[current_language]["label1"]
    label2['text']=translations[current_language]["label2"]
    bouton.config(text=translations[current_language]["button"])
    nv.config(text=translations[current_language]["new_player"])


def langue_malgache():
    change_language("Malgache")
    tkinter.messagebox.showinfo("Language", translations[current_language]["language_changed"])

def langue_Francais():
    change_language("Francais")
    tkinter.messagebox.showinfo("Language", translations[current_language]["language_changed"])

def langue_Anglais():
    change_language("Anglais")
    tkinter.messagebox.showinfo("Language", translations[current_language]["language_changed"])
