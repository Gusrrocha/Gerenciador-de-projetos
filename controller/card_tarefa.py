from qt_core import *
class CardTarefas(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('view/card_tarefas', self)