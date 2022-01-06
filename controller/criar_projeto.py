from qt_core import *
class AddProject(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('view/criar_projeto.ui', self)