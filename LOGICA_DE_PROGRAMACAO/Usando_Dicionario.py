# --------------------------------------DICIONARIO-------------------------------------------------


'''
Definição: É uma estrutura de dados que armazena pares de chave e valor. Ele é usado quando você deseja associar cada item (o valor) a uma chave única.
Chave: Identifica o valor (como um rótulo).
Valor: A informação associada à chave.
Um dicionário é definido entre chaves {} e cada par chave-valor é separado por dois pontos :.

Características importantes: -> Chaves únicas: Cada chave deve ser única; valores podem se repetir.
                             -> Mutável: Você pode adicionar, modificar ou remover itens.
                             -> Não ordenado (até Python 3.6): A ordem dos itens não é garantida.

Quando usar: -> Quando você precisa organizar dados por rótulos ou chaves:
            Exemplo: Armazenar informações de uma pessoa como nome, idade e cidade.

            -> Quando precisa associar um valor a uma chave única:
            Exemplo: Criar uma tabela de tradução, como associar "gato" a "cat" e "cachorro" a "dog".

            -> Quando quer contar a frequência de itens:
            Exemplo: Descobrir quantas vezes cada fruta aparece em uma lista, como "maçã: 3", "banana: 2".

            -> Quando precisa acessar dados de forma rápida (por chave):
            Exemplo: Procurar o nome de uma pessoa pelo número de identificação (ID), como encontrar "Ana" usando o ID "001".

            -> Quando trabalha com configurações ou preferências:
            Exemplo: Armazenar configurações de um aplicativo, como o tema escuro, idioma e notificações habilitadas.

            -> Quando precisa relacionar categorias a listas de itens:
            Exemplo: Agrupar itens como frutas em uma categoria e legumes em outra.

            -> Quando precisa atualizar ou modificar dados dinamicamente:
            Exemplo: Atualizar a idade de uma pessoa em um cadastro sem precisar recriar todo o conjunto de informações.

            -> Quando precisa representar dados estruturados:
            Exemplo: Guardar informações de um produto, como nome, preço e quantidade em estoque.

            -> Quando precisa armazenar pares chave-valor em grande escala:
            Exemplo: Organizar resultados de buscas ou documentos indexados, como associar um documento ao seu conteúdo.

            -> Quando precisa evitar duplicatas nas chaves:
            Exemplo: Armazenar números únicos, como CPF de pessoas em um cadastro.

'''

# 1. Vamos começar pelo básico. Crie um dicionário que represente informações sobre uma pessoa, como nome, idade, cidade natal e profissão.

dic_pessoa = {"Nome": "Lidia Eduarda", "Idade": 25, "Cidade_Natal": "Teotônio_Vilela", "Profissão": "Geografa"}
print(dic_pessoa)


# 2. Vamos explorar os dados. Acesse e imprima valores específicos do dicionário que você criou no exercício anterior, como o nome e a idade da pessoa.

print(f'eu nasci em {dic_pessoa["Cidade_Natal"]}')

nome_pessoa = dic_pessoa["Nome"]
nome_idade = dic_pessoa["Idade"]
profissao_pessoa = dic_pessoa["Profissão"]
print(f"Meu nome é {nome_pessoa}, e tenho {nome_idade} anos de idade, minha profissão é {profissao_pessoa}")


# 3. Hora de atualização. Modifique o valor de um item no dicionário que você criou e, em seguida, imprima o dicionário atualizado.
dic_pessoa["Idade"] = 26
print("Dicionario atualizado:", dic_pessoa)


# 4. Enriqueça o dicionário. Adicione informações adicionais à pessoa no dicionário, como seu endereço de e-mail e número de telefone.

dic_pessoa["Email"] = "lidiaeduarda@gmail.com"
dic_pessoa["Telefone"] = "(82)988775001"
print(dic_pessoa)


# 5. Hora de simplificar. Remova um item do dicionário, como o número de telefone, e imprima o dicionário atualizado.

dic_pessoa.pop("Telefone")
print("Dicionario tualizado", dic_pessoa)


# 6. Crie um dicionario com nomes de amigos, Seja um detetive. Peça ao usuário para inserir o nome de um amigo e verificar se esse nome existe no dicionário de amigos. Imprima uma mensagem informando se o amigo está ou não na lista.

dic_amigos = {"A": "Lidia", "B": "Maria", "C": "José"}
print(dic_amigos)

nome_amigo = input("Digite o nome do amigo: ")
if nome_amigo in dic_amigos.values():
    print(f"{nome_amigo} faz parte do dicionario de amigos")
else: 
    print(f"{nome_amigo} não faz parte do dicionario de amigos")


# 7. Faça uma contagem. Conte quantos amigos existem no dicionário e imprima o resultado.
    
print(f" Ao todo são {len(dic_amigos)} amigos")
print(dic_amigos.values())


# 8. Crie um dicionário de tradução que mapeie palavras de um idioma para outro (por exemplo, inglês para espanhol). Peça ao usuário para inserir uma palavra em inglês e, em seguida, imprima a tradução correspondente.

dic_traducao = {
    "hello": "hola",
    "goodbye": "adiós",
    "thank you": "gracias"
}

palavra_ingles = input("Digite a palavra: ")
if palavra_ingles in dic_traducao:
    print(f'A traducao para sua palavra {palavra_ingles} é {dic_traducao[palavra_ingles]}') # A f-string (string formatada)permite incluir expressões dentro de {} que são avaliadas e inseridas na string resultante. O Python primeiro avalia a expressão dentro das chaves {}, que é dic_traducao[palavra_ingles]. Neste caso, ele substitui palavra_ingles por "hello", resultando em dic_traducao["hello"]. O dicionário dic_traducao é consultado com a chave "hello", retornando "hola".
else:
    print(f'A palavra {palavra_ingles} não existe no dicionario de tradução.')


# 9. Vamos às compras. Crie um dicionário que representa o estoque de uma loja, com produtos como chaves e detalhes em estoque como valores. 
# Permita que o usuário insira um produto e verifique se ele está em estoque. Se desejar, informe a quantidade em estoque; caso contrário, informe que o produto não está disponível.

dic_loja_estoque = {
    "Caderno": 5,
    "Caneta": 10,
    "Marca_texto": 7,
    "Borracha": 6,
    "Bolsa": 8,
    "Corretivo": 2
}

produto_desejado = input("Digite o nome do produto: ")

if produto_desejado in dic_loja_estoque:
    print(f'O produto {produto_desejado} está disponivel, contendo {dic_loja_estoque[produto_desejado]} unidades em estoque.')

else:
    print(f'O produto {produto_desejado} não está disponivel.')


# 11. Crie dois dicionários diferentes e, em seguida, crie um terceiro dicionário que seja a mescla dos dois. Imprima o dicionário resultante.

dic_estados_diversos = {
    "SP": "São Paulo",  
    "PR": "Curitiba",
    "RJ": "Rio de Janeiro",
    "MG": "Belo Horizonte"
}

dic_estados_nordeste = {
    "AL": "Maceio",
    "PE": "Recife",
    "CE": "Fortaleza",
    "BA": "Bahia"
}

dic_estados_misturados = dic_estados_diversos.copy()
dic_estados_misturados.update(dic_estados_nordeste)
print(dic_estados_misturados)


# EX: Definição de um dicionário com siglas de estados como chaves e nomes completos como valores
dic_estados = {"MG": "Minas Gerais", "PR": "Paraná", "BA": "Bahia", "RN": "Rio Grande do Norte", "AM": "Amazonas"}
for chave in dic_estados: # Loop através das chaves do dicionário (siglas dos estados)
    print(chave) 

for valor in dic_estados.values(): # Loop através dos valores do dicionário (nomes completos dos estados)
    print(valor)

for (chav, valor) in dic_estados.items(): # Loop através dos itens do dicionário. Retorna uma lista de tuplas, onde cada tupla é composta por (chave, valor), ou seja, (sigla, nome do estado).
    print('A sigla para {} é {}'. format(chav, valor)) # sig é a sigla do estado e est é o nome completo do estado.

