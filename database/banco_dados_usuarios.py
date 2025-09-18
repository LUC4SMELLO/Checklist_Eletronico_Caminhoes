import sqlite3

def conectar_banco_dados_usuarios():
    return sqlite3.connect("TabelaUsuarios.db")

def criar_banco_dados_usuarios():

    conexao = conectar_banco_dados_usuarios()
    cursor = conexao.cursor()

    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS TabelaUsuarios (
    nome_completo VARCHAR(100),
    senha VARCHAR(50)
    )
    """
    )

    conexao.commit()
    conexao.close()

def inserir_usuario(nome_completo, senha):

    conexao = conectar_banco_dados_usuarios()
    cursor = conexao.cursor()

    cursor.execute(
    """
    INSERT INTO TabelaUsuarios (nome_completo, senha)
    VALUES (?, ?)
    """, (nome_completo, senha)
    )

    conexao.commit()
    conexao.close()

def excluir_usuario(nome_completo, senha):

    conexao = conectar_banco_dados_usuarios()
    cursor = conexao.cursor()

    cursor.execute(
    """
    DELETE FROM TabelaUsuarios
    WHERE nome_completo = ? AND senha = ?
    """, (nome_completo, senha)
    )

    conexao.commit()
    conexao.close()

def buscar_usuario(nome_completo, senha):

    conexao = conectar_banco_dados_usuarios()
    cursor = conexao.cursor()

    cursor.execute(
    """
    SELECT 1 FROM TabelaUsuarios
    WHERE nome_completo = ? AND senha = ?
    """, (nome_completo, senha)
    )

    resultado = cursor.fetchone()
        
    conexao.commit()
    conexao.close()

    return resultado