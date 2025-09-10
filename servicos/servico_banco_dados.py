from database.banco_dados_checklist import criar_banco_dados_checklist
from database.banco_dados_usuarios import criar_banco_dados_usuarios

def inicializar_bancos_dados():
    
    criar_banco_dados_checklist()
    criar_banco_dados_usuarios()