
# ============================> WHILE <==================================

"""
As estruturas de repetição, também conhecidas como loops, são usadas para 
executar repetidamente um bloco de código enquanto uma condição específica é verdadeira. 
Em Python, existem três estruturas principais de repetição (ou loops): 
FOR, wHILE e compreensão de listas (list comprehensions). 

O loop while repete um bloco de código enquanto uma condição especificada é verdadeira.
Ele é ideal para situações em que o número de iterações não é conhecido de antemão e depende 
de uma condição que pode ser verdadeira ou falsa em algum momento durante a execução do loop.
"""


# EX: Contando até 10
contando = 0

while (contando <= 10):
 print(contando)
 contando = contando + 1

print('TERMINEI DE CONTAR!')



# EX: Contando de 10 até 0 tirando 2
contadorr = 10

while (contadorr >=0):
     print(contadorr)
     contadorr = contadorr - 2

print('TERMINEI DE CONTAR')



# EX: Soma   
contadorr = 1                 
soma = 0 

while contadorr <=5:
     num = int(input("Digite um numero: "))
     soma = soma + num
     contadorr = contadorr + 1
print(" A soma dos numros foi de", soma)



# EX: Juntar dinheiro
dinheiro_j = 0
ajudante = 10
print(f"Tenho {dinheiro_j} no bolso")

while dinheiro_j <= 50:
    dinheiro_j = dinheiro_j + ajudante
    print(f"Obaaa! ganhei {ajudante}, ja tenho {dinheiro_j}")

print(f"Consegui meu objetivo {dinheiro_j}")



# EX: Gastar dinheiro com comida
dinheiro = 100
dinheiro_comida = 5

while dinheiro > 0:
    print("To gastando com comida atoa, ainda tenho {} reais".format(dinheiro))
    dinheiro = dinheiro - dinheiro_comida

print("O dinheiro acabou, poxa {} {}".format(dinheiro, dinheiro_comida))



# EX: Contando até o valor que o usuario escolher
Contador = 0
valor = int(input('Quer contar até quanto? '))
salto = int(input('Qual seráo o valor do salto? '))

while (Contador <= valor):
    print(Contador)
    Contador = Contador + salto

print('TERMINEI A CONTAGEM')



# EX: Conversor de moedas - usuario decide quantas vezes ira converter
contt = 1
vezes_conversao = float(input("Quantas vezes vai converter?")) 

while contt <= vezes_conversao:
    reais = float(input('Quantos reias você tem?'))
    dolares = reais / 2.22
    print(f'Convertendo em dolar, você tem {dolares:.2f}US$ dolares')
    contt = contt + 1  



# EX: Contando ate 6  
def lin():
     print('_' * 30)

print("CONTAGEM INTELIGENTE")

lin()

print("Inicio = 0 ")
print("Fim = 6 ")

lin()

print("CONTANDO")

lin()

C = 0
while (C <= 6):
    print(C)
    C = C + 1



# ----------> WHILE COM ESTRUTURA CONDICIONAL <----------


# Contagem Inteligente
contInc = int(input("Digite o início da contagem: "))
contFim = int(input("Digite o final da contagem: "))

if contInc <= contFim:
    while contInc <= contFim:
        print(contInc)
        contInc += 1
else:
    while contInc >= contFim:
        print(contInc)
        contInc -= 1
print("FIM DA CONTAGEM")



# EX: Tomar banho
banho = True

while banho:
    print("To no banho")
    ja_saiu = input("ja saiu do banho?").lower()

    if ja_saiu == 'sim':
        banho = False

print("Banho finalizado!")



# EX: Somando com contador e mostrando o numero maior digitado
cont = 1
soma = 0
maior_valor = float('-inf')

while (cont <=5):
    numero = int(input("digite um numero:"))
    if numero > maior_valor:
        maior_valor = numero
    soma += numero
    cont += 1
print("A soma dos numeros é =",soma)
print("O maior valor digitado foi", maior_valor)


    
# EX: Notas de alunos com melhor aproveitamento  
lin()

print("ESCOLA SANTA PACIANCIA")

lin()

cont_ = int(input("Quantos alunos a turma tem? "))
melhor_aproveitamento = 0  # Inicializando o melhor aproveitamento com 0
nome_melhor_aproveitamento = "" # Inicializando o nome do aluno com o melhor aproveitamento como vazio

while cont_ > 0:  # Enquanto houver alunos
    nome_do_aluno = input("Nome do aluno: ")
    nota_do_aluno = float(input(f"Nota de {nome_do_aluno}: "))  # Recebendo a nota do aluno

    if nota_do_aluno > melhor_aproveitamento:
        melhor_aproveitamento = nota_do_aluno  # Atualizando o melhor aproveitamento
        nome_melhor_aproveitamento = nome_do_aluno  # Atualizando o nome do aluno com melhor aproveitamento

    cont_ =  cont_ - 1  # Decrementando o contador de alunos

if melhor_aproveitamento > 0:
     print("O melhor aproveitamento foi de", nome_melhor_aproveitamento, "com a nota", melhor_aproveitamento)
else:
    print("Você não digitou nenhuma nota")



# EX: Digitar os nomes e idades de diversas pessoas, armazenando esses dados em 2 listas.
lista_idades = []
lista_pessoas = []

nome = input("Digite um nome: ") # A primeira solicitação de input inicializa a variável nome para a verificação no while. Verifica se o nome digitado é 'fim'.
while (nome.lower() != 'fim'):   # Se não for 'fim', solicita a idade e adiciona o nome e a idade às listas.
    idade = int(input("Digite uma idade: "))
    lista_idades.append(idade)
    lista_pessoas.append(nome)
    nome = input("Digite um nome: ") # A segunda solicitação de input dentro do loop permite a atualização do valor de nome para continuar ou terminar o loop.
    
print("\n\nNomes digitados\n===============") # \n\n cria duas novas linhas (ou seja, um espaço em branco de duas 
print(lista_pessoas)
print("\nIdades\n===============") # \n é um caractere especial que representa uma nova linha.
print(lista_idades)



# EX: Digitar os nomes e idades de 5 pessoas, armazenando esses dados em 2 listas. 
lista_idades = []
lista_pessoas = []
cont = 0

while (cont < 5): # E o mesmo exemplo do outro, porém nesse eu determino o contador = 5
    nome = input("Digite um nome: ")    
    idade = int(input("Digite uma idade: "))
    lista_idades.append(idade)
    lista_pessoas.append(nome)
    cont = cont + 1 # ou cont += 1
    
print("\n\nNomes digitados\n===============")
print(lista_pessoas)
print("\nIdades\n===============")
print(lista_idades)



