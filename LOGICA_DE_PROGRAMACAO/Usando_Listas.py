
# -------------------------------------- LISTAS-------------------------------------------------

'''
Definição: Uma lista é uma coleção mutável (pode ser alterada).
Sintaxe: Usam colchetes [ ].
Características: -> Permitem adicionar, remover ou modificar elementos.
                 -> Podem conter diferentes tipos de dados (int, str, etc.).
                 -> Úteis para coleções que podem mudar ao longo do tempo.

Quando usar listas? -> Quando você precisa modificar os dados.
                    -> Quando a ordem dos itens pode mudar.
                    -> Para operações como adicionar, remover ou ordenar elementos.
'''


# EX: Cria dois loops que solicitam ao usuário a entrada de idades e alturas, armazenando-as em duas listas separadas: idades e alturas.

idades = []
alturas = []

for res in range(2):
    while True: 
        try:
            idade = int(input('Qual a sua IDADE: '))
            if idade <0:
                print('Por favor, insira uma idade válida (número positivo')
                continue
            break
        except ValueError:
            print("Entrada inválida! Insira um número inteiro para a idade.")

    while True:
        try:
            altura = float(input('Qual sua ALTURA: ').replace(',', '.'))
            if altura <= 0:
                print("Por favor, insira uma altura válida (número positivo)." )   
                continue
            break
        except ValueError:
            print("Entrada inválida! Insira um número válido para a altura (ex.: 1.75).")

            
idades.append(idade)
alturas.append(altura)

print(idades)
print(alturas)


# EX: Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

Lista_Num_Inteiros = [-1, 0, 1, 2, 3]
print(Lista_Num_Inteiros)


# EX: Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

Lista_Num_Reais = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
Lista_Num_Reais.reverse()
print(Lista_Num_Reais)


# EX: Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
media = 0
soma = 0
lista_notas = [8.0, 8.5, 9.0, 9.5]

for n in lista_notas:
    soma = soma + n
    media = soma / len(lista_notas)
print("As notas são", lista_notas, "e a media das notas é igual a", media)


# EX: Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

quant_consoantes = 0
consoantes = []
lista_vogais = ["A", "E", "I", "O", "U", "B", "C", "D", "E", "F"]

for letra in lista_vogais:
    if letra not in "AEIOU":
        quant_consoantes = quant_consoantes + 1
        consoantes.append(letra)
print("No total foram", quant_consoantes, " consoantes, são elas:", consoantes)


# EX: Faça um Programa que leia 10 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

pares = []
impares = []
num_amostra = []

for cont in range(0, 10):
    numero = int(input("Digte um numero: "))
    num_amostra.append(numero)
    if (numero % 2 == 0):
        pares.append(numero)
    else:
        impares.append(numero)

print(f"Os numeros foram: {num_amostra}, sendo os pares: {pares} e os impares: {impares}")

# Outra forma de ressolver

numImp = []
numPar = []
numInt = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for n in numInt:
    if(n % 2 == 0):
        numPar.append(n)
    else:
        numImp.append(n)

print('Os numeros foram', numInt)
print('Os numeros pares foram', numPar)
print('Os numeros impares foram', numImp)


# EX: Faça um Programa que peça as quatro notas de 5 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0. 

lista_medias = []

for aluno in range(0,2):
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segiunda nota: "))
    n3 = float(input("Digite a terceira nota: "))
    n4 = float(input("Digite a quarta nota: "))
    soma_medias = (n1 + n2 + n3 + n4) / 4
    lista_medias.append(soma_medias)
    print(f"Média do aluno {aluno + 1 } = {soma_medias:.2f}")


contador = 0
for nota in lista_medias:
    if nota >=7:
        contador = contador + 1
        
print(f'A media dos alunos foram {lista_medias}')
print(f"{contador} alunos tiraram nota maior ou igual a 7")


# EX: Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

numeros_inteiros = [2,3,4,5,6]
soma = 0
multiplicacao = 1

for num in numeros_inteiros:
    soma += num
    multiplicacao *= num

print('Os numeros são', numeros_inteiros)
print('A soma dos numeros é de', soma)
print('A multipliçacão dos numeros foi de', multiplicacao)

# Outra forma de ressolver

numeros_inteiros = [] 

for n in range(5):
    numero = int(input('Digite um numero:'))
    numeros_inteiros.append(numero)

soma = sum(numeros_inteiros)

multiplicacao = 1

for num in numeros_inteiros:
    multiplicacao *= num

print('Os numeros são', numeros_inteiros)
print('A soma dos numeros é de', soma)
print('A multipliçacão dos numeros foi de', multiplicacao)


# EX: Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder
# positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
count_sim = 0
perguntas = [
    "A - Telefonou para a vítima?",
    "B - Esteve no local do crime?",
    "C - Mora perto da vítima?",
    "D - Devia para a vítima?",
    "E - Já trabalhou com a vítima?" 
]

for pergunta in perguntas:
    resposta_temporaria = input(pergunta)
    if (resposta_temporaria == 'sim'):
        count_sim = count_sim + 1

if (count_sim == 2):
    classificacao = 'Suspeito'

elif (count_sim >= 3) and (count_sim <= 4):
    classificacao = 'Cumplice'

elif (count_sim == 5):
    classificacao = 'Culpado'

else:
    classificacao = 'Inocente'

print('Voce é considerado', classificacao)


# EX: Definição de uma lista de tuplas, onde cada tupla contém quatro elementos
lista = [(18, 28, 15, 22), (18, 15, 25, 19), (16, 24, 21, 28), (18, 13, 18, 13)]
for (ele1, ele2, ele3, ele4) in lista: # Loop através de cada tupla na lista
    print('A 3a nota = {}'.format(ele3))  # Para cada tupla, imprime o terceiro elemento (ele3)

for elemento in lista: #para acessar o terceiro valor de cada tupla, por exemplo, e imprimir a 3ª nota, você pode usar o índice da tupla dentro do laço. Aqui está o código correto para isso:lista = [(18, 28, 15, 22), (18, 15, 25, 19), (16, 24, 21, 28), (18, 13, 18, 13)]
    print(f'O elemento da poição 3 é = {elemento[2]}')  
    

# EX: Iterando sobre uma lista
lista = [1, 19, 2, 15, 21, 12, 2]
for num in lista:
    print(num)


