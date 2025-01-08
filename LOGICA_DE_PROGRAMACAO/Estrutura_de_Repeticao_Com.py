
# ========================> LIST COMPREHENSIONS <==========================

"""
As estruturas de repetição, também conhecidas como loops, são usadas para 
executar repetidamente um bloco de código enquanto uma condição específica é verdadeira. 

O que é: É uma maneira concisa e eficiente de criar listas em Python. 
Permite criar listas novas a partir de sequências existentes, aplicando transformações ou filtrando elementos de forma concisa.

Quando usar:
Criar listas simples: Quando precisa de uma nova lista transformada ou filtrada a partir de outra.
Legibilidade: Ideal para casos curtos e claros. Evite usar em situações muito complexas.
Substituir loops simples: Ela reduz a necessidade de escrever várias linhas de código.
"""

# 1. Criar uma lista transformada
# Imagine que você tem uma lista de números e quer criar outra com o dobro de cada número.
lista = [1, 2, 3, 4, 5]
nova_lista_dobro = [num * 2 for num in lista]
print(nova_lista_dobro)

# 2. Filtrar itens em uma lista
# Agora, digamos que você quer uma lista apenas com os números pares de numeros.
lista = [4, 8, 10, 5]
nova_lista_pares = [num for num in lista if num % 2 == 0]
print(nova_lista_pares)

# 3. Transformar e filtrar ao mesmo tempo
# Agora, você quer os quadrados apenas dos números ímpares.
lista = [2, 4, 7, 10]
nova_lista_impares_quadrado = [num ** 2 for num in lista if num % 2 != 0 ]
print(nova_lista_impares_quadrado)

# 4. Trabalhar com texto
# Imagine que você quer transformar uma lista de nomes para letras maiúsculas.
lista = ["Python", "Linguagem", "Programação"]
lista_transformada = [letra.upper() for letra in lista]
print(lista_transformada)

# 5. Criar combinações
# Se você quer criar combinações de dois conjuntos de números.
lista_combinacoes = [(x,y) for x in range (1, 6) for y in range (1, 6)] 
print(lista_combinacoes)

# 6. Criando listas comprehension 
# Cria uma lista chamada 'letras' usando list comprehension
lista_letras = [letra.upper() for letra in "palavra"] # A list comprehension percorre cada caractere l na string "palavra" e aplica o método l.upper() para transformar l em sua versão maiúscula.
print(lista_letras)

# EX: Cria uma lista chamada 'lista' usando list comprehension
lista = [ num for num in range(1,21)] # Para cada número 'num' no range, adiciona 'num' à lista
print(lista)

# EX: Criar uma lista de numeros divisiveis apenas por 3 e 7, no o intervao de 1-100 usando COMPREHENSIONS
lista_divisiveis_3_7 = [num for num in range(1,100) if num % 3 == 0 and num % 7 == 0 ] # Para cada número 'num' no range, verifica se 'num' é divisível por 3 e por 7, Se 'num' é divisível por ambos, adiciona 'num' à lista
print(lista_divisiveis_3_7)

# EX: Criar uma lista de numeros pares entre 1 - 50, usando COMPREHENSIONS
lista_pares = [num for num in range (1,51) if num % 2 == 0] # Inclua na lista_pares um num para todos os num na faixa de 1,50 se o num % 2 for = 0
print(lista_pares)

