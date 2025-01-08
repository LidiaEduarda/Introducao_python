
# ==============================> FOR <==================================

""""
As estruturas de repetição, também conhecidas como loops, são usadas para 
executar repetidamente um bloco de código enquanto uma condição específica é verdadeira.

O que é: A estrutura de repetição for é usada para repetir uma ação para cada item em uma sequência (como uma lista, texto, ou intervalo de números). 
É usado quando sabemos antecipadamente quantas vezes o bloco de codigo será executado.

Quando usar:
Percorrer listas, tuplas ou strings: Quando você precisa trabalhar com cada elemento individualmente.
Executar algo várias vezes: Por exemplo, repetir uma ação para cada número em um intervalo.
Processar itens de coleções: Para tarefas como filtrar, transformar ou calcular com base em itens de uma sequência.

OBS: Print dentro do loop: Mostra a lista em cada etapa do loop, atualizando à medida que os elementos são adicionados. 
     Print fora do loop: Mostra a lista apenas uma vez, ao final, já completa.
"""

'''1. Transformar - Criar '''

# Imagine que você tem uma lista de números e quer criar outra com o dobro de cada número.
lista = [1, 2, 3, 4, 5]
nova_lista_dobro = []
for num in lista:
    nova_lista_dobro.append(num * 2)
print(nova_lista_dobro)


'''2. Filtrar - Criar'''

# Criar uma lista com números pares de uma lista existente:
lista = [4, 8, 10, 5]
nova_lista_pares = []
for num in lista:
    if num % 2 == 0:
        nova_lista_pares.append(num)
print(nova_lista_pares)

'''3. Filtrar - Transformar - Criar'''

# Agora, você quer os quadrados apenas dos números ímpares.
lista = [2, 4, 7, 10]
nova_lista_impares_quadrado = []
for num in lista:
    if num % 2 != 0:
        nova_lista_impares_quadrado.append(num ** 2)
print(nova_lista_impares_quadrado)

'''Filtra'''
 
# Somar os numeros da lista [impares e pares] 
lista = [1, 19, 2, 15, 21, 12, 2]
soma_numeros_pares = 0
soma_numeros_impares = 0
for num in lista:
    if num % 2 == 0:
        soma_numeros_pares += 1
    else:
        soma_numeros_impares += 1
print("A lista contem {} números pares e {} números ímpares.".format(soma_numeros_pares, soma_numeros_impares))

# Somar os numeros impares da lista  
lista = [1, 5, 8, 15, 21, 12, 4]
soma_numeros_impares = 0
for num in lista:
    if num % 2 == 1:
        soma_numeros_impares += num
print("A soma dos elementos ímpares da lista = ", soma_numeros_impares)

'''4. Trabalhar com texto'''

# Imagine que você quer transformar uma lista de nomes para letras maiúsculas.
lista = ["Python", "Linguagem", "Programação"]
lista_transformada = []
for letra in lista:
    lista_transformada.append(letra.upper())
print(lista_transformada)

'''5. Criar combinações'''

# Criar combinações de dois conjuntos de números.
lista_combinacoes = []
for x in range(1,5):
    for y in range(1,5):
        lista_combinacoes.append((x,y))
print(lista_combinacoes)

# Gerar combinações de cor e formato
cores = ["vermelho", "azul", "verde"]
formatos = ["círculo", "quadrado"]
for cor in cores:
     for formato in formatos:
        print('{} - {}'.format(cores, formatos))


'''Mais Exemplos'''

# Tabuada de 1 - 9
for num in range(1,10):
    for mult in range(1,10):
        print('{} x {} = {}'.format(num, mult, num*mult))

# Contando até  10 de 2 em 2
for cont in range(1, 10, 2):
    print(cont)

# Contando de 0 até o valor que o usuario digitar - so os pares
v = int(input("Digite o valor: "))
for num in range(0, v, 2): # O v define o limite superior do intervalo gerado pelo range.
    print(num)

# Somando 5 numeros que o usuario digitar
s = 0
for num in range(1, 6):
    n = int(input("digite um valor: "))
    s = s + n
print("A soma dos valores é de", s)

# Usando variavel pra acumular soma da lista
lista = [1, 19, 2, 15, 21, 12, 2]
soma_lista = 0
for num in lista:
    soma_lista += num
print("A soma dos elementos da lista = ", soma_lista)
# Há uma forma mais simples de calcular somatórios
print("A soma dos elementos da lista = ", sum(lista)) # Mas a função sum() não permite somar elementos específicos, veja no promixo exemplo.

# Contando do valor do que o usuario digitar até 0 - apenas numeros pares
valor = int(input("Digite um valor: "))
if (valor % 2 == 1):
    valor = valor - 1 # para que o valor que o usurio colocar mesmo que seja um numero impa, que no resultado final do for ele fique par e descarte o restante
for num in range(valor, -1, -2): # conte do valor que o usuario digitar, até 0, tirando de 2 em 2, nesse caso o resultado daria impa, por isso realizei a expressao if acima
    print(num)

# Numeros divisiveis por 5, media dos numeros, soma, soam dos pares, numeros nulos. 
div_5  = 0 # Para contar números divisíveis por 5. Um número é divisível por 5 se o seu último algarismo é 0 ou 5. Exemplos: 75 é divisível por 5 pois termina com o algarismo 5, mas 107 não é divisível por 5 pois o seu último algarismo não é 0 e nem 5.
media = 0
soma = 0 # Para somar todos os números digitados
numNulos = 0 # Para contar números que são zero
somaPares = 0 # Para somar números pares

for cont in range(1, 5):
    num = int(input("Digite um numero: "))
    soma = soma + num

    if (num % 2 == 0):
        div_5 = div_5 + 1
        somaPares = somaPares + num

    if (num == 0):
        numNulos = numNulos + 1
        
print(f'A soma entre os numeros é = {soma}')
print(f'Os valores divisiveis por cinco são: {div_5}')
print(f'Os valores nulos são: {numNulos}')
print(f'A soma dos numreos pares é = {somaPares}')
print(f'A media dos numeros é = {soma/cont}')

# Quantos numeros tem entre 0 e 10, e some quantos numeros impares tem entre esse mesmo intervalo. Considerando que sera o usurio que vai passar os numeros.
# Caso queira somar todos os números ímpares, independentemente de estarem dentro do intervalo de 0 a 10, você precisa mover a operação de soma dos números ímpares para fora do loop, para garantir que ela ocorra após a entrada de todos os valores.
Tot10 = 0
SomaImpar = 0

for Cont in range(1, 7):
    Valor = int(input("Digite um valor: "))

    if (Valor >= 0) and (Valor <=10): 
        Tot10 = Tot10 + 1
                                                
        if (Valor % 2 == 1): # IF ANINHADO - Se você retirar o segundo if de dentro do primeiro, ele seria avaliado independentemente de o valor estar no intervalo de 0 a 10, o que alteraria a lógica do programa.
            SomaImpar = SomaImpar + Valor  # Só é executado se o primeiro if for verdadeiro, ou seja, se o valor estiver no intervalo entre 0 e 10. Isso garante que apenas os valores ímpares dentro do intervalo contribuam para SomaImpar.
print("Ao todo foram", Tot10, "numeros entre 0 e 10")
print("Nesse intervalo a soma dos numeros impares foi de", SomaImpar)
