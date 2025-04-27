class Arquivo:
    def __init__(self, nome, dono):
        self.nome = nome
        self.dono = dono
        self.permissoes = {}  # Dicionário para armazenar permissões por usuário

    def definir_permissao(self, usuario, leitura=False, escrita=False, execucao=False):
        self.permissoes[usuario.nome] = {
            'leitura': leitura,
            'escrita': escrita,
            'execucao': execucao
        }

    def verificar_permissao(self, usuario, tipo):
        return f"Permissão de {tipo} para o usuário '{usuario.nome}': {self.permissoes[usuario.nome].get(tipo, False)}"