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
    try:
        conn = dbase.connect()
        cursor = conn.cursor()
        sql = """UPDATE Colaboradores SET nome=?,email=? WHERE id=?;"""
        l = colaborador.getColab()
        l.append(colaborador.id)
        cursor.execute(sql, l)
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()

def delete(id):
    try:
        conn = dbase.connect()
        cursor = conn.cursor()
        sql = """DELETE FROM Colaboradores WHERE id = ?"""
        cursor.execute(sql, [id])
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()

def selectAll():
    lista = []
    try:
        conn = dbase.connect()
        cursor = conn.cursor()
        sql = """SELECT * FROM Colaboradores ORDER BY upper(nome)"""
        cursor.execute(sql)
        result = cursor.fetchall()
        for c in result:
            novo_colab = Colaboradores(c[0],c[1],c[2])
            lista.append(novo_colab)
    except Exception as e:
        print(e)
    finally:
        conn.close()
    return lista