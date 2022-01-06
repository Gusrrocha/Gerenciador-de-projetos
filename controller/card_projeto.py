from qt_core import *
class CardProject(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('view/card_projeto.ui', self)