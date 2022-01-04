from qt_core import *
from model.colaborador import Colaboradores
from model.colab_dao import *
class CriarColab(QWidget):
    def __init__(self, mainWindow, colaborador=None):
        super().__init__()
        uic.loadUi('view/criar_colab.ui', self)
        self.mainWindow = mainWindow


        self.cancelar.clicked.connect(self.fechar_page)
        self.salvar.clicked.connect(self.salvar_colab)

    def fechar_page(self):
        self.mainWindow.tabela.setCurrentIndex(1)

    def salvar_colab(self):
        nome = self.nome.text()
        email = self.email.text()

        novo = Colaboradores(None, nome, email)
        add(novo)
    

        self.mainWindow.show_colab()
        
