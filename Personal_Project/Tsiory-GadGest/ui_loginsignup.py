from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets,QtCore,QtGui
import sys , rs
import sqlite3
import subprocess

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(848, 544)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(50, 20, 801, 481))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 771, 461))
        self.label.setCursor(QCursor(Qt.PointingHandCursor))
        self.label.setStyleSheet(u"border-image: url(:/images/fond.png);\n"
"border-radius:30px;\n"
"")
        self.graphicsView = QGraphicsView(self.widget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(70, 50, 291, 91))
        self.graphicsView.setStyleSheet(u"border-image: url(:/images/logo-fr.png);")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(140, 170, 201, 81))
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(25)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(100, 430, 331, 20))
        self.label_6.setStyleSheet(u"color:rgba(255,255,255,140);")
        self.pushButton_quit = QPushButton(self.widget)
        self.pushButton_quit.setObjectName(u"pushButton_quit")
        self.pushButton_quit.setGeometry(QRect(730, 30, 31, 31))
        font1 = QFont()
        font1.setFamily(u"Roboto Light")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.pushButton_quit.setFont(font1)
        self.pushButton_quit.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_quit.setStyleSheet(u"background-color: rgb(0, 85, 255);\n"
"color:white;\n"
"border-radius:15px;")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 200, 281, 281))
        self.label_5.setStyleSheet(u"border-image: url(:/images/My logo.png);")
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(430, 0, 351, 481))
        self.label_login = QLabel(self.widget_3)
        self.label_login.setObjectName(u"label_login")
        self.label_login.setGeometry(QRect(10, 20, 331, 441))
        self.label_login.setStyleSheet(u"background-color:rgba(0,0,0,100);\n"
"border-radius:20px;")
        self.label_login_2 = QLabel(self.widget_3)
        self.label_login_2.setObjectName(u"label_login_2")
        self.label_login_2.setGeometry(QRect(80, 60, 221, 31))
        font2 = QFont()
        font2.setFamily(u"Roboto")
        font2.setPointSize(23)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_login_2.setFont(font2)
        self.label_login_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lineEdit_user = QLineEdit(self.widget_3)
        self.lineEdit_user.setObjectName(u"lineEdit_user")
        self.lineEdit_user.setGeometry(QRect(80, 150, 200, 40))
        self.lineEdit_user.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:None;\n"
"border-bottom:1px solid rgba(155,158,252,255);\n"
"color:rgba(255,255,255,250);\n"
"padding-bottom:2px;")
        self.lineEdit_password = QLineEdit(self.widget_3)
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setGeometry(QRect(80, 240, 200, 40))
        self.lineEdit_password.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:None;\n"
"border-bottom:1px solid rgba(155,158,252,255);\n"
"color:rgba(255,255,255,250);\n"
"padding-bottom:2px;")
        self.pushButton_login = QPushButton(self.widget_3)
        self.pushButton_login.setObjectName(u"pushButton_login")
        self.pushButton_login.setGeometry(QRect(60, 330, 221, 40))
        font3 = QFont()
        font3.setFamily(u"Roboto")
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.pushButton_login.setFont(font3)
        self.pushButton_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_login.setStyleSheet(u"#pushButton_login{\n"
"	\n"
"	\n"
"	background-color: rgb(0, 170, 255);\n"
"	color: rgba(255, 255, 255, 210);\n"
"	border-radius: 20px;\n"
"\n"
"}\n"
"#pushButton_login:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0.487025, y1:0.063, x2:0.461874, y2:1, stop:0 rgba(40, 67, 98, 158), stop:1 rgba(105, 118, 132, 226));\n"
"	}\n"
"#pushButton_login:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color:rgba(105,118,132,200);\n"
"\n"
"}")
        self.pushButton_signupgo = QPushButton(self.widget_3)
        self.pushButton_signupgo.setObjectName(u"pushButton_signupgo")
        self.pushButton_signupgo.setGeometry(QRect(130, 390, 75, 23))
        self.pushButton_signupgo.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_signupgo.setStyleSheet(u"text-decoration:underline;\n"
"background-color:transparent;\n"
"color:white;")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(320, 10, 461, 471))
        self.label_signup = QLabel(self.widget_2)
        self.label_signup.setObjectName(u"label_signup")
        self.label_signup.setGeometry(QRect(140, 10, 311, 441))
        self.label_signup.setStyleSheet(u"background-color:rgba(0,0,0,100);\n"
"border-radius:20px;")
        self.label_signup_2 = QLabel(self.widget_2)
        self.label_signup_2.setObjectName(u"label_signup_2")
        self.label_signup_2.setGeometry(QRect(220, 50, 151, 31))
        self.label_signup_2.setFont(font2)
        self.label_signup_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lineEdit_user_signup = QLineEdit(self.widget_2)
        self.lineEdit_user_signup.setObjectName(u"lineEdit_user_signup")
        self.lineEdit_user_signup.setGeometry(QRect(180, 130, 221, 40))
        self.lineEdit_user_signup.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:None;\n"
"border-bottom:1px solid rgba(155,158,252,255);\n"
"color:rgba(255,255,255,250);\n"
"padding-bottom:2px;")
        self.lineEdit_password_signup = QLineEdit(self.widget_2)
        self.lineEdit_password_signup.setEchoMode(QLineEdit.Password)
        self.lineEdit_password_signup.setObjectName(u"lineEdit_password_signup")
        self.lineEdit_password_signup.setGeometry(QRect(180, 190, 221, 40))
        self.lineEdit_password_signup.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:None;\n"
"border-bottom:1px solid rgba(155,158,252,255);\n"
"color:rgba(255,255,255,250);\n"
"padding-bottom:2px;")
        self.lineEdit_codedadministration = QLineEdit(self.widget_2)
        self.lineEdit_codedadministration.setObjectName(u"lineEdit_codedadministration")
        self.lineEdit_codedadministration.setGeometry(QRect(180, 250, 221, 40))
        self.lineEdit_codedadministration.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:None;\n"
"border-bottom:1px solid rgba(155,158,252,255);\n"
"color:rgba(255,255,255,250);\n"
"padding-bottom:2px;")
        self.pushButton_signup = QPushButton(self.widget_2)
        self.pushButton_signup.setObjectName(u"pushButton_signup")
        self.pushButton_signup.setGeometry(QRect(180, 330, 231, 40))
        self.pushButton_signup.setFont(font3)
        self.pushButton_signup.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_signup.setStyleSheet(u"#pushButton_signup{\n"
"	\n"
"	background-color: rgb(0, 170, 255);\n"
"	color: rgba(255, 255, 255, 210);\n"
"	border-radius: 20px;\n"
"\n"
"}\n"
"#pushButton_signup:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0.487025, y1:0.063, x2:0.461874, y2:1, stop:0 rgba(40, 67, 98, 158), stop:1 rgba(105, 118, 132, 226));\n"
"	}\n"
"#pushButton_signup:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color:rgba(105,118,132,200);\n"
"\n"
"}")
        self.pushButton_logingo = QPushButton(self.widget_2)
        self.pushButton_logingo.setObjectName(u"pushButton_logingo")
        self.pushButton_logingo.setGeometry(QRect(240, 390, 101, 23))
        self.pushButton_logingo.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_logingo.setStyleSheet(u"text-decoration:underline;\n"
"background-color:transparent;\n"
"color:white;")
        self.label.raise_()
        self.label_4.raise_()
        self.label_6.raise_()
        self.label_5.raise_()
        self.widget_3.raise_()
        self.widget_2.raise_()
        self.pushButton_quit.raise_()
        self.graphicsView.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 848, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        
        self.widget_2.hide()
        self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=0,yOffset=0,color=QtGui.QColor(234,221,186,100)))
        self.label_4.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=0,yOffset=0,color=QtGui.QColor(105,118,186,100)))
        self.pushButton_quit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=3,yOffset=3,color=QtGui.QColor(105,118,132,100)))
        
        
        
        self.pushButton_signup.clicked.connect(self.signup_insert)
        self.pushButton_logingo.clicked.connect(self.goto_login)
        self.pushButton_signupgo.clicked.connect(self.goto_signup)
        self.pushButton_quit.clicked.connect(self.quitWindow)
        self.pushButton_login.clicked.connect(self.connect)
                
        # Créez une connexion à la base de données SQLite
        self.conn = sqlite3.connect('db.sqlite')  # Remplacez 'user_about.db' par le nom de votre base de données SQLite
        self.cursor = self.conn.cursor()
        
        
        #Pour le déplacement de la fenetrE
        MainWindow.mouseMoveEvent = ui.moveWindow
        

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
    
    
    def connect(self):
            # Récupérez les valeurs des champs entry_name et entry_password
                username = self.lineEdit_user.text()
                password = self.lineEdit_password.text()
                
                # Créez la table "users" si elle n'existe pas déjà
                query = """
                CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL
                )
                """
                self.cursor.execute(query)
                self.conn.commit()

                # Vérifiez les informations dans la base de données
                query = "SELECT * FROM users WHERE username=? AND password=?"
                self.cursor.execute(query, (username, password))

                result = self.cursor.fetchone()

                if result:
                        QMessageBox.information(MainWindow, "Connexion réussie", "Connexion réussie!")
                         
                        # Fermer la fenêtre actuelle
                        MainWindow.close()
                        # Ouvrir une nouvelle fenêtre qui est le main_interface
                        subprocess.Popen([sys.executable, "main_izy.py"])
                
                else:
                        QMessageBox.warning(MainWindow, "Erreur de connexion", "Nom d'utilisateur ou mot de passe incorrect!")
                        
    def signup_insert(self):
                # Récupérez les valeurs des champs entry_name et entry_password
                username = self.lineEdit_user_signup.text()
                password = self.lineEdit_password_signup.text()
                codeadmin=self.lineEdit_codedadministration.text()
                
                # Créez la table "users" si elle n'existe pas déjà
                query = """
                CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AU TOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL
                )
                """
                self.cursor.execute(query)
                self.conn.commit()
                
                keypass="GP.2023.persoProjetTsiory"
                if codeadmin==keypass:
                        # Insérez les informations dans la base de données
                        query = "INSERT INTO users (username, password) VALUES (?, ?)"
                        self.cursor.execute(query, (username, password))
                        self.conn.commit()
                        QMessageBox.information(MainWindow, "Inscription ", "Inscription réussie!")
                        self.widget_2.hide()
                        self.widget_3.show()
                         
                else:
                        if username=="" or password=="" or codeadmin=="":
                                QMessageBox.warning(MainWindow, "Erreur d'inscription", "Veuillez remplir tous les champs ")
                        
                        else:        
                                QMessageBox.warning(MainWindow, "Erreur d'inscription", "Code d'Administration Invalide ")
                
    def goto_signup(self):
                self.widget_3.hide()
                self.widget_2.show()
                
    def goto_login(self):
                self.widget_2.hide()
                self.widget_3.show()
        
    #fonction pour le déplacement de la fenetre
    def mousePressEvent(self,event):
                print("mousePressEvent triggered")

                #Prendre la postion actuelle de la souris
                self.clickPosition = event.globalPos()

    def mouseMoveEvent(self, event):
            if event.buttons() == QtCore.Qt.LeftButton and self.clickPosition is not None:
                MainWindow.move(MainWindow.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()
    def moveWindow(self, event):
                if MainWindow.isMaximized() == False:
                        if event.buttons() == Qt.LeftButton:
                                MainWindow.move(MainWindow.pos() + event.globalPos() - self.clickPosition)
                                self.clickPosition = event.globalPos()
                                event.accept()

                
    def quitWindow(self):
                MainWindow.close()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Bienvenue\n"
"      sur", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Copyright \u00a9 2023 TSIORY. Tous droits r\u00e9serv\u00e9s.", None))
        self.pushButton_quit.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.label_5.setText("")
        self.label_login.setText("")
        self.label_login_2.setText(QCoreApplication.translate("MainWindow", u"Se connecter", None))
        self.lineEdit_user.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nom d'utilisateur", None))
        self.lineEdit_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Mot de pass", None))
        self.pushButton_login.setText(QCoreApplication.translate("MainWindow", u"Se connecter", None))
        self.pushButton_signupgo.setText(QCoreApplication.translate("MainWindow", u"S'inscrire?", None))
        self.label_signup.setText("")
        self.label_signup_2.setText(QCoreApplication.translate("MainWindow", u"S'inscrire", None))
        self.lineEdit_user_signup.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nom d'utilisateur", None))
        self.lineEdit_password_signup.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Mot de pass", None))
        self.lineEdit_codedadministration.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Code d'administration", None))
        self.pushButton_signup.setText(QCoreApplication.translate("MainWindow", u"S'inscrire", None))
        self.pushButton_logingo.setText(QCoreApplication.translate("MainWindow", u"Se connecter?", None))
    # retranslateUi
    
    
    
                

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()  # Utilisez QMainWindow au lieu de QWidget
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.mousePressEvent = ui.mousePressEvent  # Ajoutez cette ligne

    MainWindow.show()  # Utilisez MainWindow
    sys.exit(app.exec_())
