class Arquivo:
    def __init__(self, nome, dono):
        self.nome = nome
        self.dono = dono
        self.permissoes = {}

    def definir_permissao(self, usuario, leitura=False, escrita=False, execucao=False):
        self.permissoes[usuario.nome] = {
            'leitura': leitura,
            'escrita': escrita,
            'execucao': execucao
        }

    def verificar_permissao(self, usuario, tipo):
        # Corrigido para evitar erro caso o usuário não tenha permissões definidas
        permissoes_usuario = self.permissoes.get(usuario.nome, {})
        return f"Permissão de {tipo} para o usuário '{usuario.nome}': {permissoes_usuario.get(tipo, False)}"