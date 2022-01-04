from qt_core import *
import model.colab_dao as colab_dao
from controller.card_colab import CardColab
class ColabPage(QWidget):
    def __init__(self, mainWindow):
        super().__init__()
        uic.loadUi('view/colab.ui', self)

        self.mainWindow = mainWindow

        self.load()

    def load(self):
        lista = colab_dao.selectAll()
        for colab in lista:
            self.painel_colab.addWidget(
                CardColab(colab, self.mainWindow))
        
