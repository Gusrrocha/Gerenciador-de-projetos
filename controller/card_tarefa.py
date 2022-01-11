from qt_core import *
class CardTarefas(QWidget):
    def __init__(self, tarefa):
        super().__init__()
        uic.loadUi('view/card_tarefas.ui', self)

        self.tarefa = tarefa
        self.nome_t.setText(tarefa.nome)
        self.desc_t.setText(tarefa.descricao)
        self.colab_t.setText(str(tarefa.id_projeto))
        if self.tarefa.status == 1:
            self.status.setText('Concluída!')
        elif self.tarefa.status == 0:
            self.status.setText('Em progresso!')
