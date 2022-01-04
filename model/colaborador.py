class Colaboradores():
    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email

    def getColab(self):
        return [self.nome, self.email]