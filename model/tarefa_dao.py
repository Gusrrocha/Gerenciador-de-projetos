import sqlite3
from model import dbase
from model.tarefa import Tarefas

lista_tarefa = []
def add_task(tarefa):
    lista_tarefa.append(tarefa)
    try:
        conn = dbase.connect()
        cursor = conn.cursor()
        sql = """INSERT INTO Tarefas (nome, descricao, status, colab)
              VALUES (?, ?, ?, ?);"""
        cursor.execute(sql, tarefa.getTask())
        conn.commit()
    except Exception as e:
        print("Deu erro!")
        print(e)
    finally:
        conn.close()

def edit_task(tarefa):
    pass

def delete_task(id):
    pass

def selectAll():
    pass

