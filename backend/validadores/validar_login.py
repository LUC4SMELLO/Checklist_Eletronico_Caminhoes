from database.banco_dados_usuarios import buscar_usuario

def validar_login(nome_completo, senha):

    resultado = buscar_usuario(nome_completo, senha)
    if not resultado:
        return False, "Usuário Não Encontrado."

    if not nome_completo or not senha:
        return False, "Todos os Campos Devem ser Preechidos."
    
    if len(senha) < 8:
        return False, "Tamanho da Senha Inválido."
    
    return True, "Login Bem Sucedido!"
    
