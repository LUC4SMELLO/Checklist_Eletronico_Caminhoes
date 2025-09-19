import sqlite3

def conectar_banco_dados_checklist():
    return sqlite3.connect("TabelaChecklist.db")

def criar_banco_dados_checklist():

    conexao = conectar_banco_dados_checklist()
    cursor = conexao.cursor()

    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS TabelaChecklist (
    data VARCHAR(10),
    usuario VARCHAR(50),
    caminhao VARCHAR(2),
    tipo VARCHAR(7),
    pneu VARCHAR(10),
    estepe VARCHAR(10),
    adesivos_refletivos VARCHAR(10),
    cinto_seguranca VARCHAR(10),
    freio VARCHAR(10),
    tacografo VARCHAR(10),
    luzes VARCHAR(10),
    farois VARCHAR(10),
    indicadores VARCHAR(10),
    documentos_veiculo VARCHAR(10),
    observacao VARCHAR(500)
    )
    """
    )

    conexao.commit()
    conexao.close()
