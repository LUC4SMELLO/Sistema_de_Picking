from backend.models.usuarios import Usuario

def validar_cadastro(nome_completo, senha):

    if not nome_completo or not senha:
        return False, "Todos os Campos Devem Ser Preenchidos."
    
    resultado = Usuario.buscar_usuario(nome_completo)
    if resultado:
        return False, "Nome de Usuário Já Encontrado."
    
    if len(senha) < 8:
        return False, "Tamanho da Senha Inválido."
    
    
    return True, "Cadastro Válido."

    