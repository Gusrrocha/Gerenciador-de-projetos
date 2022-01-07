from qt_core import *
from model.pj_dao import *
class CardProject(QWidget):
    def __init__(self, projeto, mainWindow):
        super().__init__()
        uic.loadUi('view/card_projeto.ui', self)

        self.mainWindow = mainWindow
        self.projeto = projeto
        self.nome.setText(projeto.nome)
        self.descricao.setText(projeto.descricao)

        self.edit_btn.clicked.connect(self.mousePressEvent)
        self.waste_btn.clicked.connect(self.waste_pj)
   
    def mousePressEvent(self, event):
        self.mainWindow.show_addproject(self.projeto)

    def waste_pj(self):
        del_pj(self.projeto.id)
        self.mainWindow.show_project()


