# Criando usuários
from Model.Usuario import Usuario
from Model.Arquivo import Arquivo

usuario1 = Usuario("Alice")
usuario2 = Usuario("Bob")
usuario3 = Usuario("Samuel")

# Criando arquivo
arquivo = Arquivo("documento.txt", usuario1)

# Definindo permissões
arquivo.definir_permissao(usuario1, leitura=True, escrita=True, execucao=False)
arquivo.definir_permissao(usuario2, leitura=True, escrita=False, execucao=False)




# Verificando permissões
print(arquivo.verificar_permissao(usuario1, "leitura"))
print(arquivo.verificar_permissao(usuario1, "escrita"))
print(arquivo.verificar_permissao(usuario1, "execucao"))

print("----------------------------------------------------------")

print(arquivo.verificar_permissao(usuario2, "leitura"))
print(arquivo.verificar_permissao(usuario2, "escrita"))
print(arquivo.verificar_permissao(usuario2, "execucao"))

print("----------------------------------------------------------")

print(arquivo.verificar_permissao(usuario3, "leitura"))
print(arquivo.verificar_permissao(usuario3, "escrita"))
print(arquivo.verificar_permissao(usuario3, "execucao"))