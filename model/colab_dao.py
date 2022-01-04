import sqlite3
from model import dbase
from model.colaborador import Colaboradores

lista = []
def add(colaborador):
    lista.append(colaborador)
    try:
        conn = dbase.connect() # conecta
        cursor = conn.cursor() # se move no banco
        sql = """INSERT INTO Colaboradores (nome, email)
            VALUES (?, ?);"""
        cursor.execute(sql, colaborador.getColab())
        conn.commit()
    except Exception as e:
        print("Erro!")
        print(e)
    finally:
        conn.close()

def edit(colaborador):
    pass
def delete(id):
    pass