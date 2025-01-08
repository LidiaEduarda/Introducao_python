#suffix: A sequência que você quer verificar se está no final da string.
#start: (opcional) A posição inicial onde começar a procurar a sequência.
#end: (opcional) A posição final onde parar a procura pela sequência.

# Exercicio 05 - Faça um programa que leia um numero inteiro e mostre na tela  seu sucessor e o seu antecessor.
numero = int(input("Digite um numero:"))
antecessor = numero - 1
sucessor = numero + 1
print('Analisando o valor {}, seu antecessor é {} e seu sucessor é {}'.format (numero, antecessor, sucessor))


# Exercicio 06 - Crie m algoritimo que leia um numero e mostre o seu dubro, tripo e raiz quadrada.
numero = int(input("Digite um valor:")) 
n_dobro = numero * 2
n_triplo = numero * 3
n_sqrt = numero ** (1/2)
print('O dobro de {} é {}'.format(numero, (numero*2)))
print('O triplo de {} é {}'.format(numero, numero*3))
print('A raiz quadrada de {} é {:.2f}'.format(numero, (numero**(1/2))))
print(' O dobro de {} é {}. \n O triplo de {} é {}. \n E a raiz quadrada de {} é {:.2f}'.format(numero, n_dobro, numero, n_triplo, numero, n_sqrt ))


# Exercicio 07 - Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média
nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
media = (nota1 + nota2) / 2
print('A media entre as notas {} e {} é = {}'.format(nota1, nota2, media))


# Exercicio 08 - Escreva um programa que leia um valor em metros e convertar ele para centrimetros e milimetros.
valor_metros = float(input("Digite uma distancia em metros:"))
cm = valor_metros * 100
mm = valor_metros * 1000
print('A distancia em metros de {} corresponde a {:.0f}cm e {:.0f}mm'. format(valor_metros, cm, mm))


# Exercicio 09 - Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
numero = int(input("Digite um numero e veja sua tabuada:"))
print('{} * {} = {}'. format(numero, 1, numero*1))
print('{} * {} = {}'. format(numero, 2, numero*2))
print('{} * {} = {}'. format(numero, 3, numero*3))
print('{} * {} = {}'. format(numero, 4, numero*4))
print('{} * {} = {}'. format(numero, 5, numero*5))


# Exercicio 10 - Crei um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar
dinheiro = float(input("Quantos reias você tem? R$"))
conversor_dolar = dinheiro / 3.27
print('Com R${:.2f} você compraria US${:.2f}'.format(dinheiro, conversor_dolar))


# Exercicio 11
largura = float(input("Digite a largura da parede:"))
altura = float(input("Digite a altura da parede:"))
area = largura * altura
quant_tinta = area / 2
print('Uma parede com {} de largura e {} de altura, resulta em uma area de {}m2'.format(largura, altura, area))
print('Logo,você irá precisar de {}l de tinta para pintar essa parede.'.format(quant_tinta))

# Exercicio 12 - Faça um algoritimo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
preco_produto = float(input("Digite o valor do produto: R$"))
desconto = preco_produto - (preco_produto * 5 / 100)
print('O produto que custava R${:.2f} na promoção, com desconto de 5% vai custar R${:.2f}'.format(preco_produto, desconto))  


# Exercicio 13 - Faça um algoritimo qie leia o salario de um funcionario e mostre seu novo salario com 15% de aumento
salario = float(input("Digite o valor do salario: R$"))
novo_salario = salario + (15 / 100 * 1000) # salario + (salario * 15 / 100)
print('O novo salario com aumento de 15% é igual a R${:.2f}'.format(novo_salario))


# Exercicio 14 - Escreva um programa que converte uma temperatura digitada em ˚c para ˚f
c = float(input("Valor em graus˚C: "))
f = c * 9 / 5 + 32
print('A temperatura de {:.2f} ˚C em fahrenheit é {:.2f} ˚F'.format(c, f))


# Exercicio 15
km_percorrido = float(input("Digite o valor percorrido em KM:"))
dias_aluguel = int(input("Digite os dias de aluguel:"))
preco_pagar = (km_percorrido * 0.15) + (dias_aluguel * 60)
print('O total a pagar é de {:.2f}R$'.format(preco_pagar))