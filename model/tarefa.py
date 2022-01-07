class Tarefas():
    def __init__(self, id, nome, descricao, status, lista_colab = []):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.status = status
        self.lista_colab = lista_colab