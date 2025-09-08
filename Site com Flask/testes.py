from database.banco_dados_checklist import conectar_banco_dados_checklist, criar_banco_dados_checklist, inserir_checklist

criar_banco_dados_checklist()

conexao = conectar_banco_dados_checklist()
cursor = conexao.cursor()

# cursor.execute(
# """
# DELETE FROM TabelaChecklist
# WHERE data
# """
# )
cursor.execute(
"""
SELECT * FROM TabelaChecklist
"""
)

resultado = cursor.fetchall()

for i in resultado:
    print(i)