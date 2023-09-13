# ce module fournit des fonctionnalités et des variables liées au système
import sys
# python text to speech:  bibliothèque Python qui permet la synthèse vocale
import pyttsx3
# facilite la reconnaissance vocale.
import speech_recognition as sr
# facilite certaines tâches communes telles que la lecture de vidéos YouTube, la recherche sur Google,
import pywhatkit
import datetime
import wikipedia
# sélection aléatoire
import random

# 1er partie: initialisation de l'assistante virtuelle
listener = sr.Recognizer()
engine = pyttsx3.init()
# concernant la voix
engine.setProperty("voice", "french")
engine.setProperty("rate", 170)

# 2e partie:creation de la fonction qui va repondre:
def talk(text):
    engine.say(text)
    engine.runAndWait() #elle attend quelques seconde avant de repondre

# 3e partie : la fonction qui va repondre l'heure actuel programmé selon le moment de la journée
def greetme():
    current_hour = int(datetime.datetime.now().hour) #pour qu'elle prend l'heure de ce moment meme
    if 0 <= current_hour < 12:
        talk ("Bonjour mademoiselle Fenitra")

    if 12 <= current_hour < 18:
        talk("Bon après-midi mademoiselle")

    if current_hour >= 18 and current_hour != 0:
        talk("Bonsoir Harijaona Fenitra")

# parametrer la voix feminine française:
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
greetme()
engine.say("Comment vas-tu en ce moment?")
engine.runAndWait()

#l'user demande a alexa : recoit la demande de l'user
def alexa_command():
    with sr.Microphone() as source:
        print("en attente...")
        listener.pause_threshold = 1 #le temps qu'elle prendra avant de me repondre: ici 1 seconde
        voice = listener.listen(source)
        command = listener.recognize_google(voice, language="fr-FR") #la voix qu'elle reconnaitra: ici francais
        # transforme la commande en miniscule
        command = command.lower()
        print(command)
        # condition: l'utilisateur dit "alexa": alexa fait partie de la commande
        if "alexa" in command:
            command = command.replace("alexa", "")
            print(command)
    return command

# execution des taches
def run_alexa():
    command = alexa_command()

# playonyt= play on you tube: c'est sur you tube qu'elle va prendre la musique que je lui demande
    if "musique" in command:
        song = command.replace("musique", "").strip()
        talk("musique en cours...")
        pywhatkit.playonyt(song)

# cela ca indiquer l'heure et la minute actuelle
    elif "heure" in command:
        time = datetime.datetime.now().strftime("%H:%M") #l'heure qu'elle donne va être sous cette forme par exemple 16:32
        print(time)
        talk("il est actuellement: " + time)

# faire recherche sur wikipedia
    elif "qui est" in command:
        # person = command.replace("qui est", "")
        person = command.split("qui est ", 1)[-1].strip()
        wikipedia.set_lang("fr")
        # info = wikipedia.summary(person, 1)  # retourne une seule phrase
        # en cas d'erreurs:
        try:
            info = wikipedia.summary(person, 1)  # Obtenir un bref résumé sur la personne
            talk(info)
        except wikipedia.exceptions.DisambiguationError as e:
            talk("Je ne suis pas sûr de la personne dont vous parlez. Veuillez être plus précis.")
        except wikipedia.exceptions.PageError as e:
            talk("Désolé, je n'ai pas trouvé d'informations sur cette personne.")

# pour lui demander des choses
    elif "sortir" in command:
        talk("Desolé, je suis un peu occupé en ce moment")
    elif "es-tu en couple" in command:
        talk("non, mon coeur est encore a personne")
    elif " une blague" in command:
        jokes = ["la maitresse demande a toto de conjuguer le verbe marcher au present, et il le conjugue:je je marche,tu ...tu marches, mais la maitresse le presse et lui dit, plus vite, et il dit je cours, tu cours"
                   ]
        talk(random.choice(jokes))
# A chaque fois qu'elle capte: "et toi" elle va repondr a l'un des deux aleatoirement.
    elif "et toi" in command:
        msgs = ["je fais juste mon truc!", "je vais bien"]
        talk(random.choice(msgs))
#un commnde qui va lui ordonner de se desactiver par elle même.
    elif "desactive-toi" in command:
        talk("merci de m'avoir utilisée")
        sys.exit()
# si ce que je dis n'est pas dans la commande, elle va dire ceci.
    else:
        talk("répète un peu, je n'ai pas bien compris")

# l'execution du code
if __name__ == '__main__':
    while True:
        run_alexa()