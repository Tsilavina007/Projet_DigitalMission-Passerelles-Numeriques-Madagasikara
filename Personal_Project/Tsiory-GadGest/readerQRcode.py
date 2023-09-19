import cv2
from pyzbar import pyzbar
import sqlite3
from datetime import datetime
import mysql.connector
import winsound

def lire_qr_code_en_direct():
    # Ouvrir la capture vidéo
    capture = cv2.VideoCapture(0)

    # Créer une connexion à la base de données SQLite
    conn = sqlite3.connect('db.sqlite')
    cursor = conn.cursor()

    # Liste des données déjà scannées
    donnees_scannees = []

    while True:
        
         # Utilisez fréquence et durée appropriées pour le bip souhaité
        frequence = 3000  # en hertz
        duree = 1000  # en millisecondes

   
        # Lire la frame vidéo
        ret, frame = capture.read()

        # Convertir la frame en échelle de gris
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Détecter et décoder les QR codes
        qr_codes = pyzbar.decode(gray)

        # Parcourir les QR codes détectés
        for qr_code in qr_codes:
            data = qr_code.data.decode('utf-8')
            print("Contenu du QR code:", data)

            # Vérifier si la donnée a déjà été scannée
            if data in donnees_scannees:
                print("La donnée a déjà été scannée.")
                
                #Emmettre le son bip
                winsound.Beep(frequence, duree)

                (x, y, w, h) = qr_code.rect
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                # Afficher le contenu du QR code à côté du rectangle
                cv2.putText(frame, data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            else:
                # Ajouter la donnée à la liste des données scannées
                donnees_scannees.append(data)

                # Dessiner un rectangle autour du QR code
                (x, y, w, h) = qr_code.rect
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                # Afficher le contenu du QR code à côté du rectangle
                cv2.putText(frame, data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                
                
                #Création du table
                cursor.execute('''CREATE TABLE IF NOT EXISTS present (etudiant TEXT,Date DATE,Heure TIME,Moment TEXT)''')
                temps=int(datetime.now().strftime("%H"))
                if (temps>0) and (temps<12):
                    # Insérer les données dans la table de la base de données
                    sql_insert = "INSERT INTO present (etudiant, Date,Heure,Moment) VALUES (?, ?, ?,?)"
                    values_insert = (data, datetime.now().strftime("%Y-%m-%d"),datetime.now().strftime("%H:%M"),"Matin")

                    cursor.execute(sql_insert, values_insert)   
                else:
                    # Insérer les données dans la table de la base de données
                    sql_insert = "INSERT INTO present (etudiant, Date,Heure,Moment) VALUES (?, ?, ?,?)"
                    values_insert = (data, datetime.now().strftime("%Y-%m-%d"),datetime.now().strftime("%H:%M"),"Après-Midi")

                    cursor.execute(sql_insert, values_insert)
                
                conn.commit()

        # Afficher la frame vidéo
        cv2.imshow('Lecture QR Code', frame)

        # Quitter la boucle si la touche 'q' est pressée
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Fermer la connexion à la base de données et libérer la capture vidéo
    cursor.close()
    conn.close()
    capture.release()
    cv2.destroyAllWindows()
# Appeler la fonction pour lire les QR codes en direct depuis la caméra
lire_qr_code_en_direct()
