import sqlite3

# Função para conectar ao banco
def conectar():
    return sqlite3.connect("estudantes.db")

# Função para criar a tabela caso não exista
def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS estudantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            nome_mae TEXT NOT NULL,
            nome_pai TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            idade INTEGER NOT NULL,
            cpf TEXT UNIQUE NOT NULL,
            turma TEXT NOT NULL,
            senha TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()