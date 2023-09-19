# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainkNTcVV.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
from PySide2 import QtCore, QtGui, QtWidgets
import sqlite3
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2 import QtCore
from data_student import data_name
import subprocess
import qdarkstyle
import icon_rc
from PySide2.QtCore import QDateTime
from datetime import datetime, timedelta

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1279, 696)
        self.root=MainWindow
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Background = QFrame(self.centralwidget)
        self.Background.setObjectName(u"Background")
        self.Background.setStyleSheet(qdarkstyle.load_stylesheet())
        self.Background.setFrameShape(QFrame.StyledPanel)
        self.Background.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.Background)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Header = QFrame(self.Background)
        self.Header.setObjectName(u"Header")
        self.Header.setMinimumSize(QSize(0, 30))
        self.Header.setMaximumSize(QSize(16777215, 30))
        self.Header.setStyleSheet(u"*{color:#fff;\n"
"background-color: rgb(10, 10, 10);\n"
"border:none;\n"
"}\n"
"QPushButton{color:#fff;\n"
"background-color:transparent;\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:white;\n"
"border:none;\n"
"}\n"
"\n"
"")
        self.Header.setFrameShape(QFrame.StyledPanel)
        self.Header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.Header)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.Header)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_26 = QLabel(self.frame_2)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(20, 0))
        self.label_26.setMaximumSize(QSize(30, 16777215))
        self.label_26.setStyleSheet(u"border-image: url(:/images/images/3-removebg-preview.png);")

        self.horizontalLayout_4.addWidget(self.label_26)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 25))
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(0, 191, 255);")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label)


        self.horizontalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.Header)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 35))
        self.frame_3.setMaximumSize(QSize(16777215, 35))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 7, 0)
        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        icon = QIcon()
        icon.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(16, 16))

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.pushButton_6 = QPushButton(self.frame_3)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMaximumSize(QSize(16, 16777215))
        self.pushButton_6.setStyleSheet(u"border-image: url(:/icons/icons/square.svg);")

        self.horizontalLayout_3.addWidget(self.pushButton_6)

        self.pushButton_3 = QPushButton(self.frame_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QSize(16, 16))

        self.horizontalLayout_3.addWidget(self.pushButton_3)


        self.horizontalLayout_2.addWidget(self.frame_3, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout.addWidget(self.Header, 0, Qt.AlignTop)

        self.Main = QFrame(self.Background)
        self.Main.setObjectName(u"Main")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Main.sizePolicy().hasHeightForWidth())
        self.Main.setSizePolicy(sizePolicy1)
        self.Main.setFrameShape(QFrame.StyledPanel)
        self.Main.setFrameShadow(QFrame.Raised)
        self.frame_4 = QFrame(self.Main)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(0, 0, 41, 701))
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setMinimumSize(QSize(0, 346))
        self.frame_4.setStyleSheet(u"background-color: rgb(10, 10, 10);\n"
"color: rgb(255, 255, 255);\n"
"border:None;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.toolButton = QToolButton(self.frame_4)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(5, 5, 100, 23))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton.setIcon(icon2)
        self.toolButton.setIconSize(QSize(25, 25))
        self.toolButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.button_1 = QToolButton(self.frame_4)
        self.button_1.setObjectName(u"button_1")
        self.button_1.setGeometry(QRect(5, 50, 100, 23))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/folder-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_1.setIcon(icon3)
        self.button_1.setIconSize(QSize(25, 25))
        self.button_1.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.button_2 = QToolButton(self.frame_4)
        self.button_2.setObjectName(u"button_2")
        self.button_2.setGeometry(QRect(5, 80, 100, 23))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/monitor.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_2.setIcon(icon4)
        self.button_2.setIconSize(QSize(25, 25))
        self.button_2.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.toolButton_4 = QToolButton(self.frame_4)
        self.toolButton_4.setObjectName(u"toolButton_4")
        self.toolButton_4.setGeometry(QRect(5, 110, 100, 23))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/database.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_4.setIcon(icon5)
        self.toolButton_4.setIconSize(QSize(25, 25))
        self.toolButton_4.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.toolButton_5 = QToolButton(self.frame_4)
        self.toolButton_5.setObjectName(u"toolButton_5")
        self.toolButton_5.setGeometry(QRect(5, 140, 100, 23))
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/calendar.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_5.setIcon(icon6)
        self.toolButton_5.setIconSize(QSize(25, 25))
        self.toolButton_5.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.toolButton_6 = QToolButton(self.frame_4)
        self.toolButton_6.setObjectName(u"toolButton_6")
        self.toolButton_6.setGeometry(QRect(10, 610, 101, 23))
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_6.setIcon(icon7)
        self.toolButton_6.setIconSize(QSize(25, 25))
        self.toolButton_6.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.frame_5 = QFrame(self.Main)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(40, 0, 1360, 760))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.stackedWidget = QStackedWidget(self.frame_5)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 0, 1321, 701))
        font1 = QFont()
        font1.setPointSize(22)
        self.stackedWidget.setFont(font1)
        self.stackedWidget.setStyleSheet(u"background-color:transparent;")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.tableWidget = QTableWidget(self.page_1)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(40, 340, 591, 291))
        font2 = QFont()
        font2.setFamily(u"Roboto")
        self.tableWidget.setFont(font2)
        self.tableWidget.setStyleSheet(u"")
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2 = QTableWidget(self.page_1)
        if (self.tableWidget_2.columnCount() < 2):
            self.tableWidget_2.setColumnCount(2)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(650, 340, 551, 291))
        self.tableWidget_2.setStyleSheet(u"")
        self.calendarWidget = QCalendarWidget(self.page_1)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(650, 70, 371, 201))
        self.calendarWidget.setStyleSheet(u"")
        self.label_2 = QLabel(self.page_1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 290, 121, 31))
        font3 = QFont()
        font3.setFamily(u"Arial Rounded MT Bold")
        font3.setPointSize(15)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setUnderline(True)
        font3.setWeight(50)
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"color: rgb(0, 191, 255);")
        self.label_4 = QLabel(self.page_1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(700, 290, 81, 31))
        font4 = QFont()
        font4.setFamily(u"Arial Rounded MT Bold")
        font4.setPointSize(15)
        font4.setBold(False)
        font4.setUnderline(True)
        font4.setWeight(50)
        self.label_4.setFont(font4)
        self.label_4.setStyleSheet(u"color: rgb(0, 191, 255);")
        self.label_5 = QLabel(self.page_1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(480, 10, 251, 71))
        font5 = QFont()
        font5.setPointSize(20)
        self.label_5.setFont(font5)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.comboBox = QComboBox(self.page_1)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(208, 170, 221, 41))
        font6 = QFont()
        font6.setPointSize(15)
        self.comboBox.setFont(font6)
        self.comboBox.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(430, 30, 461, 101))
        self.label_3.setFont(font5)
        self.label_3.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.pushButton_demarrer = QPushButton(self.page_2)
        self.pushButton_demarrer.setObjectName(u"pushButton_demarrer")
        self.pushButton_demarrer.setGeometry(QRect(540, 210, 241, 81))
        self.pushButton_demarrer.setStyleSheet(u"color:#fff;\n"
"background-color: rgb(0, 191, 255);\n"
"border-radius:20px;")
        self.label_22 = QLabel(self.page_2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(440, 410, 491, 101))
        self.label_22.setFont(font6)
        self.label_22.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"")
        self.label_6 = QLabel(self.page_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(470, 10, 351, 51))
        self.label_6.setFont(font5)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_8 = QLabel(self.page_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(40, 80, 47, 13))
        self.label_8.setStyleSheet(u"	color: rgb(255, 255, 255);")
        self.label_9 = QLabel(self.page_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(290, 80, 61, 16))
        self.label_9.setStyleSheet(u"	color: rgb(255, 255, 255);")
        self.label_10 = QLabel(self.page_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(40, 170, 121, 16))
        self.label_10.setStyleSheet(u"	color: rgb(255, 255, 255);")
        self.label_11 = QLabel(self.page_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(1030, 90, 47, 13))
        self.label_11.setStyleSheet(u"	color: rgb(255, 255, 255);")
        self.label_12 = QLabel(self.page_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(800, 90, 47, 13))
        self.label_12.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_13 = QLabel(self.page_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(540, 90, 47, 13))
        self.label_13.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_14 = QLabel(self.page_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(290, 170, 61, 16))
        self.label_14.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_15 = QLabel(self.page_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(540, 170, 47, 13))
        self.label_15.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_16 = QLabel(self.page_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(800, 170, 61, 16))
        self.label_16.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_17 = QLabel(self.page_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(1030, 170, 51, 16))
        self.label_17.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_ajouter = QPushButton(self.page_3)
        self.pushButton_ajouter.setObjectName(u"pushButton_ajouter")
        self.pushButton_ajouter.setGeometry(QRect(110, 260, 191, 23))
        self.pushButton_ajouter.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);\n"
"border-radius:10px;")
        self.pushButton_modifier = QPushButton(self.page_3)
        self.pushButton_modifier.setObjectName(u"pushButton_modifier")
        self.pushButton_modifier.setGeometry(QRect(430, 260, 181, 23))
        self.pushButton_modifier.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);\n"
"border-radius:10px;")
        self.pushButton_supprimer = QPushButton(self.page_3)
        self.pushButton_supprimer.setObjectName(u"pushButton_supprimer")
        self.pushButton_supprimer.setGeometry(QRect(744, 260, 171, 23))
        self.pushButton_supprimer.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);\n"
"border-radius:10px;")
        self.pushButton_reinitialiser = QPushButton(self.page_3)
        self.pushButton_reinitialiser.setObjectName(u"pushButton_reinitialiser")
        self.pushButton_reinitialiser.setGeometry(QRect(1040, 260, 171, 23))
        self.pushButton_reinitialiser.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);\n"
"border-radius:10px;")
        self.lineEdit_nom = QLineEdit(self.page_3)
        self.lineEdit_nom.setObjectName(u"lineEdit_nom")
        self.lineEdit_nom.setGeometry(QRect(40, 120, 201, 20))
        self.lineEdit_prenom = QLineEdit(self.page_3)
        self.lineEdit_prenom.setObjectName(u"lineEdit_prenom")
        self.lineEdit_prenom.setGeometry(QRect(292, 120, 181, 20))
        self.lineEdit_sexe = QLineEdit(self.page_3)
        self.lineEdit_sexe.setObjectName(u"lineEdit_sexe")
        self.lineEdit_sexe.setGeometry(QRect(542, 120, 191, 20))
        self.lineEdit_age = QLineEdit(self.page_3)
        self.lineEdit_age.setObjectName(u"lineEdit_age")
        self.lineEdit_age.setGeometry(QRect(802, 120, 161, 20))
        self.lineEdit_tel = QLineEdit(self.page_3)
        self.lineEdit_tel.setObjectName(u"lineEdit_tel")
        self.lineEdit_tel.setGeometry(QRect(1032, 120, 181, 20))
        self.dateEdit_naissance = QDateEdit(self.page_3)
        self.dateEdit_naissance.setObjectName(u"dateEdit_naissance")
        self.dateEdit_naissance.setGeometry(QRect(40, 200, 191, 22))
        self.dateEdit_naissance.setStyleSheet(u"")
        self.comboBox_region = QComboBox(self.page_3)
        self.comboBox_region.addItem("")
        self.comboBox_region.addItem("")
        self.comboBox_region.addItem("")
        self.comboBox_region.addItem("")
        self.comboBox_region.addItem("")
        self.comboBox_region.addItem("")
        self.comboBox_region.addItem("")
        self.comboBox_region.addItem("")
        self.comboBox_region.addItem("")
        self.comboBox_region.addItem("")
        self.comboBox_region.addItem("")
        self.comboBox_region.addItem("")
        self.comboBox_region.addItem("")
        self.comboBox_region.addItem("")
        self.comboBox_region.addItem("")
        self.comboBox_region.addItem("")
        self.comboBox_region.addItem("")
        self.comboBox_region.addItem("")
        self.comboBox_region.addItem("")
        self.comboBox_region.addItem("")
        self.comboBox_region.addItem("")
        self.comboBox_region.addItem("")
        self.comboBox_region.addItem("")
        self.comboBox_region.setObjectName(u"comboBox_region")
        self.comboBox_region.setGeometry(QRect(290, 200, 191, 22))
        self.comboBox_region.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lineEdit_ong = QLineEdit(self.page_3)
        self.lineEdit_ong.setObjectName(u"lineEdit_ong")
        self.lineEdit_ong.setGeometry(QRect(542, 200, 191, 20))
        self.lineEdit_adresse = QLineEdit(self.page_3)
        self.lineEdit_adresse.setObjectName(u"lineEdit_adresse")
        self.lineEdit_adresse.setGeometry(QRect(802, 200, 161, 20))
        self.lineEdit_email = QLineEdit(self.page_3)
        self.lineEdit_email.setObjectName(u"lineEdit_email")
        self.lineEdit_email.setGeometry(QRect(1032, 200, 181, 20))
        self.tableWidget_3 = QTableWidget(self.page_3)
        if (self.tableWidget_3.columnCount() < 11):
            self.tableWidget_3.setColumnCount(11)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(6, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(7, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(8, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(9, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(10, __qtablewidgetitem16)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setGeometry(QRect(70, 310, 1101, 321))
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.label_7 = QLabel(self.page_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(510, 40, 321, 31))
        font7 = QFont()
        font7.setPointSize(19)
        self.label_7.setFont(font7)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_18 = QLabel(self.page_4)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(40, 120, 91, 31))
        font8 = QFont()
        font8.setPointSize(13)
        font8.setUnderline(True)
        self.label_18.setFont(font8)
        self.label_18.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lineEdit_etudiant_doc = QLineEdit(self.page_4)
        self.lineEdit_etudiant_doc.setObjectName(u"lineEdit_etudiant_doc")
        self.lineEdit_etudiant_doc.setGeometry(QRect(40, 160, 221, 31))
        self.label_27 = QLabel(self.page_4)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(40, 210, 131, 21))
        self.label_27.setFont(font8)
        self.label_27.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lineEdit_doc = QLineEdit(self.page_4)
        self.lineEdit_doc.setObjectName(u"lineEdit_doc")
        self.lineEdit_doc.setGeometry(QRect(40, 250, 221, 31))
        self.label_28 = QLabel(self.page_4)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(540, 120, 131, 31))
        self.label_28.setFont(font8)
        self.label_28.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.plainTextEdit_prescription = QPlainTextEdit(self.page_4)
        self.plainTextEdit_prescription.setObjectName(u"plainTextEdit_prescription")
        self.plainTextEdit_prescription.setGeometry(QRect(540, 160, 321, 121))
        self.label_29 = QLabel(self.page_4)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(290, 120, 131, 31))
        self.label_29.setFont(font8)
        self.label_29.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lineEdit_prescripteur = QLineEdit(self.page_4)
        self.lineEdit_prescripteur.setObjectName(u"lineEdit_prescripteur")
        self.lineEdit_prescripteur.setGeometry(QRect(290, 160, 221, 31))
        self.label_30 = QLabel(self.page_4)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(290, 210, 91, 21))
        self.label_30.setFont(font8)
        self.label_30.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_duration = QSpinBox(self.page_4)
        self.spinBox_duration.setObjectName(u"spinBox_duration")
        self.spinBox_duration.setGeometry(QRect(290, 250, 221, 31))
        self.lineEdit = QLineEdit(self.page_4)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(40, 320, 221, 41))
        self.lineEdit.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pushButton_search = QPushButton(self.page_4)
        self.pushButton_search.setObjectName(u"pushButton_search")
        self.pushButton_search.setGeometry(QRect(300, 330, 21, 21))
        self.pushButton_search.setStyleSheet(u"border-image: url(:/icons/icons/search.svg);")
        self.label_31 = QLabel(self.page_4)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(290, 320, 41, 41))
        self.label_31.setMaximumSize(QSize(45, 16777215))
        self.label_31.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:20px")
        self.calendarWidget_doc = QCalendarWidget(self.page_4)
        self.calendarWidget_doc.setObjectName(u"calendarWidget_doc")
        self.calendarWidget_doc.setGeometry(QRect(910, 110, 312, 171))
        self.tableWidget_4 = QTableWidget(self.page_4)
        if (self.tableWidget_4.columnCount() < 8):
            self.tableWidget_4.setColumnCount(8)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(5, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(6, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(7, __qtablewidgetitem24)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        self.tableWidget_4.setGeometry(QRect(20, 390, 801, 231))
        self.label_32 = QLabel(self.page_4)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(910, 90, 71, 21))
        self.label_32.setFont(font8)
        self.label_32.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_2 = QPushButton(self.page_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(390, 332, 81, 21))
        self.pushButton_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 191, 255);\n"
"border-radius:10px;\n"
"")
        self.pushButton_4 = QPushButton(self.page_4)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(540, 330, 75, 23))
        self.pushButton_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 191, 255);\n"
"border-radius:10px;")
        self.pushButton_5 = QPushButton(self.page_4)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(670, 330, 75, 23))
        self.pushButton_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 191, 255);\n"
"border-radius:10px;")
        self.tableWidget_6 = QTableWidget(self.page_4)
        if (self.tableWidget_6.columnCount() < 5):
            self.tableWidget_6.setColumnCount(5)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(0, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(1, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(2, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(3, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(4, __qtablewidgetitem29)
        self.tableWidget_6.setObjectName(u"tableWidget_6")
        self.tableWidget_6.setGeometry(QRect(840, 390, 371, 231))
        self.comboBox_matin = QComboBox(self.page_4)
        self.comboBox_matin.addItem("")
        self.comboBox_matin.addItem("")
        self.comboBox_matin.setObjectName(u"comboBox_matin")
        self.comboBox_matin.setGeometry(QRect(920, 330, 69, 22))
        self.comboBox_midi = QComboBox(self.page_4)
        self.comboBox_midi.addItem("")
        self.comboBox_midi.addItem("")
        self.comboBox_midi.setObjectName(u"comboBox_midi")
        self.comboBox_midi.setGeometry(QRect(1020, 330, 69, 22))
        self.comboBox_soir = QComboBox(self.page_4)
        self.comboBox_soir.addItem("")
        self.comboBox_soir.addItem("")
        self.comboBox_soir.setObjectName(u"comboBox_soir")
        self.comboBox_soir.setGeometry(QRect(1110, 330, 69, 22))
        self.label_33 = QLabel(self.page_4)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(920, 300, 47, 21))
        font9 = QFont()
        font9.setPointSize(10)
        font9.setUnderline(True)
        self.label_33.setFont(font9)
        self.label_33.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_34 = QLabel(self.page_4)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(1020, 300, 47, 21))
        self.label_34.setFont(font9)
        self.label_34.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_35 = QLabel(self.page_4)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(1110, 300, 47, 21))
        font10 = QFont()
        font10.setUnderline(True)
        self.label_35.setFont(font10)
        self.label_35.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.stackedWidget.addWidget(self.page_4)
        self.label_7.raise_()
        self.label_18.raise_()
        self.lineEdit_etudiant_doc.raise_()
        self.label_27.raise_()
        self.lineEdit_doc.raise_()
        self.label_28.raise_()
        self.plainTextEdit_prescription.raise_()
        self.label_29.raise_()
        self.lineEdit_prescripteur.raise_()
        self.label_30.raise_()
        self.spinBox_duration.raise_()
        self.lineEdit.raise_()
        self.label_31.raise_()
        self.pushButton_search.raise_()
        self.calendarWidget_doc.raise_()
        self.tableWidget_4.raise_()
        self.label_32.raise_()
        self.pushButton_2.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.tableWidget_6.raise_()
        self.comboBox_matin.raise_()
        self.comboBox_midi.raise_()
        self.comboBox_soir.raise_()
        self.label_33.raise_()
        self.label_34.raise_()
        self.label_35.raise_()
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.label_21 = QLabel(self.page_5)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(520, 40, 261, 61))
        self.label_21.setFont(font6)
        self.label_21.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.tableWidget_5 = QTableWidget(self.page_5)
        if (self.tableWidget_5.columnCount() < 3):
            self.tableWidget_5.setColumnCount(3)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(2, __qtablewidgetitem32)
        self.tableWidget_5.setObjectName(u"tableWidget_5")
        self.tableWidget_5.setGeometry(QRect(690, 120, 501, 291))
        self.pushButton_ajouter_admin = QPushButton(self.page_5)
        self.pushButton_ajouter_admin.setObjectName(u"pushButton_ajouter_admin")
        self.pushButton_ajouter_admin.setGeometry(QRect(550, 120, 101, 51))
        self.pushButton_ajouter_admin.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);\n"
"border-radius:10px;")
        self.pushButton_supprimer_admin = QPushButton(self.page_5)
        self.pushButton_supprimer_admin.setObjectName(u"pushButton_supprimer_admin")
        self.pushButton_supprimer_admin.setGeometry(QRect(550, 220, 101, 51))
        self.pushButton_supprimer_admin.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);\n"
"border-radius:10px;")
        self.pushButton_modifier_admin = QPushButton(self.page_5)
        self.pushButton_modifier_admin.setObjectName(u"pushButton_modifier_admin")
        self.pushButton_modifier_admin.setGeometry(QRect(550, 320, 101, 51))
        self.pushButton_modifier_admin.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);\n"
"border-radius:10px;")
        self.label_23 = QLabel(self.page_5)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(170, 150, 211, 31))
        self.label_23.setFont(font8)
        self.label_23.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_24 = QLabel(self.page_5)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(170, 270, 161, 21))
        self.label_24.setFont(font8)
        self.label_24.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lineEdit_admin_name = QLineEdit(self.page_5)
        self.lineEdit_admin_name.setObjectName(u"lineEdit_admin_name")
        self.lineEdit_admin_name.setGeometry(QRect(170, 200, 191, 31))
        self.lineEdit_admin_password = QLineEdit(self.page_5)
        self.lineEdit_admin_password.setObjectName(u"lineEdit_admin_password")
        self.lineEdit_admin_password.setGeometry(QRect(170, 310, 191, 31))
        self.label_25 = QLabel(self.page_5)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(180, 390, 191, 51))
        self.label_25.setFont(font8)
        self.label_25.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.textBrowser = QTextBrowser(self.page_5)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(360, 440, 821, 192))
        self.textBrowser.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border:None")
        self.label_19 = QLabel(self.page_5)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(110, 380, 281, 291))
        self.label_19.setStyleSheet(u"border-image: url(:/images/images/2-removebg-preview.png);")
        self.pushButton_deconnect = QPushButton(self.page_5)
        self.pushButton_deconnect.setObjectName(u"pushButton_deconnect")
        self.pushButton_deconnect.setGeometry(QRect(1170, 20, 31, 31))
        self.pushButton_deconnect.setStyleSheet(u"border-image: url(:/icons/icons/power.svg);")
        self.stackedWidget.addWidget(self.page_5)
        self.frame_5.raise_()
        self.frame_4.raise_()

        self.verticalLayout.addWidget(self.Main)

        self.Footer = QFrame(self.Background)
        self.Footer.setObjectName(u"Footer")
        self.Footer.setMinimumSize(QSize(0, 25))
        self.Footer.setMaximumSize(QSize(16777215, 25))
        self.Footer.setStyleSheet(u"background-color: rgb(10, 10, 10);")
        self.Footer.setFrameShape(QFrame.StyledPanel)
        self.Footer.setFrameShadow(QFrame.Raised)
        self.label_20 = QLabel(self.Footer)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(540, -20, 381, 51))
        self.label_20.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.Footer)


        self.horizontalLayout.addWidget(self.Background)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        
        self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=0,yOffset=0,color=QtGui.QColor(234,221,186,100)))
        self.label_4.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=0,yOffset=0,color=QtGui.QColor(105,118,186,100)))
        self.pushButton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=3,yOffset=3,color=QtGui.QColor(105,118,132,100)))
                
        self.verticalLayout.addWidget(self.Footer)


        self.horizontalLayout.addWidget(self.Background)

        MainWindow.setCentralWidget(self.centralwidget)
        
        
        #Pour agrandir la fenetre
        self.pushButton_6.clicked.connect(self.enlargeWindow)
        
        #Pour reduire la fenetre
        self.pushButton_3.clicked.connect(self.reduceWindow)
        
        #Pour quiiter la fenetre
        self.pushButton.clicked.connect(self.quitWindow)
        
        #Pour demarrer le scanneur de QR code
        self.pushButton_demarrer.clicked.connect(self.readerQrCode)
        
        #Pour utiliser la fonction qui récupere la valeur du calendrier
        self.calendarWidget.selectionChanged.connect(self.handleDateSelection)
         
        
      
        
        # Ajout des fonctions au bouton
        self.pushButton_ajouter.clicked.connect(self.add_student)
        self.pushButton_modifier.clicked.connect(self.update_data)
        self.pushButton_supprimer.clicked.connect(self.delete_data)
        self.pushButton_reinitialiser.clicked.connect(self.reset_data)
        self.pushButton_ajouter_admin.clicked.connect(self.add_user)
        self.pushButton_modifier_admin.clicked.connect(self.update_data_user)
        self.pushButton_supprimer_admin.clicked.connect(self.delete_data_user)
        self.pushButton_deconnect.clicked.connect(self.deconnect)
        
         #evenement click dans le tableau
        self.tableWidget_3.cellClicked.connect(self.get_cursor)
        self.tableWidget_5.cellClicked.connect(self.get_cursor1)
        
        
        #Side
        self.Side_Menu_Num=0
        self.toolButton.clicked.connect(lambda:self.Side_Menu_Def_0())
        
        #PAGE1
        self.button_1.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.page_1))
        
        #PAGE2
        self.button_2.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.page_2))
        self.frame_5.mousePressEvent = self.Side_Menu_Def_1
        
        #PAGE2
        self.toolButton_4.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.page_3))
        
        
        #PAGE3
        self.toolButton_5.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.page_4))
        
        #PAGE4
        self.toolButton_6.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.page_5))
        
        
        # Créer une minuterie pour rafraîchir les données toutes les 30 secondes
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.fetchDataFromDatabase1)
        self.timer.timeout.connect(self.fetchDataFromDatabase)
        self.timer.timeout.connect(self.fetchDataFromDatabase2)
        self.timer.timeout.connect(self.showStudentData)
        self.timer.timeout.connect(self.fetchDataFromDatabase_medoc)
        self.timer.start(4000)  # Démarrer la minuterie avec une période de 30 000 millisecondes (30 secondes)
        
        
        #Pour le déplacement de la fenetrE
        # MainWindow.mouseMoveEvent = ui.moveWindow
        
        
        self.pushButton_2.clicked.connect(self.add_medoc)
        self.pushButton_5.clicked.connect(self.update_data_periode)
        self.pushButton_search.clicked.connect(self.fetchDataFromDatabase_search)
        self.tableWidget_4.cellClicked.connect(self.get_cursor_doc)
        self.tableWidget_6.cellClicked.connect(self.get_cursor_doc_periode)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
    
    def deconnect(self):
        deconnect = QMessageBox.question(self.root, "Modifier", "Êtes-vous sûr de vouloir deconnecté?", QMessageBox.Yes | QMessageBox.No,
                                              QMessageBox.No)
        if deconnect == QMessageBox.Yes:
                subprocess.Popen(["Python","ui_loginsignup.py"])
                self.close()
        else:
                pass
            
    
    def add_medoc(self):
            if self.lineEdit_etudiant_doc.text() == "" or self.lineEdit_doc.text() == "" or self.plainTextEdit_prescription.toPlainText() == "":
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setWindowTitle("Erreur")
                msg_box.setText("Tous les champs sont obligatoires")
                msg_box.exec_()
            else:
                        try:
                                conn = sqlite3.connect('db.sqlite')
                                cursor = conn.cursor()

                                # Convert duree en integer
                                duree = int(self.spinBox_duration.value())


                                start_date = self.calendarWidget_doc.selectedDate().toPython()
                                print(start_date)

                                # Calculer la date du fin du medicaments
                                end_date = start_date + timedelta(days=duree)

                                end_date_str = end_date.strftime('%d/%m/%Y')
                                print(end_date)
                                start_date=start_date.strftime('%d/%m/%Y')
                                
                                cursor.execute('''INSERT INTO medicaments(ETUDIANT, DEBUT, FIN, MEDICAMENTS, DUREE, PRESCRIPTEURS, PRESCRIPTIONS)
                                VALUES (?, ?, ?, ?, ?, ?, ?)''',
                                (self.lineEdit_etudiant_doc.text(), start_date, end_date_str, self.lineEdit_doc.text(),
                                self.spinBox_duration.value(), self.lineEdit_prescripteur.text(), self.plainTextEdit_prescription.toPlainText()))
                                conn.commit()
                                # Récupérer l'ID de la dernière ligne insérée dans la table medicaments
                                last_row_id = cursor.lastrowid

                                # Convertir le texte de la date initiale en un objet QDateTime
                                start_date = QDateTime.fromString(start_date, "dd/MM/yyyy")

                                
                                # Boucle pour insérer dans la table periode en utilisant l'ID récupéré
                                for i in range(0, int(self.spinBox_duration.value())):
                                        # Incrémenter la date d'un jour en utilisant addDays(1)
                                        current_date = start_date.addDays(i)
                                        # Convertir current_date en une représentation de chaîne de caractères
                                        current_date_str = current_date.toString("dd/MM/yyyy")
                                        # Insérer dans la table periode en utilisant l'ID récupéré
                                        cursor.execute('''INSERT INTO periode (date, matin, midi, soir, id_doc) VALUES (?, ?, ?, ?, ?)''',
                                                        (current_date_str, "Non", "Non", "Non", last_row_id))
                

                                       
                                conn.commit()
                                cursor.close()
                                conn.close()
                                self.fetchDataFromDatabase_medoc()
                                msg_box = QMessageBox()
                                msg_box.setIcon(QMessageBox.Information)
                                msg_box.setWindowTitle("Succès")
                                msg_box.setText("Suivi ajouté")
                                msg_box.exec_()
                                
                        except Exception as es:
                                msg_box = QMessageBox()
                                msg_box.setIcon(QMessageBox.Critical)
                                msg_box.setWindowTitle("Erreur")
                                msg_box.setText("Erreur lors de l'ajout du suivie")
                                msg_box.exec_()
                                
                                
    def get_cursor_doc(self, row, column):
        data = []
        for col in range(self.tableWidget_4.columnCount()):  # Commence à partir de la deuxième colonne (index 1)
                item = self.tableWidget_4.item(row, col)
                data.append(item.text() if item else "")
        for item in data:
                print(data)
        
        self.selected_id_doc = data[0]
        self.start_doc=data[2]
        self.end_doc=data[3]
        self.fetchDataFromDatabase_medoc_periode(self.selected_id_doc,self.start_doc,self.end_doc)


    def get_cursor_doc_periode(self, row, column):
                data_periode = []
                for col in range(self.tableWidget_6.columnCount()):  # Commence à partir de la deuxième colonne (index 1)
                        item = self.tableWidget_6.item(row, col)
                        data_periode.append(item.text() if item else "")
                for item in data_periode:
                        print(data_periode) 
                self.id_periode=data_periode[0]
                self.comboBox_matin.setCurrentText(data_periode[2])
                self.comboBox_midi.setCurrentText(data_periode[3])
                self.comboBox_soir.setCurrentText(data_periode[4])
                self.fetchDataFromDatabase_medoc_periode(self.selected_id_doc,self.start_doc,self.end_doc)


    def update_data_periode(self):
                try:
                        update = QMessageBox.question(self.root, "Modifier", "Êtes-vous sûr de vouloir modifier les données?", QMessageBox.Yes | QMessageBox.No,
                                              QMessageBox.No)
                        if update == QMessageBox.Yes:
                                conn = sqlite3.connect('db.sqlite')
                                cursor = conn.cursor()
                                print(self.comboBox_matin.currentText(),self.comboBox_midi.currentText(),self.comboBox_soir.currentText(),self.id_periode)
                                query = "UPDATE periode SET matin=?, midi=?,soir=? WHERE id_date=?"
                                values = (self.comboBox_matin.currentText(),self.comboBox_midi.currentText(),self.comboBox_soir.currentText(),self.id_periode)
                                cursor.execute(query, values)
                                conn.commit()
                                conn.close()
                                self.fetchDataFromDatabase_medoc_periode(self.selected_id_doc,self.start_doc,self.end_doc)
                                QMessageBox.information(self.root, "Succès", "Valeur modifié")
                        else:
                                if not update:
                                        return
                except Exception as es:
                        QMessageBox.critical(self.root, "Erreur", "Erreur lors de la modification de l'étudiant")

    #Recherche
    def fetchDataFromDatabase_search(self):
        search=self.lineEdit.text()
        conn = sqlite3.connect('db.sqlite')
        cursor = conn.cursor()
        query = f"SELECT * FROM medicaments WHERE ETUDIANT=?"
        cursor.execute(query,(search,))
        self.data = cursor.fetchall()
        cursor.close()
        conn.close()
        # Mettre à jour le tableau avec les nouvelles données
        self.populateTable_medoc(self.data)

        
    #Afficher les données              
    def fetchDataFromDatabase_medoc(self):
        conn = sqlite3.connect('db.sqlite')
        cursor = conn.cursor()
        query = f"SELECT * FROM medicaments"
        cursor.execute(query)
        self.data = cursor.fetchall()
        cursor.close()
        conn.close()
        # Mettre à jour le tableau avec les nouvelles données
        self.populateTable_medoc(self.data)
        
    def populateTable_medoc(self, data):
        self.tableWidget_4.setRowCount(len(data))
        for row, row_data in enumerate(data):
            for col, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.tableWidget_4.setItem(row, col, item)
                
    def fetchDataFromDatabase_medoc_periode(self, id, start, end):
        conn = sqlite3.connect('db.sqlite')
        cursor = conn.cursor()

        # Utiliser des paramètres de requête pour éviter les problèmes de syntaxe et d'injection SQL
        query = "SELECT id_date,Date, matin, midi, soir FROM periode WHERE date BETWEEN ? AND ? AND id_doc = ?"
        cursor.execute(query, (start, end, id))

        self.data = cursor.fetchall()
        cursor.close()
        conn.close()
        # Mettre à jour le tableau avec les nouvelles données
        self.populateTable_medoc_periode(self.data)
        
    def populateTable_medoc_periode(self, data):
        self.tableWidget_6.setRowCount(len(data))
        for row, row_data in enumerate(data):
            for col, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.tableWidget_6.setItem(row, col, item)
    def readerQrCode(self):
            subprocess.Popen(["python","readerQRcode.py"], bufsize=0)
            
        
    def Side_Menu_Def_0(self):
        if self.Side_Menu_Num == 0:
            self.animation1=QtCore.QPropertyAnimation(self.frame_4,b"maximumWidth")
            self.animation1.setDuration(500)
            self.animation1.setStartValue(40)
            self.animation1.setEndValue(110)
            self.animation1.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation1.start()

            self.animation2=QtCore.QPropertyAnimation(self.frame_4,b"minimumWidth")
            self.animation2.setDuration(500)
            self.animation2.setStartValue(40)
            self.animation2.setEndValue(110)
            self.animation2.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation2.start()
            self.Side_Menu_Num=1
        else:
            self.animation1=QtCore.QPropertyAnimation(self.frame_4,b"maximumWidth")
            self.animation1.setDuration(500)
            self.animation1.setStartValue(110)
            self.animation1.setEndValue(40)
            self.animation1.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation1.start()
            
            self.animation2=QtCore.QPropertyAnimation(self.frame_4,b"minimumWidth")
            self.animation2.setDuration(500)
            self.animation2.setStartValue(110)
            self.animation2.setEndValue(40)
            self.animation2.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation2.start()
            self.Side_Menu_Num=0
            
    def Side_Menu_Def_1(self,Event):
            if Event.button() == QtCore.Qt.LeftButton:
                if self.Side_Menu_Num==1:
                    self.animation1=QtCore.QPropertyAnimation(self.frame_4,b"maximumWidth")
                    self.animation1.setDuration(500)
                    self.animation1.setStartValue(110)
                    self.animation1.setEndValue(40)
                    self.animation1.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
                    self.animation1.start()
                    
                    self.animation2=QtCore.QPropertyAnimation(self.frame_4,b"minimumWidth")
                    self.animation2.setDuration(500)
                    self.animation2.setStartValue(110)
                    self.animation2.setEndValue(40)
                    self.animation2.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
                    self.animation2.start()
                    self.Side_Menu_Num=0
                else:
                    pass

        
    def add_user(self):
            if self.lineEdit_admin_name.text() == "" or self.lineEdit_admin_password.text() == "":
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setWindowTitle("Erreur")
                msg_box.setText("Tous les champs sont obligatoires")
                msg_box.exec_()
            else:
                try:
                        conn = sqlite3.connect('db.sqlite')
                        cursor = conn.cursor()
                        cursor.execute('''INSERT INTO users(username,password) VALUES (?, ?)''',(self.lineEdit_admin_name.text(), self.lineEdit_admin_password.text()))
                        conn.commit()
                        self.fetchDataFromDatabase()
                        cursor.close()
                        conn.close()
                        msg_box = QMessageBox()
                        msg_box.setIcon(QMessageBox.Information)
                        msg_box.setWindowTitle("Succès")
                        msg_box.setText("Utilisateur ajouté")
                        msg_box.exec_()
                                
                                
                except Exception as es:
                        msg_box = QMessageBox()
                        msg_box.setIcon(QMessageBox.Critical)
                        msg_box.setWindowTitle("Erreur")
                        msg_box.setText("Erreur lors de l'ajout de l'étudiant")
                        msg_box.exec_()
                                
                                
    def add_student(self):
            if self.lineEdit_nom.text() == "" or self.lineEdit_prenom.text() == "" or self.lineEdit_email.text() == "":
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setWidowTitle("Erreur")
                msg_box.setText("Tous les champs sont obligatoires")
                msg_box.exec_()
            else:
                        try:
                                conn = sqlite3.connect('db.sqlite')
                                cursor = conn.cursor()
                                cursor.execute('''INSERT INTO student(NOM, PRENOM, SEXE, AGE, TEL, NAISSANCE, REGION, ONG, ADRESSE, EMAIL)
                                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                                                (self.lineEdit_nom.text(), self.lineEdit_prenom.text(), self.lineEdit_sexe.text(), self.lineEdit_age.text(),
                                                self.lineEdit_tel.text(), self.dateEdit_naissance.text(), self.comboBox_region.currentText(), self.lineEdit_ong.text(),
                                                self.lineEdit_adresse.text(), self.lineEdit_email.text()))
                                conn.commit()
                                self.fetchDataFromDatabase()
                                cursor.close()
                                conn.close()
                                msg_box = QMessageBox()
                                msg_box.setIcon(QMessageBox.Information)
                                msg_box.setWindowTitle("Succès")
                                msg_box.setText("Étudiant ajouté")
                                msg_box.exec_()
                                
                                
                        except Exception as es:
                                msg_box = QMessageBox()
                                msg_box.setIcon(QMessageBox.Critical)
                                msg_box.setWindowTitle("Erreur")
                                msg_box.setText("Erreur lors de l'ajout de l'étudiant")
                                msg_box.exec_()
                                
                                     
    #Afficher les données              
    def fetchDataFromDatabase(self):
        conn = sqlite3.connect('db.sqlite')
        cursor = conn.cursor()
        query = f"SELECT * FROM student"
        cursor.execute(query)
        self.data = cursor.fetchall()
        cursor.close()
        conn.close()
        # Mettre à jour le tableau avec les nouvelles données
        self.populateTable(self.data)
        
    #Afficher les données              
    def fetchDataFromDatabase2(self):
        conn = sqlite3.connect('db.sqlite')
        cursor = conn.cursor()
        query = f"SELECT * FROM users"
        cursor.execute(query)
        self.data = cursor.fetchall()
        cursor.close()
        conn.close()
        # Mettre à jour le tableau avec les nouvelles données
        self.populateTable2(self.data)
        
    def populateTable2(self, data):
        self.tableWidget_5.setRowCount(len(data))
        for row, row_data in enumerate(data):
            for col, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.tableWidget_5.setItem(row, col, item)
        
        
    def populateTable(self, data):
        self.tableWidget_3.setRowCount(len(data))
        for row, row_data in enumerate(data):
            for col, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.tableWidget_3.setItem(row, col, item)
                
    #Avoir le curseur
    @Slot(int, int)
    def get_cursor(self, row, column):
        data = []
        for col in range(self.tableWidget_3.columnCount()):  # Commence à partir de la deuxième colonne (index 1)
                item = self.tableWidget_3.item(row, col)
                data.append(item.text() if item else "")
        for item in data:
                print(data)
                 
        self.selected_id = data[0]
        self.lineEdit_nom.setText(data[1])
        self.lineEdit_prenom.setText(data[2])
        self.lineEdit_sexe.setText(data[3])
        self.lineEdit_age.setText(data[4])
        self.lineEdit_tel.setText(data[5])
        self.dateEdit_naissance.setDate(QDate.fromString(data[6], "yyyy-MM-dd"))
        self.comboBox_region.setCurrentText(data[7])
        self.lineEdit_ong.setText(data[8])
        self.lineEdit_adresse.setText(data[9])
        self.lineEdit_email.setText(data[10])
        
    @Slot(int, int)
    def get_cursor1(self, row, column):
        data = []
        for col in range(self.tableWidget_5.columnCount()):  # Commence à partir de la deuxième colonne (index 1)
                item = self.tableWidget_5.item(row, col)
                data.append(item.text() if item else "")
        for item in data:
                print(data)
                
        self.selected_id_users = data[0]
        self.lineEdit_admin_name.setText(data[1])
        self.lineEdit_admin_password.setText(data[2])
        
        
        
    def update_data_user(self):
        if self.lineEdit_admin_name.text() == "" or self.lineEdit_admin_password.text() == "":
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setWindowTitle("Erreur")
                msg_box.setText("Tous les champs sont obligatoires")
                msg_box.exec_()
        else:
                try:
                        update = QMessageBox.question(self.root, "Modifier", "Êtes-vous sûr de vouloir modifier les données?", QMessageBox.Yes | QMessageBox.No,
                                              QMessageBox.No)
                        if update == QMessageBox.Yes:
                                conn = sqlite3.connect('db.sqlite')
                                cursor = conn.cursor()
                                query = "UPDATE users SET username=?, password=? WHERE id_user=?"
                                values = (self.lineEdit_admin_name.text(), self.lineEdit_admin_password.text(),self.selected_id_users)
                                cursor.execute(query, values)
                                conn.commit()
                                conn.close()
                                self.fetchDataFromDatabase2()
                                QMessageBox.information(self.root, "Succès", "Utilisateur modifié")
                        else:
                                if not update:
                                        return
                except Exception as es:
                        QMessageBox.critical(self.root, "Erreur", "Erreur lors de la modification de l'utilisateur")
        
    #Fonction pour modifier 
    def update_data(self):
        if self.lineEdit_nom.text() == "" or self.lineEdit_prenom.text() == "" or self.lineEdit_email.text() == "":
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setWindowTitle("Erreur")
                msg_box.setText("Tous les champs sont obligatoires")
                msg_box.exec_()
        else:
                try:
                        update = QMessageBox.question(self.root, "Modifier", "Êtes-vous sûr de vouloir modifier les données?", QMessageBox.Yes | QMessageBox.No,
                                              QMessageBox.No)
                        if update == QMessageBox.Yes:
                                conn = sqlite3.connect('db.sqlite')
                                cursor = conn.cursor()
                                query = "UPDATE student SET NOM=?, PRENOM=?, SEXE=?, AGE=?, TEL=?, NAISSANCE=?, REGION=?, ONG=?, ADRESSE=?, EMAIL=? WHERE id=?"
                                values = (self.lineEdit_nom.text(), self.lineEdit_prenom.text(), self.lineEdit_sexe.text(), self.lineEdit_age.text(), self.lineEdit_tel.text(), self.dateEdit_naissance.text(), self.comboBox_region.currentText(), self.lineEdit_ong.text(), self.lineEdit_adresse.text(), self.lineEdit_email.text(),self.selected_id)
                                cursor.execute(query, values)
                                conn.commit()
                                conn.close()
                                self.fetchDataFromDatabase()
                                QMessageBox.information(self.root, "Succès", "Étudiant modifié")
                        else:
                                if not update:
                                        return
                except Exception as es:
                        QMessageBox.critical(self.root, "Erreur", "Erreur lors de la modification de l'étudiant")
                        

    #Fonction pour supprimer les données
    def delete_data(self):
        if self.lineEdit_nom.text() == "" or self.lineEdit_prenom.text() == "" or self.lineEdit_email.text() == "":
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setWindowTitle("Erreur")
                msg_box.setText("Tous les champs sont obligatoires")
                msg_box.exec_()
        else:
                try:
                        Delete = QMessageBox.question(self.root, "Supprimer", "Etes vous sur de vouloir supprimer l'étudiant?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                        if Delete == QMessageBox.Yes:
                                conn = sqlite3.connect('db.sqlite')
                                cursor = conn.cursor()
                                sql = "DELETE FROM student WHERE id = ?"
                                value = (self.selected_id ,)
                                cursor.execute(sql, value)
                                if cursor.rowcount > 0:
                                        conn.commit()
                                        self.fetchDataFromDatabase()
                                        QMessageBox.information(self.root, "Supprimer", "L'étudiant est bien supprimé")
                                else:
                                        QMessageBox.critical(self.root, "Erreur", "Aucune ligne n'a été supprimée")
                                conn.close()
                        else:
                             if not Delete:
                                return

                except Exception as es:
                      Qmessagebox.Critical(self.root,"Erreur", f"Erreur lors de la suppression de l'étudiant : {str(es)}")
                      
    def delete_data_user(self):
        if self.lineEdit_admin_name.text() == "" or self.lineEdit_admin_password.text() == "":
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setWindowTitle("Erreur")
                msg_box.setText("Tous les champs sont obligatoires")
                msg_box.exec_()
        else:
                try:
                        Delete = QMessageBox.question(self.root, "Supprimer", "Etes vous sur de vouloir supprimer l'utilisateur?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                        if Delete == QMessageBox.Yes:
                                conn = sqlite3.connect('db.sqlite')
                                cursor = conn.cursor()
                                sql = "DELETE FROM users WHERE id_user = ?"
                                value = (self.selected_id_users,)
                                cursor.execute(sql, value)
                                if cursor.rowcount >= 0:
                                        conn.commit()
                                        self.fetchDataFromDatabase2()
                                        QMessageBox.information(self.root, "Supprimer", "L'Utilisateur est bien supprimé")
                                else:
                                        QMessageBox.critical(self.root, "Erreur", "Aucune ligne n'a été supprimée")
                                conn.close()
                        else:
                             if not Delete:
                                return

                except Exception as es:
                      Qmessagebox.Critical(self.root,"Erreur", f"Erreur lors de la suppression de l'étudiant : {str(es)}")

    #fonction de réinitialisation de donner
    def reset_data(self):
            self.selected_id = ""
            self.lineEdit_nom.setText("")
            self.lineEdit_prenom.setText("")
            self.lineEdit_sexe.setText("")
            self.lineEdit_age.setText("")
            self.lineEdit_tel.setText("")
            self.dateEdit_naissance.setDate(QDate.fromString("01/01/2000"))
            self.comboBox_region.setCurrentText("Diana")
            self.lineEdit_ong.setText("")
            self.lineEdit_adresse.setText("")
            self.lineEdit_email.setText("")
            
    def quitWindow(self):
            self.close()
            
    def reduceWindow(self):
        self.showMinimized()
        
    def enlargeWindow(self):
        self.showMaximized()
                
    #fonction Pour rafracihir le tableau et récuperer les données pour le tableau
    def fetchDataFromDatabase1(self):
        selected_date = self.calendarWidget.selectedDate()
        conn = sqlite3.connect('db.sqlite')
        cursor = conn.cursor()
        query = "SELECT etudiant, Date, Heure, Moment FROM present WHERE Date = ? and Moment = ?"
        cursor.execute(query, (selected_date.toString(Qt.ISODate), self.comboBox.currentText(),))
        self.data = cursor.fetchall()
        cursor.close()
        conn.close()
        # Mettre à jour le tableau avec les nouvelles données
        self.populateTable1(self.data)



    def handleDateSelection(self):
        self.fetchDataFromDatabase1()


    #Fonction pour remplir le tableau
    def populateTable1(self, data):
        self.tableWidget.setRowCount(len(data))
        for row, row_data in enumerate(data):
            for col, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.tableWidget.setItem(row, col, item)
                
    #Fonction pour récuperer seulement les étudiants dans le tableau présent
    def getStudentData(self):
            student_data = set()
            for row in range(self.tableWidget.rowCount()):
                item = self.tableWidget.item(row, 0)  # Colonne 0 contient les données des étudiants
                if item is not None:
                    student_data.add(item.text())
            return student_data
    
    
    #Afficher les absents dans le tableau_widget_missing
    def showStudentData(self):
        student_data = self.getStudentData()
        missing_students = set(data_name) - student_data

        self.tableWidget_2.setRowCount(len(missing_students))
        
        # Variables pour suivre la ligne avec le numéro maximum
        max_row = 0
        max_row_number = 0
        
        for row, student in enumerate(missing_students):
            item = QTableWidgetItem(student)
            self.tableWidget_2.setItem(row, 0, item)
            
            # Mettre à jour le numéro de ligne maximum
            if row > max_row:
                max_row = row
                max_row_number = row + 1
        
        # Afficher le numéro de ligne maximum dans la deuxième colonne
        item = QTableWidgetItem(str(max_row_number))
        self.tableWidget_2.setItem(0, 1, item)
    
    
    #fonction pour le déplacement de la fenetre
#     def mousePressEvent(self,event):
#                 print("mousePressEvent triggered")

#                 #Prendre la postion actuelle de la souris
#                 self.clickPosition = event.globalPos()

#     def mouseMoveEvent(self, event):
#             if event.buttons() == QtCore.Qt.LeftButton and self.clickPosition is not None:
#                 MainWindow.move(MainWindow.pos() + event.globalPos() - self.clickPosition)
#                 self.clickPosition = event.globalPos()
#                 event.accept()
#     def moveWindow(self, event):
#                 if MainWindow.isMaximized() == False:
#                         if event.buttons() == Qt.LeftButton:
#                                 MainWindow.move(MainWindow.pos() + event.globalPos() - self.clickPosition)
#                                 self.clickPosition = event.globalPos()
#                                 event.accept()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_26.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"GadGest", None))
        self.pushButton.setText("")
        self.pushButton_6.setText("")
        self.pushButton_3.setText("")
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"    MENU", None))
        self.button_1.setText(QCoreApplication.translate("MainWindow", u"    GPRESENCE", None))
        self.button_2.setText(QCoreApplication.translate("MainWindow", u"    PRESENCE", None))
        self.toolButton_4.setText(QCoreApplication.translate("MainWindow", u"    ETUDIANT", None))
        self.toolButton_5.setText(QCoreApplication.translate("MainWindow", u"    MEDICALE", None))
        self.toolButton_6.setText(QCoreApplication.translate("MainWindow", u"   ADMIN", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nom d'etudiant", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nouvelle colonne", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Moment", None));
        ___qtablewidgetitem4 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Nom d'etudiant", None));
        ___qtablewidgetitem5 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Total absent", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Present:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Absent:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Gestion de Pr\u00e9sence", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Matin", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Apr\u00e8s-Midi", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"PRESENCE", None))
        self.pushButton_demarrer.setText(QCoreApplication.translate("MainWindow", u"D\u00e9marrer", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Pour quitter le scanneur veuillez appuiez sur \"q\"", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"GESTION DES ETUDIANTS", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"NOM:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"PRENOM", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"DATE DE NAISSANCE:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"TEL:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"AGE:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"SEXE:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"REGION:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"ONG:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"ADRESSE:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"EMAIL:", None))
        self.pushButton_ajouter.setText(QCoreApplication.translate("MainWindow", u"AJOUTER", None))
        self.pushButton_modifier.setText(QCoreApplication.translate("MainWindow", u"MODIFIER", None))
        self.pushButton_supprimer.setText(QCoreApplication.translate("MainWindow", u"SUPPRIMER", None))
        self.pushButton_reinitialiser.setText(QCoreApplication.translate("MainWindow", u"REINITIALISER", None))
        self.comboBox_region.setItemText(0, QCoreApplication.translate("MainWindow", u"Diana", None))
        self.comboBox_region.setItemText(1, QCoreApplication.translate("MainWindow", u"Sava", None))
        self.comboBox_region.setItemText(2, QCoreApplication.translate("MainWindow", u"Itasy", None))
        self.comboBox_region.setItemText(3, QCoreApplication.translate("MainWindow", u"Analamanga", None))
        self.comboBox_region.setItemText(4, QCoreApplication.translate("MainWindow", u"Vakinakaratra", None))
        self.comboBox_region.setItemText(5, QCoreApplication.translate("MainWindow", u"Bongolava", None))
        self.comboBox_region.setItemText(6, QCoreApplication.translate("MainWindow", u"Sofia", None))
        self.comboBox_region.setItemText(7, QCoreApplication.translate("MainWindow", u"Boeny", None))
        self.comboBox_region.setItemText(8, QCoreApplication.translate("MainWindow", u"Betsiboka", None))
        self.comboBox_region.setItemText(9, QCoreApplication.translate("MainWindow", u"Melaky", None))
        self.comboBox_region.setItemText(10, QCoreApplication.translate("MainWindow", u"Alaotra Mangoro", None))
        self.comboBox_region.setItemText(11, QCoreApplication.translate("MainWindow", u"Antsinanana", None))
        self.comboBox_region.setItemText(12, QCoreApplication.translate("MainWindow", u"Analanjorofo", None))
        self.comboBox_region.setItemText(13, QCoreApplication.translate("MainWindow", u"Amoron'i Mania", None))
        self.comboBox_region.setItemText(14, QCoreApplication.translate("MainWindow", u"Haute Matsiatra", None))
        self.comboBox_region.setItemText(15, QCoreApplication.translate("MainWindow", u"Vatovavy", None))
        self.comboBox_region.setItemText(16, QCoreApplication.translate("MainWindow", u"Fitovinany", None))
        self.comboBox_region.setItemText(17, QCoreApplication.translate("MainWindow", u"Atsimo Atsinanana", None))
        self.comboBox_region.setItemText(18, QCoreApplication.translate("MainWindow", u"Ihorombe", None))
        self.comboBox_region.setItemText(19, QCoreApplication.translate("MainWindow", u"Menabe", None))
        self.comboBox_region.setItemText(20, QCoreApplication.translate("MainWindow", u"Atsimo Andrefana", None))
        self.comboBox_region.setItemText(21, QCoreApplication.translate("MainWindow", u"Androy", None))
        self.comboBox_region.setItemText(22, QCoreApplication.translate("MainWindow", u"Anosy", None))

        ___qtablewidgetitem6 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem7 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"NOM", None));
        ___qtablewidgetitem8 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"PRENOM", None));
        ___qtablewidgetitem9 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"SEXE", None));
        ___qtablewidgetitem10 = self.tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"AGE", None));
        ___qtablewidgetitem11 = self.tableWidget_3.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"TEL", None));
        ___qtablewidgetitem12 = self.tableWidget_3.horizontalHeaderItem(6)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"NAISSANCE", None));
        ___qtablewidgetitem13 = self.tableWidget_3.horizontalHeaderItem(7)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"REGION", None));
        ___qtablewidgetitem14 = self.tableWidget_3.horizontalHeaderItem(8)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"ONG", None));
        ___qtablewidgetitem15 = self.tableWidget_3.horizontalHeaderItem(9)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"ADRESSE", None));
        ___qtablewidgetitem16 = self.tableWidget_3.horizontalHeaderItem(10)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"EMAIL", None));
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"FICHE MEDICALE", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"ETUDIANT:", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"MEDICAMENTS:", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"PRESCRIPTION:", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"PRESCRIPTEUR:", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"DUREE:", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Rechercher", None))
        self.pushButton_search.setText("")
        self.label_31.setText("")
        ___qtablewidgetitem17 = self.tableWidget_4.horizontalHeaderItem(0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"id_doc", None));
        ___qtablewidgetitem18 = self.tableWidget_4.horizontalHeaderItem(1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"ETUDIANT", None));
        ___qtablewidgetitem19 = self.tableWidget_4.horizontalHeaderItem(2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"DEBUT", None));
        ___qtablewidgetitem20 = self.tableWidget_4.horizontalHeaderItem(3)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"FIN", None));
        ___qtablewidgetitem21 = self.tableWidget_4.horizontalHeaderItem(4)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"MEDICAMENTS", None));
        ___qtablewidgetitem22 = self.tableWidget_4.horizontalHeaderItem(5)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"DUREE(jour)", None));
        ___qtablewidgetitem23 = self.tableWidget_4.horizontalHeaderItem(6)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"PRESCRIPTEURS", None));
        ___qtablewidgetitem24 = self.tableWidget_4.horizontalHeaderItem(7)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"PRESCRIPTION", None));
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"DEBUT:", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"AJOUTER", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"SUPPRIMER", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"VALIDER", None))
        ___qtablewidgetitem25 = self.tableWidget_6.horizontalHeaderItem(0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"periode_id", None));
        ___qtablewidgetitem26 = self.tableWidget_6.horizontalHeaderItem(1)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"DATE", None));
        ___qtablewidgetitem27 = self.tableWidget_6.horizontalHeaderItem(2)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"MATIN", None));
        ___qtablewidgetitem28 = self.tableWidget_6.horizontalHeaderItem(3)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"MIDI", None));
        ___qtablewidgetitem29 = self.tableWidget_6.horizontalHeaderItem(4)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"SOIR", None));
        self.comboBox_matin.setItemText(0, QCoreApplication.translate("MainWindow", u"Non", None))
        self.comboBox_matin.setItemText(1, QCoreApplication.translate("MainWindow", u"Oui", None))

        self.comboBox_midi.setItemText(0, QCoreApplication.translate("MainWindow", u"Non", None))
        self.comboBox_midi.setItemText(1, QCoreApplication.translate("MainWindow", u"Oui", None))

        self.comboBox_soir.setItemText(0, QCoreApplication.translate("MainWindow", u"Non", None))
        self.comboBox_soir.setItemText(1, QCoreApplication.translate("MainWindow", u"Oui", None))

        self.label_33.setText(QCoreApplication.translate("MainWindow", u"MATIN:", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"MIDI:", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"SOIR:", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"ESPACE ADMINISTRATEUR", None))
        ___qtablewidgetitem30 = self.tableWidget_5.horizontalHeaderItem(0)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"id_user", None));
        ___qtablewidgetitem31 = self.tableWidget_5.horizontalHeaderItem(1)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"UTILISATEUR", None));
        ___qtablewidgetitem32 = self.tableWidget_5.horizontalHeaderItem(2)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"MOT DE PASS", None));
        self.pushButton_ajouter_admin.setText(QCoreApplication.translate("MainWindow", u"AJOUTER", None))
        self.pushButton_supprimer_admin.setText(QCoreApplication.translate("MainWindow", u"SUPPRIMER", None))
        self.pushButton_modifier_admin.setText(QCoreApplication.translate("MainWindow", u"MODIFIER", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"NOM D'UTILISATEUR:", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"MOT DE PASS:", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"A PROPOS de GadGest:", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Version:1.0.0<br />D\u00e9veloppeur:Tsiory Vahya RABEARIVONY</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Contact:+261346739592</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Description:<br />GadGest<span style=\" font-size:8pt;\"> "
                        "est un logiciel de bureau polyvalent con\u00e7u pour faciliter la gestion des t\u00e2ches quotidiennes. Il offre une gamme de fonctionnalit\u00e9s puissantes, telles que la gestion de pr\u00e9sence, des etudiants , des medicaments. GadGest est l\u00e0 pour vous aider \u00e0 rester organis\u00e9 et productif.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Licence:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">GadGest est distribu\u00e9 sous licence propri\u00e9taire. L'utilisation de la version de base est gratuite.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px"
                        "; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Copyright \u00a9 2023  Tsiory Vahya RABEARIVONY. Tous droits r\u00e9serv\u00e9s.</span></p></body></html>", None))
        self.label_19.setText("")
        self.pushButton_deconnect.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\n"
"Copyright \u00a9 2023  Tsiory Vahya RABEARIVONY. Tous droits r\u00e9serv\u00e9s.", None))
    # retranslateUi

