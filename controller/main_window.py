from qt_core import *
from controller.colab_page import ColabPage
from controller.criar_colab import CriarColab
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('view/main_window.ui', self)


        self.colab_btn.clicked.connect(self.show_colab)
        self.novo_colab_btn.clicked.connect(self.show_criar_colab)
    
    def show_criar_colab(self, colaborador=None):
        self.tabela.insertWidget(2, CriarColab(self, colaborador))
        self.tabela.setCurrentIndex(2)
    
    def show_colab(self):
        self.tabela.insertWidget(1, ColabPage(self))
        self.tabela.setCurrentIndex(1)