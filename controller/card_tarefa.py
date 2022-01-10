from qt_core import *
class CardTarefas(QWidget):
    def __init__(self, mainWindow, tarefa):
        super().__init__()
        uic.loadUi('view/card_tarefas', self)

        self.mainWindow = mainWindow
        self.tarefa = tarefa
        self.nome_t.setText(tarefa.nome)
        self.desc_t.setText(tarefa.descricao)
        self.colab_t.setText(tarefa.lista_colab)
        if tarefa.status == 1:
            self.status.setText('Concluída')
        else:
            self.status.setText('Em progresso')
