from random import randint # randint: gera um número inteiro aleatório entre a e b (inclusive).
from time import sleep # sleep(seconds): faz o programa "dormir" ou pausar por um número específico de segundos.

# Exercicio 28 - Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 a 5 a peça para o usuário tentar descobrir qual foi número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
computador = randint(0, 5) # Faz o computador sortear 1 numero entre 0-5
print('-=-' * 20)
print('Vou pensar em um numero entre 0-5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número está pensei? ')) # jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS!' 'Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))


# Exercicio 29 - Escreva um programa que leia a velocidade de um carro. Se ela ultrapassar 80Km/h, mostra uma mensagem dizendo que ele foi multado. A multa vai custar R$7.00 por cada Km acima do limite.
velocidade = float(input('Qual é a sua velocidade? '))
if velocidade > 80:
    print('MULTADO! Você execedeu o limite de velocidade que é de 80km/h')
    multa = (velocidade - 80) * 7
    print('Sua multa foi de {:.2f}R$'.format(multa))
print('Tenha um Bom dia! Dirija com segurança!')