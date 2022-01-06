from controller.projeto import ProjetosPage
from qt_core import *
from controller.colab_page import ColabPage
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('view/main_window.ui', self)

        self.show_project()
        self.colab_btn.clicked.connect(self.show_colab)
        self.projeto_btn.clicked.connect(self.show_project)

    
    def show_colab(self):
        self.tabela.insertWidget(1, ColabPage())
        self.tabela.setCurrentIndex(1)

    def show_project(self):
        self.tabela.insertWidget(0, ProjetosPage(self))
        self.tabela.setCurrentIndex(0)

    def show_criar_project(self):
        self.tabela.insertWidget(2, )