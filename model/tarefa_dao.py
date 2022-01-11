import sqlite3
from model import dbase
from model.tarefa import Tarefas

lista_tarefa = []
def add_task(tarefa):
    lista_tarefa.append(tarefa)
    try:
        conn = dbase.connect()
        cursor = conn.cursor()
        sql = """INSERT INTO Tarefas (nome, descricao, status, id_projeto, colab)
              VALUES (?, ?, ?, ?, ?);"""
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

def selectAll(id_proj):
    lista_t = []
    try:
        conn = dbase.connect()
        cursor = conn.cursor()
        sql = """SELECT * FROM Tarefas WHERE id_projeto=?"""
        cursor.execute(sql, [id_proj])
        result = cursor.fetchall()
        for c in result:
            nova_tarefa = Tarefas(c[0],c[1],c[2],c[3],c[4],c[5])
            lista_t.append(nova_tarefa)
    except Exception as e:
        print(e)
    finally:
        conn.close()
    return lista_t

