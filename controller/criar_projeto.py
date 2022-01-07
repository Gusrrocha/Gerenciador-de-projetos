from qt_core import *
from model.projeto import Projetos
from model.pj_dao import *
import model.colab_dao as colab_dao
class AddProject(QWidget):
    def __init__(self, mainWindow, projeto=None):
        lista_add_colabs = []
        super().__init__()
        uic.loadUi('view/criar_projeto.ui', self)

        self.projeto = projeto
        self.mainWindow = mainWindow
        self.load_colabs()
        if self.projeto != False:
            self.nome_pj.setText(self.projeto.nome)
            self.desc_pj.setText(self.projeto.descricao)
        self.colab_add.clicked.connect(self.addColab)
        self.salvar_pj_btn.clicked.connect(self.salvar_pj)


    def load_colabs(self):
        # Colaboradores ComboBox
        t_l = []
        self.lista_colabs = colab_dao.selectAll()
        for colaborador in self.lista_colabs:
            t_l.append(colaborador.nome)
        self.colab_comboBox.addItems(t_l)

    def addColab(self):
        i = self.colab_comboBox.currentIndex()
        c = self.lista_colabs[i]
        if self.isExist(c) == False:
            self.lista_add_colabs.append(c)
            self.colab_added_comboBox.addItem(self.lista_colabs[i].nome)
            self.label_qt_colab.setText(f'Colaboradores alocados: {len(self.lista_add_colabs)}')

    def salvar_pj(self):
        nome = self.nome_pj.text()
        desc = self.desc_pj.text()
        if nome != '' and desc != '':
            if self.p == False:  # novo projeto
                add_pj(Projetos(None, nome, desc))
            else:
                pass

        # vai para a janela principal
        self.mainWindow.show_project()
