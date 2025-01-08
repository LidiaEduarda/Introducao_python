# -------------------------------------- CONJUNTOS-------------------------------------------------

'''
Definição: Python são coleções de elementos não ordenados e únicos. Eles são semelhantes a conjuntos matemáticos, permitindo operações como união, interseção e diferença.
Sintexe: Usa-se Colchetes {}.

Caractristicas: -> Elementos únicos: Não permitem duplicatas.
                -> Sem ordem: Não têm índice ou ordem fixa.
                -> Mutáveis: Você pode adicionar ou remover elementos, mas os próprios elementos devem ser imutáveis (como números, strings ou tuplas).

Quando usar:    -> Armazenar elementos únicos: Eles automaticamente eliminam duplicatas.
                -> Realizar operações matemáticas de conjuntos: Como união, interseção e diferença.
                -> Verificar rapidamente a presença de um elemento: Operações como in são mais rápidas em conjuntos.

'''


''' 1. Sistema de gerenciamento de usuários únicos (Evitar duplicatas)
   Cenário: Um sistema precisa registrar os usuários únicos que acessaram um site.'''

# Lista de usuários que acessaram o site (com duplicatas)
acessos = ["alice", "bob", "alice", "carol", "david", "bob"]

# Usando conjunto para armazenar usuários únicos
usuarios_unicos = set(acessos)
print(usuarios_unicos)  # Saída: {'alice', 'bob', 'carol', 'david'}

# Adicionando um novo usuário
usuarios_unicos.add("eve")
print(usuarios_unicos)


''' 2. Análise de preferências de clientes (Operações de conjuntos)
    Cenário: Uma loja deseja saber quais clientes compraram produtos em comum em diferentes categorias. '''

eletronicos = {"alice", "bob", "carol"}
roupas = {"bob", "carol", "david", "eve"}

# União (clientes que compraram pelo menos em uma das categorias)
todos_os_clientes = eletronicos.union(roupas)
print(todos_os_clientes)  

# Interseção (clientes que compraram em ambas as categorias)
clientes_comuns = eletronicos.intersection(roupas)
print(clientes_comuns)  

# Diferença (clientes que compraram apenas eletrônicos)
somente_eletronicos = eletronicos.difference(roupas)
print(somente_eletronicos)

# Diferença Simétrica (clientes exclusivos de cada categoria)
exclusivos = eletronicos.symmetric_difference(roupas)
print(exclusivos)  


''' 3. Verificação de palavras proibidas em um texto (Presença rápida)
    Cenário: Um sistema de moderação precisa identificar rapidamente palavras proibidas em um comentário. '''

# Lista de palavras proibidas
palavras_proibidas = {"spam", "fraude", "fake"}

# Comentário enviado por um usuário
comentario = "Este produto é fake e é uma fraude!"

# Quebrando o comentário em palavras
palavras = set(comentario.lower().split())

# Verificando se há palavras proibidas no comentário
if palavras.intersection(palavras_proibidas):
    print("Comentário contém palavras proibidas.")
else:
    print("Comentário está limpo.")


''' 4. Gerenciamento de inventário (Itens únicos e operações)
    Cenário: Um supermercado precisa gerenciar o inventário de produtos disponíveis em diferentes filiais. '''

# Produtos disponíveis em duas filiais
filial_a = {"maçã", "banana", "laranja"}
filial_b = {"banana", "laranja", "uva", "manga"}

# União (Todos os produtos disponíveis nas duas filiais)
todos_os_produtos = filial_a.union(filial_b)
print("Todos os produtos:", todos_os_produtos)

# Interseção (Produtos disponíveis em ambas as filiais)
comuns = filial_a.intersection(filial_b)
print("Produtos em ambas as filiais:", comuns)

# Diferença (Produtos exclusivos da filial A)
exclusivos_a = filial_a.difference(filial_b)
print("Exclusivos da filial A:", exclusivos_a)

# Diferença (Produtos exclusivos da filial B)
exclusivos_b = filial_b.difference(filial_a)
print("Exclusivos da filial B:", exclusivos_b)

# Diferença Simétrica (Produtos exclusivos de cada filial)
exclusivos_cada_filial = filial_a.symmetric_difference(filial_b)
print("Produtos exclusivos de cada filial:", exclusivos_cada_filial)
