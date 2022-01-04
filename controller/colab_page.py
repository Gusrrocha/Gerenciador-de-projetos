from qt_core import *
class ColabPage(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('view/colab.ui', self)
        
