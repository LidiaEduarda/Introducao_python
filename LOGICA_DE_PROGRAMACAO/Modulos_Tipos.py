'''
  MÓDULO: É um arquivo com extensão .py que pode ter funções, classes e variáveis.
  Ele organiza o código em partes reutilizáveis.

  math: Operações matemáticas avançadas (raiz quadrada, logaritmos, etc).
  os: Manipulação de arquivos e interação com o sistema operacional.
  random: Geração de números aleatórios e operações relacionadas à aleatoriedade.
  time: Trabalhar com tempo (pausas, medições, etc).
  json: Manipular dados no formato JSON (ler e salvar).
  sys: Acessar parâmetros e funções do sistema (como argumentos da linha de comando).
  re: Trabalhar com expressões regulares (busca e manipulação de padrões em texto).
  numpy: Operações matemáticas eficientes com arrays e matrizes.(Biblioteca)
  pandas: Manipulação e análise de dados tabulares (tabelas e planilhas). (Bibliotecas)
'''

'''                          
  FUNÇÕES MATEMÁTICAS DO MÓDULO MATH' São comandos que fazem operações mais complexas ou específicas. 

  Ângulo = 45 
  Radiano = math.radians(angulo)  
  Seno = math.sin(angulo_radiano)  
  Cosseno = math.cos(angulo_radiano)  
  Tangente = math.tan(angulo_radiano)  
  Raiz = math.sqrt(25)  
  Potência = math.pow(2, 3)
'''

import math # Está importanto todas as funções do módulo
numero = int(input("Digite um numero:"))
raizQ = math.sqrt(numero)
print('A raiz quadara de {} é = {}'.format(numero, math.ceil(raizQ)))


import random # Gerar um número aleatório inteiro em um intervalo
num = random.random()
print(num)

nume = random.randint(1, 10)
print(nume)


from math import sqrt, ceil # Está importando funções específicas do módulo math, ao invés de importar o módulo inteiro
numero = int(input("Digite um numero:"))
raizQ = sqrt(numero)
print('A raiz quadara de {} é = {}'.format(numero, ceil(raizQ)))


# EX: Diversos
valor_absoluto = abs(-50)
print(valor_absoluto) 

expo = math.exp(5.2)
print(expo)

raizQ = math.floor(math.sqrt(91))
print(raizQ)


# EX: Calculando Imposto
preco = float (input('Digite o preço do produto:'))
Imposto = math.floor(preco * 60 / 100)
print('O imposto séra de US$', Imposto)
