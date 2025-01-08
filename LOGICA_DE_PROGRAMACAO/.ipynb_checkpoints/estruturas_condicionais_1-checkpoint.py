import math  

# ----------> ESTRUTURA CONDICIONAIS <----------

"""
Estruturas condicionais em Python são usadas para executar diferentes blocos de código 
com base em certas condições. As principais estruturas condicionais são if, elif e else.
"""

# ----------> IF <----------
"""
A estrutura if é usada para testar uma condição.
Se a condição for verdadeira, o bloco de código dentro do if será executado.
"""

# ----------> ELIF <----------
"""
A estrutura elif (abreviação de "else if") é usada para testar múltiplas condições. 
Se a condição if for falsa, o Python testa a condição elif.
"""

# ----------> ELSE <----------
"""
A estrutura else é usada para executar um bloco de código 
quando todas as condições anteriores são falsas.
"""


# EX: Maior de idade
ano_atual = int(input('Em que ano estamos?'))
ano_nascimento = int(input('Em que ano você nasceu?'))
sua_idade = ano_atual - ano_nascimento
print(f'Você tem {sua_idade} anos de idade')

if sua_idade >= 18:
    print('Você já é maior de idade')
else:
    print('Você não é maior de idade')


#EX: Ir para um show
dinheiro = input('Você tem dolares?')
resposta = dinheiro.lower() == 'sim'

if resposta:
    print('Vamos para o show')
else: 
   print('Estou chateada')
    

# EX: Par/Impar
num = float(input('Digite um numero:'))
if num % 2 == 0:
    print(f'O numero {num} é par')
else: 
    print(f'O numero {num} é impa')


# EX: Massa Corporal - IMC
massa = float(input('Digite seu peso:'))
altura = float(input('Digite sua altura:'))
imc = math.floor(massa / (altura * altura))
print(f'Seu peso é = {imc:.2f}')

if (imc >= 18.5) and (imc < 25):
    print('Parabens! Você está no seu peso ideal')
else:
    print('Você não está na faixa de peso ideal') 


# EX: Tirar carteira
def lin():
    print('_' * 30)

lin ()
print("DEPARTAMENTO DE TRANSITO ". center(30))
lin()

Ano_atual = int(input('Digite em que ano estamos:'))
Ano_nascimento = int(input('Digite o ano que você nasceu:'))

lin()
print(' STATUS ')

Sua_idade = Ano_atual - Ano_nascimento
print('Idade:', Sua_idade)

if Sua_idade >= 18:
    print('Apto a tirar CNH')
else:
    print('Não apto a tirar CNH')
lin()
print()

# EX: Aprovado ou reprovado
lin()
print('ESCOLA PTYHON')
lin()

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

lin()

media = (nota1 + nota2) / 2
print('Nota =', media) # Aredondar 2 casas deciamis depois da virgula

if media >= 7:
    print('Aprovado')
else:
    print('Reprovado')

lin()


# ----------> ESTRUTURA CONDICIONAL ANINHADA <----------

# EX: Aprovado, Recuperação, Rep
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
nota_final = (n1 + n2) / 2
print(nota_final)

if nota_final >= 7:
    print('APROVADO')
elif (nota_final < 7) and (nota_final >3):
    print('RECUPERAÇÃO')
else: 
    print('REPROVADO')


# Como controlar o input? Digo a pessoa pode digitar 1 vírgula 62,0 ou 1 ponto 62,0 Qual a forma mais prática de evitar erros no programa?
peso = input("Digite seu peso: ")
peso = float(peso.replace(',', '.'))
altura = input("Digite sua altura: ")
altura = float(altura.replace(',', '.')) 
print(altura, peso)


# O programa abaixo solicita que o usuário digite 3 lados de um suposto triângulo. Depois de receber os valores dos 3 lados, ele verifica se os 3 lados formam ou não formam um triângulo.
lado1 = float(input("Digite o 1o lado do triângulo: "))
lado2 = float(input("Digite o 2o lado do triângulo: "))
lado3 = float(input("Digite o 3o lado do triângulo: "))

if (lado1 + lado2 > lado3) and (lado2 + lado3 > lado1) and (lado3 + lado1 > lado2):
    print("Os lados {}, {} e {} formam um triângulo".format(lado1, lado2, lado3))
else:
    print("Os lados {}, {} e {} NÃO formam um triângulo".format(lado1, lado2, lado3))


# O programa abaixo solicita que o usuário digite 3 lados de um suposto triângulo. Depois de receber os valores dos 3 lados, ele verifica se os 3 lados formam ou não formam um triângulo. Se os 3 lados formarem um triângulo, ele imprime que tipo de triângulo será informado.
lado1 = float(input("Digite o 1o lado do triângulo: "))
lado2 = float(input("Digite o 2o lado do triângulo: "))
lado3 = float(input("Digite o 3o lado do triângulo: "))

if (lado1 + lado2 > lado3) and (lado2 + lado3 > lado1) and (lado3 + lado1 > lado2):
    if (lado1 == lado2) and (lado2 == lado3): # também poderia usar if a==b==c:
        print("Os lados {}, {} e {} formam um triângulo equilátero.".format(lado1, lado2, lado3))
    else:
        if (lado1 == lado2) or (lado2 == lado3) or (lado3 == lado1):
            print("Os lados {}, {} e {} formam um triângulo isóceles.".format(lado1, lado2, lado3))
        else:
            print("Os lados {}, {} e {} formam um triângulo escaleno.".format(lado1, lado2, lado3))
else:
    print("Os lados {}, {} e {} NÃO formam um triângulo".format(lado1, lado2, lado3))


# Esse faz a mesma coisa do exemplo de cima,porem com o elif 
lado1 = float(input("Digite o 1o lado do triângulo: "))
lado2 = float(input("Digite o 2o lado do triângulo: "))
lado3 = float(input("Digite o 3o lado do triângulo: "))

if (lado1 + lado2 > lado3) and (lado2 + lado3 > lado1) and (lado3 + lado1 > lado2):
    if (lado1 == lado2) and (lado2 == lado3): # também poderia usar if a==b==c:
        print("Os lados {}, {} e {} formam um triângulo equilátero.".format(lado1, lado2, lado3))
    elif (lado1 == lado2) or (lado2 == lado3) or (lado3 == lado1):
        print("Os lados {}, {} e {} formam um triângulo isóceles.".format(lado1, lado2, lado3))
    else:
        print("Os lados {}, {} e {} formam um triângulo escaleno.".format(lado1, lado2, lado3))
else:
    print("Os lados {}, {} e {} NÃO formam um triângulo".format(lado1, lado2, lado3))