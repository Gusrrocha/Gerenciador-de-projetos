from qt_core import *
import model.colab_dao as colab_dao
from model.colaborador import Colaboradores
class ColabPage(QWidget):
    lista_colabs = []
    colab_atual = None

    def __init__(self):
        super().__init__()
        uic.loadUi('view/colab.ui', self)

        self.salvar_btn.clicked.connect(self.salvar)
        self.excluir_btn.clicked.connect(self.excluir)
        self.painel.verticalHeader().setVisible(False)
        self.painel.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) 
        self.painel.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.cancel_edit.clicked.connect(self.cancel_edicao)
        self.cancel_edit.hide()
        self.load()
        self.painel.clicked.connect(self.click_linha)

    def load(self):
        self.lista_colabs = colab_dao.selectAll()

        self.clear()
        self.painel.setRowCount(0)
        for c in self.lista_colabs:
            self.add_colab(c)
    def cancel_edicao(self):
        self.clear()
        self.cancel_edit.hide()
    def salvar(self):
        nome = self.nome.text()
        email = self.email.text()
        
        if self.colab_atual != None:
            edit_colab = Colaboradores(None, nome, email)
            edit_colab.id = self.colab_atual.id 
            colab_dao.edit(edit_colab)

        else:
            novo_colab = Colaboradores(None, nome, email)
            colab_dao.add(novo_colab)

        self.load()
        
    def excluir(self):
        if self.colab_atual != None:
            colab_dao.delete(self.colab_atual.id)
            self.load()

    def add_colab(self, c):
        rowCount = self.painel.rowCount()
        self.painel.insertRow(rowCount)

        id = QTableWidgetItem(str(c.id))
        nome = QTableWidgetItem(c.nome)
        email = QTableWidgetItem(c.email)

        self.painel.setItem(rowCount, 0, id)
        self.painel.setItem(rowCount, 1, nome)
        self.painel.setItem(rowCount, 2, email)

    def clear(self):
        self.nome.clear()
        self.email.clear()
        self.colab_atual = None

    def click_linha(self):
        selected_row = self.painel.currentRow()
        self.colab_atual = self.lista_colabs[selected_row]
        self.nome.setText(self.colab_atual.nome)
        self.email.setText(self.colab_atual.email)
        self.cancel_edit.show()
