class Tarefas():
    def __init__(self, id, nome, descricao, status, id_projeto, lista_colab = []):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.status = status
        self.lista_colab = lista_colab
        self.id_projeto = id_projeto

    def getTask(self):
        return [self.nome, self.descricao, self.status, self.lista_colab, self.id_projeto]