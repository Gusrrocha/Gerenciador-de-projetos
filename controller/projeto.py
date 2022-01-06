from qt_core import *

class ProjetosPage(QWidget):
    def __init__(self, mainWindow):
        super().__init__()
        uic.loadUi('view/projeto.ui', self)

        self.mainWindow = mainWindow
        self.novo_projeto_btn.clicked.connect(self.novo_projeto)

    
    def novo_projeto(self):
        self.mainWindow.setCurrentIndex(2)