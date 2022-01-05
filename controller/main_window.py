from qt_core import *
from controller.colab_page import ColabPage
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('view/main_window.ui', self)


        self.colab_btn.clicked.connect(self.show_colab)
    
    
    def show_colab(self):
        self.tabela.insertWidget(1, ColabPage())
        self.tabela.setCurrentIndex(1)