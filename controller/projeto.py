from controller.card_projeto import CardProject
from qt_core import *
from model.pj_dao import *
class ProjetosPage(QWidget):
    def __init__(self, mainWindow):
        super().__init__()
        uic.loadUi('view/projeto.ui', self)

        self.mainWindow = mainWindow
        self.novo_projeto_btn.clicked.connect(self.novo_projeto)

        self.load()

    def load(self):
        l = selectAll()
        for p in l:
            self.painel_colab.addWidget(CardProject(p, self.mainWindow))
    def novo_projeto(self):
        self.mainWindow.setCurrentIndex(2)