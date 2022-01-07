from controller.projeto import AddProject
from qt_core import *
from controller.colab_page import ColabPage
import model.pj_dao as projeto_dao
from controller.card_projeto import CardProject
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('view/main_window.ui', self)

        self.colab_btn.clicked.connect(self.show_colab)
        self.projeto_btn.clicked.connect(self.show_project)
        self.novo_pj.clicked.connect(self.novo_projeto)
        self.load()

    def load(self):
        l = projeto_dao.selectAll()
        for p in l:
            self.painel_pj.addWidget(CardProject(p, self))
    def show_colab(self):
        self.tabela.insertWidget(1, ColabPage())
        self.tabela.setCurrentIndex(1)

    def show_project(self):
        self.tabela.setCurrentIndex(0)

    def novo_projeto(self, projeto=None):
        self.tabela.insertWidget(2, AddProject(self, projeto))
        self.tabela.setCurrentIndex(2)