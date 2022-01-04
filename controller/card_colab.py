from qt_core import *
import model.colab_dao as colab_dao
class CardColab(QWidget):
    def __init__(self, colaborador, mainWindow):
        super().__init__()
        uic.loadUi('view/card_colab.ui', self)

        self.colaborador = colaborador
        self.mainWindow = mainWindow
        self.nome.setText(colaborador.nome)
        self.email.setText(colaborador.email)
        
        self.excluir_btn.clicked.connect(self.excluir)
        self.editar_btn.clicked.connect(self.mousePressEvent)

    def excluir(self):
        colab_dao.delete(self.colaborador.id)
        self.mainWindow.show_colab()

    def mousePressEvent(self, event):
        self.mainWindow.show_criar_colaborador(self.colaborador)