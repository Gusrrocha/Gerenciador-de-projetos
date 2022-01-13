class Projetos():
    def __init__(self, id, nome, descricao, lista_tasks=[]):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.lista_tasks = lista_tasks
        
    def getPj(self):
        return [self.nome, self.descricao]