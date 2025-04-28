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
                permissoes_usuario = self.permissoes.get(usuario.nome, {})
                for permissao, valor in permissoes_usuario.items():
                    if permissao == tipo:
                        return f"Permissão de {tipo} para o usuário '{usuario.nome}': {valor}"
                return f"Permissão de {tipo} para o usuário '{usuario.nome}': False"