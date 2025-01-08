 
# Exercicio 22 - Crie um programa que leia o nome completo de uma pessoa e mostre o nome com todas as letras maiúsculas e minúsculas, quantas letras ao todo (sam considerar espaços) e quantas letras tem o primeiro nome.
nome = (input ('Digite seu Nome:')).strip()
nome_sem_espaco = nome.replace(" ", "") # Substitui todos os espaços (" ") na variavel nome por uma string vazia ("").
separa_string = nome.split() # Para usar no ultimo print
print('Analisando seu nome...')
print('Seu nome em maiúsculos é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome_sem_espaco))) # Forma usando a variavel nome_sem_espaco
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' '))) # Forma usando count para saber quantos espaços tem entre a string e mandando subtrair-los. | len(nome) - nome.count(' '): Subtrai o número de espaços em branco do total de caracteres, resultando no número de letras (caracteres que não são espaços).
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa_string[0], len(separa_string[0]))) # Usando a variavel separa_string que está dividendo a variavel nome, em seguida estou acessando o indice 0 dessa string e contando quantos letras ele tem 


#Exercicio 23 - Faça um programa que leia um numero de 0 - 9999 e mostre na tela cada um dos digitos separdos 
num = int(input('Digite um valor:'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10 
print('Unidade = {}'.format(u))
print('Decena = {}'.format(d))
print('Centena = {}'.format(c))
print('Milhar = {}'.format(m))


# Exercicio 24 - Escreva um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"
cidade = input('Em que cidade você nasceu?').strip() # .strip() - Elimina os espaços
print(cidade[:5].upper() == 'SANTO' )


# Exercicio 25 - Escreva um programa que leia o nome de uma pessoa e diga se ela tem "SILVA"
nome = input('Qual é seu nome completo:').strip()
print('Tem silva no seu nome? {}'.format('SILVA' in nome.upper())) # SILVA existe na variavel nome - o upper serve para deixar o silva em Maisculo mesmo que o usuario coloque em minusculo.


# Exercicio 26 - Faça um programa que leia uma frase pelo teclado e moste: quantas vezes a letra A aparece, Em que posição ela aparece pela primeira e ultima vez. 
frase = input('Digite uma frase:').strip().upper()
print('A letra A aparece {} vezes na frase'.format(frase.count('A'))) # Count quanto quantas vezes a letra A apareceu na variavel frase.
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1)) # Find conta qual é a posição que a letra A apareceu primeiro. +1 faz com que a posição nao inicie em 0 e sim em 1.
print('A ultima letra A apareceu na posição {}'.format(frase.rfind('A')+1)) # rFind conta qual é a posição que a letra A apareceu por ultimo. +1 faz com que a posição nao inicie em 0 e sim em 1.
 

# Exercicio 27
nome = input('Digite seu nome completo:').strip().upper()
indice_nome = nome.split() # Dividindo a frase da variavel nome
print('Prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(indice_nome[0]))
print('Seu ultimo nome é {}'.format(indice_nome[-1])) # Usando so o indice -1 
print('Seu ultimo nome é {}'.format(indice_nome[len(indice_nome)-1]))  # Usndo o len e passando a posição

# A expressão '-'.join(frase) é uma forma de combinar todos os caracteres da string frase, inserindo um traço (-) entre cada um deles.
frase = 'Curso em Video Python'
resultado = '-'.join(frase)
print(resultado)


