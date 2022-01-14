
from controller.card_projeto import CardProject
from qt_core import *
from model.pj_dao import *
import model.colab_dao as colab_dao
import model.tarefa_dao as tarefa_dao
from controller.card_tarefa import CardTarefas
from model.tarefa import Tarefas
class AddProject(QWidget):
    def __init__(self, mainWindow, projeto=None):
        super().__init__()
        uic.loadUi('view/projeto.ui', self)

        self.lista_task = []
        self.lista_colabs = []
        self.lista_added_colabs = []
        self.projeto = projeto
        self.mainWindow = mainWindow
        
        self.load_colabs()
        
        
        if self.projeto != False:
            self.nome_pj.setText(self.projeto.nome)
            self.desc_pj.setText(self.projeto.descricao)
            self.load_tasks(self.projeto)
        self.colab_add.clicked.connect(self.addColab)
        self.salvar_pj_btn.clicked.connect(self.salvar_pj)
        self.colab_discard.clicked.connect(self.removeColab)
        self.add_task_btn.clicked.connect(self.addTask)
                
        
    def load_colabs(self):
        t_l = []
        self.lista_colabs = colab_dao.selectAll()
        for colaborador in self.lista_colabs:
            t_l.append(colaborador.nome)
        self.colab_comboBox.addItems(t_l)

    def load_tasks(self, projeto):
        for i in reversed(range(self.painel_tarefas.count())):
            self.painel_tarefas.itemAt(i).widget().deleteLater()

        l = self.projeto.lista_tasks
        for t in l:
            self.painel_tarefas.addWidget(CardTarefas(t))
        
    def load_t(self):
        for i in reversed(range(self.painel_tarefas.count())):
            self.painel_tarefas.itemAt(i).widget().deleteLater()

        l = self.lista_task
        for t in l:
            self.painel_tarefas.addWidget(CardTarefas(t))

    def addColab(self):
        i = self.colab_comboBox.currentIndex()
        c = self.lista_colabs[i]
        if self.isExist(c) == False:
            self.lista_added_colabs.append(c)
            self.colab_added_comboBox.addItem(self.lista_colabs[i].nome)
            self.label_qt_colab.setText(f'Colaboradores alocados: {len(self.lista_added_colabs)}')

    def addTask(self):
        try:
            nome = self.nome_task.text()
            desc = self.desc_task.text()
            if (self.done_btn.isChecked()):
                status = 1
            elif (self.pending_btn.isChecked()):
                status = 0
            colab = len(self.lista_added_colabs)
            if nome != '' and desc != '' and colab > 0:
                if self.projeto == False:
                    tarefa_dao.add_task(Tarefas(None, nome, desc, status, colab))
                    self.lista_task.append(Tarefas(None, nome, desc, status, colab))
                    self.load_t()
                    self.clear()
            else:
                QMessageBox.about(self, "Erro", "Preencha todas as colunas!")
        except Exception as e:
            QMessageBox.about(self, "Erro", "Preencha todas as colunas!")
            print(e)
        
            
            
            
        

    def isExist(self, colab):
        for c in self.lista_added_colabs:
            if c.id == colab.id:
                return True
        return False
    
    def clear(self):
        self.nome_task.clear()
        self.desc_task.clear()
        self.lista_added_colabs = []
        self.colab_added_comboBox.clear()
        self.label_qt_colab.setText(f'Colaboradores alocados: 0')
        
        self.done_btn.setChecked(False)
        self.pending_btn.setChecked(False)
        


    def removeColab(self):
        i = self.colab_added_comboBox.currentIndex()
        if i >= 0:
            self.lista_added_colabs.remove(self.lista_added_colabs[i])
            self.colab_added_comboBox.removeItem(i)
            self.label_qt_colab.setText(f'Colaboradores alocados: {len(self.lista_added_colabs)}')

    def salvar_pj(self):
        nome = self.nome_pj.text()
        desc = self.desc_pj.text()
        task = self.lista_task
        if nome != '' and desc != '':
            if self.projeto == False:  # novo projeto
                    novo = Projetos(None, nome, desc, task)
                    add_pj(novo)
            else:
                pass
            
        


        # vai para a janela principal
        self.mainWindow.show_project()