import math  

# =====================> ESTRUTURA CONDICIONAIS <==========================

"""
Estruturas condicionais em Python são usadas para executar diferentes blocos de código 
com base em certas condições. As principais estruturas condicionais são if, elif e else.

IF: A estrutura if é usada para testar uma condição.
Se a condição for verdadeira, o bloco de código dentro do if será executado.

ELIF: A estrutura elif (abreviação de "else if") é usada para testar múltiplas condições. 
Se a condição if for falsa, o Python testa a condição elif.

ELSE: A estrutura else é usada para executar um bloco de código 
quando todas as condições anteriores são falsas.

-----> try e except: Garantem que, se o usuário digitar algo que não pode ser convertido para número (como letras), o programa exibirá uma mensagem de erro amigável.
-----> .replace(",", "."): Troca a vírgula por ponto, permitindo que o Python interprete corretamente os números com decimais.

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


# EX: Ir para um show
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


# EX: O programa abaixo solicita que o usuário digite 3 lados de um suposto triângulo. Depois de receber os valores dos 3 lados, ele verifica se os 3 lados formam ou não formam um triângulo.
lado1 = float(input("Digite o 1o lado do triângulo: "))
lado2 = float(input("Digite o 2o lado do triângulo: "))
lado3 = float(input("Digite o 3o lado do triângulo: "))

if (lado1 + lado2 > lado3) and (lado2 + lado3 > lado1) and (lado3 + lado1 > lado2):
    print("Os lados {}, {} e {} formam um triângulo".format(lado1, lado2, lado3))
else:
    print("Os lados {}, {} e {} NÃO formam um triângulo".format(lado1, lado2, lado3))


# EX: O programa abaixo solicita que o usuário digite 3 lados de um suposto triângulo. Depois de receber os valores dos 3 lados, ele verifica se os 3 lados formam ou não formam um triângulo. Se os 3 lados formarem um triângulo, ele imprime que tipo de triângulo será informado.
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


# EX: Esse faz a mesma coisa do exemplo de cima,porem com o elif 
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


# EX: Aprovação de aluno 
def lin():
    print('_' * 30)

lin()

print('PYTHON')

lin()

primeira_nota = int(input('Digite a primeira nota: '))
segunda_nota = int(input('Digite a segunda nota: '))

lin()

media = (primeira_nota + segunda_nota) / 2
print(media)


if (media <= 10) and (media > 9):
    print('Aproveitamento A')
    
elif (media <= 8.90) and (media > 8):
    print('Aproveitamento B')
   
elif (media <= 7.90) and (media > 7):
    print('Aproveitamento C')

elif (media <= 6.90) and (media > 6):
   print('Aproveitamento D')

elif (media <= 5.90) and (media > 5):
    print('Aproveitamento E')
    
elif (media < 5) and (media >= 0):
    print('Aproveitamento F')

else:
    print('Nota invalida')

lin()


# EX: Partida de futbol
lin()

print('BANGU X MADUREIRA')

lin()
gols_do_madureira = int(input('Quantos gols do madureira: '))
gols_do_bangu = int(input('Quantos gols do bangu: '))

lin()

diferenca = gols_do_madureira - gols_do_bangu
print('Diferença', diferenca)
print('GOLEADA!')

lin()


# EX: Faça um programa que receba dois numeros e mostre qual deles é o maior, ou se eles sao iguais.

try: 

    num1 = float(input('Digite o primeiro valor: ').replace(",", "."))
    num2 = float(input('Digite o primeiro valor: ').replace(",", "."))


    if num1 > num2:
        print('O maior número é {}'.format(num1))
    elif num2 > num1:
        print('O maior número é {}'.format(num2))
    else:
        print("Os números são iguais.")

except ValueError:
    print('Por favor, insira valores numéricos válidos.')


# EX: Leia um numero fornecido pelo usuario. Se esse numero for positivo, calcule a raiz quadrada do numero. Se o numero for negativo, mostre uma mensagem dizendo que o numero e invalido.

try: 

    num = float((input('Digite um valor:').replace(',', '.')))

    if num > 0:
        raizq = math.sqrt(num)
        print('Sua raiz quadrada é = {}.'.format(raizq))
    else:
        print('O numero é invalido.')
except:
    print('Por favor, insira valores numéricos válidos.')


# EX: Leia um numero real. Se o numero for positivo imprima a raiz quadrada. Do contrario, imprima o numero ao quadrado.

try:
    number = float(input('Digite um valor:').replace(',','.'))

    if number > 0:
        raizq = math.sqrt(number)
        print('A raiz quadarda de {} é = {:.2f}'.format(number, raizq))
    else:
        exponenciacao = number ** 2
        print('O numero {} elevado ao quadrado é = {:.2f}'.format(number, exponenciacao))
except:
    print('Por favor, insira valores numéricos válidos.')


# EX: Faça um programa que leia um numero e, caso ele seja positivo, calcule e mostre: O numero digitado ao quadrado, e a raiz quadrada do numero digitado
try:
    num = float(input('Digite um numero: ').replace(',','.'))
    if num > 0:
        exponenciacao = num ** 2 
        raizq = math.sqrt(num)
        print ('O numero {} elevado ao quadrado é = {:.2f}'.format(num, exponenciacao))
        print('A raiz quadrada de {} é = {:.2f}'.format(num, raizq))
    else:
        print('O numero digitado é negativo')
except:
    print('Por favor, insira valores numéricos válidos.')


# EX: Faça um programa que receba um numero inteiro e verifique se este numero é par ou ımpar.

try:
    numero = int(input('Insira um numero: ').replace(',','.'))
    if numero % 2 == 0:
        print('O numero {} é par'.format(numero))
    else:
        print('O numero é impa')
except:
    print('Por favor, insira valores numéricos válidos.')


# EX: Escreva um programa que, dados dois numeros inteiros, mostre na tela o maior deles, assim como a diferenca existente entre ambos. Se por acaso, os dois numeros forem iguais, imprima a mensagem Numeros iguais.

try:
    num1 = float(input('Digite o primeiro numero: ').replace(',','.'))
    num2 = float(input('Digite o segundo numero: ').replace(',','.'))

    if num1 > num2:
        subtracao = num1 - num2 
        print('Numero {} é maior que {}, com diferença de {}'.format(num1, num2, subtracao))

    elif num2 > num1:
        sub = num2 - num1
        print('Numero {} é maior que {}, com diferença de {}'.format(num2, num1, sub))

    else: 
        print('Ambos os numeros são iguais')          
except:
    print('Por favor, insira valores numéricos válidos.')


# EX: Faca um programa que leia 2 notas de um aluno, verifique se as notas sao validas e exiba na tela a media destas notas. Uma nota valida deve ser, obrigatoriamente, um valor entre 0.0 e 10.0, onde caso a nota nao possua um valor valido, este fato deve ser informado ao usuario e o programa termina.

try:
    nota1 = float(input('Digite a nota: ').replace(',','.'))
    nota2 = float(input('Digite a nota: ').replace(',','.'))

    if nota1 and nota2 > 0.0:
        media = (nota1 + nota2) / 2
        print('A media das notas {} e {} = {}'.format(nota1, nota2, media))
    
    else: 
        print('As notas não são validas')
except:
    print('Por favor, insira valores numéricos válidos.')


# EX: Leia o salario de um trabalhador e o valor da prestacao de um emprestimo. Se a prestacao for maior que 20% do salario imprima: Emprestimo nao concedido, caso contrario imprima: Emprestimo concedido.
try: 
    salario = float(input("Digite o valor do salário do trabalhador: R$ ").replace(',','.'))
    prestacao = float(input("Digite o valor da prestação do empréstimo: R$ ").replace(',','.'))

    limite = salario * 0.2

    if prestacao > limite:
        print('Empréstimo não concedido.')
    else:
        print('Empréstimo concedido. O valor que você pagara do seu emprestimo é = {}')
except:
    print('Por favor, insira valores numéricos válidos.')


