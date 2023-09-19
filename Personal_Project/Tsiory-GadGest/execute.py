from GadGest import * 
# from ui_main1 import Ui_MainWindow
from PySide2.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        # Instanciation de la classe Ui_MainWindow
        # self.ui = Ui_MainWindow()
        
        # # Initialisation de l'interface utilisateur
        # self.ui.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
