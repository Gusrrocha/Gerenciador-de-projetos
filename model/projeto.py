class Projetos():
    def __init__(self, id, nome, descricao):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        
    def getPj(self):
        return [self.nome, self.descricao]