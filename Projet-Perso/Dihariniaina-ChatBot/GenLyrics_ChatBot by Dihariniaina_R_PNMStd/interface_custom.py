from tkinter import *
import datetime
from fonctions import *

BG_Gray = "#ABB2B9"
BG_Color = "#17202A"
Text_color = "#EAECEE"
FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

class Chatbot: 
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("ChatGen Lyrics")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=470, height=550, bg=BG_Color)

        # Head label 
        head_label = Label(self.window, bg=BG_Color, fg=Text_color, text="Welcome to the chatGen Lyrics!", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)

        # Tiny divider
        line = Label(self.window, width=450, bg=BG_Color)
        line.place(relwidth=2, rely=0.07, relheight=0.012)

        # Text widget
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_Color, fg=Text_color, font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # Scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)

        # Bottom label 
        bottom_label = Label(self.window, bg=BG_Gray, height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        # Message entry box
        self.msg_entry = Entry(bottom_label, bg="#2C3E50", fg=Text_color, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.0011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        # Send button
        sent_button = Button(bottom_label, text="SEND", font=FONT_BOLD, width=20, bg=BG_Gray, command=self._on_enter_pressed)
        sent_button.place(relwidth=0.22, relheight=0.06, relx=0.77, rely=0.008)

    """def _on_enter_pressed(self, event=None):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")
        self._insert_message(self.chatbot_response(msg), "Machine")"""
    def _on_enter_pressed(self, event=None):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")
        self._insert_message(self.chatbot_response(msg), "Machine")
        self.msg_entry.delete(0, END)  # Effacer le contenu de l'entrée utilisateur après l'envoi


    def _insert_message(self, msg, sender):
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, f"{sender}: {msg}\n\n")
        self.text_widget.configure(state=DISABLED)
    """def _insert_message(self, msg, sender):
        self.text_widget.configure(state=NORMAL)
        self.text_widget.delete('1.0', END)  # Effacer le contenu actuel du widget Text
        self.text_widget.insert(END, f"{sender}: {msg}\n\n")
        self.text_widget.configure(state=DISABLED)"""

#Réponse du chatbot
    def chatbot_response(self, user_message):
        user_message = user_message.lower()

        if any(keyword in user_message for keyword in ['bonjour', 'salut', 'hi', 'hello']):
            response = "Bonjour, Je suis Tononkira, votre assistante génératrice de Lyrics.\n" + "Comment ça va ? Comment puis-je vous aider ?"

        elif 'heure' in user_message:
            heure = datetime.datetime.now().strftime("%H:%M")
            response = f"Il est {heure}"

        elif any(keyword in user_message for keyword in ['merci', 'okay', 'ok','Misaotra']):
            response = "Je vous en prie"

        elif 'nom' in user_message or 'appelles' in user_message:
            response = "Je me nomme Tonokira"

        elif any(keyword in user_message for keyword in ['liste', 'mpihira', 'chanteur', 'isany', 'combien']):
            response = f"{df.Mpihira.value_counts}"

        elif any(keyword in user_message for keyword in ['parole', 'tononkira', 'lyrics', 'tonony', 'suite','chansons']):
            response = "Merci d'entrer alors votre mots clé"

        elif any(keyword in user_message for keyword in generate_lyrics(user_message)):
            lyrics = generate_lyrics(user_message)  # Appel de la fonction generate_lyrics
            response = f"{lyrics}"  # Utilisation des paroles générées 
        else:
            response = "Je suis navrée, je ne comprends pas"
        
        return response

    def handle_submit(self, sender):
        user_message = self.msg_entry.value
        response = self.chatbot_response(user_message)

        with self.text_widget:
            print(f"You: {user_message}\n")
            print(f"Tononkira Chatbot: {response}\n")


if __name__ == "__main__":
    app = Chatbot()
    app.run()
