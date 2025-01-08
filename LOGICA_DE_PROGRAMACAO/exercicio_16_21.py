import math
import random 

# Exercicio 16 - Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porçao inteira
# PORÇÃO INTEIRA (math.trunc)
num = float(input("Digite um numero:"))
print('O valor digite foi de {} e a sua porção inteira é {}'.format(num, math.trunc(num)))
print('O valor digite foi de {} e a sua porção inteira é {}'.format(num, int(num)))

# Exercicio 17 - Faça um programa que leia o comprimento do cateto oposto e adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa
# HEPOTENUSA (math.hypot)
c_adjacente = float(input("Comprimento do cateto oposto: "))
c_oposto =  float(input("Comprimento do cateto adjcente: "))
hipotenusa = (c_adjacente ** 2 + c_oposto ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))
# Forma importando a hipotenusa
c_adjacente = float(input("Comprimento do cateto oposto: "))
c_oposto =  float(input("Comprimento do cateto adjcente: "))
hipotenusa = math.hypot(c_adjacente, c_oposto)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))


# Exercicio 18 - Faça um programa que leia um angulo qualquer e mostre na tela o valor do Seno, Cosseno e Tangente desse angulo
# SENO (math.sin) - COSSENO (math.cos) - TANGENTE (math.tan) - RDIANOS (radiuns)
angulo = float(input("Digite o angulo que você deseja: "))
seno = math.sin(math.radians(angulo)) # O angulo estar sendo convertido para radianos  e depois converdito para seno - Pois na biblioteca de matemaica do python o seno estar em radianos
print('O angulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O angulo de {} tem TANGENTE de {:.2f}'.format(angulo, tangente))


# Exercicio 19 - Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escolhendo o nome do escolhido
# ESCOLAHA ALEATORIA (ramdon.choice)
n1 = input("Nome do 1˚ Aluno: ")
n2 = input("Nome do 2˚ Aluno: ")
n3 = input("Nome do 3˚ Aluno: ")
n4 = input("Nome do 4˚ Aluno: ")
lista = [n1, n2, n3, n4]
sorteado = random.choice(lista)
print('O aluno escolhido foi {}'.format(sorteado))


# Exercicio 20 - Um professor quer sortear a ordem de apresentacao de trablhos dos alunos. Faça um programa que leia o nome doa alunos e mostre a ordem sorteada
# ORDEM EMBARALHADA (ramdon.shuffle)
n1 = input("Nome do 1˚ Aluno: ")
n2 = input("Nome do 2˚ Aluno: ")
n3 = input("Nome do 3˚ Aluno: ")
n4 = input("Nome do 4˚ Aluno: ")
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentacao será {}'.format(lista))

# Exercicio 21 - Faça um programa em python que abra e reproduza o audio de um mp3
import pygame
pygame.init()
pygame.mixer.music.load("/Users/macbookair/Desktop/music.mp3")
pygame.mixer.music.play()
input()
pygame.event.wait()

