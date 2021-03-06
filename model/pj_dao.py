import sqlite3
from model import dbase
from model.projeto import Projetos

lista_pj = []
def add_pj(projeto):
    lista_pj.append(projeto)
    try:
        conn = dbase.connect() # conecta
        cursor = conn.cursor() # se move no banco
        sql = """INSERT INTO Projetos (nome, descricao)
            VALUES (?, ?);"""
        cursor.execute(sql, projeto.getPj())
        conn.commit()
    except Exception as e:
        print("Erro!")
        print(e)
    finally:
        conn.close()

def edit_pj(projeto):
    try:
        conn = dbase.connect()
        cursor = conn.cursor()
        sql = """UPDATE Projetos SET nome=?, descricao=? WHERE id=?;"""
        p = projeto.getPj()
        p.append(projeto.id)
        cursor.execute(sql, p)
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()

def del_pj(id):
    try:
        conn = dbase.connect()
        cursor = conn.cursor()
        sql = """DELETE FROM Projetos WHERE id = ?"""
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
        sql = """SELECT * FROM Projetos ORDER BY upper(nome)"""
        cursor.execute(sql)
        result = cursor.fetchall()
        for p in result:
            novo_prj = Projetos(p[0],p[1],p[2])
            lista.append(novo_prj)
    except Exception as e:
        print(e)
    finally:
        conn.close()
    return lista
