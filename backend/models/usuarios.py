from database.banco_dados_usuarios import conectar_banco_dados_usuarios

from backend.constantes.banco_dados import TABELA_USUARIOS


class Usuario:
    def __init__(self, nome_completo, senha):
        self.nome_completo = nome_completo
        self.senha = senha


    def inserir_usuario(self):
        conexao = conectar_banco_dados_usuarios()
        cursor = conexao.cursor()

        cursor.execute(
        f"""
        INSERT INTO {TABELA_USUARIOS} (
        nome_completo, senha
        )
        VALUES (?, ?)
        """, (self.nome_completo, self.senha)
        )

        conexao.commit()
        conexao.close()
    

    def excluir_usuario(self):
        conexao = conectar_banco_dados_usuarios()
        cursor = conexao.cursor()

        cursor.execute(
        f"""
        DELETE FROM {TABELA_USUARIOS}
        WHERE nome_completo = ? AND senha = ?
        """, (self.nome_completo, self.senha)
        )

        conexao.commit()
        conexao.close()
    

    @staticmethod
    def buscar_usuario(nome_completo):
        conexao = conectar_banco_dados_usuarios()
        cursor = conexao.cursor()

        cursor.execute(
        f"""
        SELECT * FROM {TABELA_USUARIOS}
        WHERE nome_completo = ?
        """, (nome_completo,)
        )

        resultado = cursor.fetchall()

        conexao.commit()
        conexao.close()

        return resultado
