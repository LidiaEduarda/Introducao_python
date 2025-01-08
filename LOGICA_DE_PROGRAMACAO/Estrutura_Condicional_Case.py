# =====================> USANDO CASE <=======================

# EX: Doação
valor = ''
padrao = ''
doar = input(
'''______________________
  CRIANÇA ESPERANÇA
______________________
  OBRIGADA POR DOAR  
[1] Para doar R$10
[2] Para doar R$25
[3] Para doar R$50
[4] Para doar outros valores
[5] Para cancelar ''')

match int(doar):
    case 1:
        valor = '10'
    case 2:
        valor = '25'
    case 3: 
        valor = '50'
    case 4:
        valor = input('Qual valor da doação: ')
    case 5:
        valor = '0'
    case _:
        padrao = 'Escolha umadas opçoes: 1, 2, 3, 4 ou 5'

if padrao:
    print(padrao)
else:
    print('-----------------------')
    print('Sua doação foi de R$',valor)
    print('Obrigada pela doação')



# EX: Aumento de salario
nomeF = input('Digite o nome do funcionario: ')
depedentes = int(input('Digite  numero de dependentes: '))
salario = int(input('Digite o valor do salario: '))
novo_salario = ''

match depedentes:
    case 0:
        novo_salario = salario + (salario * 5 / 100)
    case 1 | 2 | 3:
        novo_salario = salario + (salario * 10 / 100)
    case 4| 5| 6:
        novo_salario = salario + (salario * 15 / 100)
    case _:
        novo_salario = salario + (salario * 18 / 100)
print(f'O novo salario de {nomeF} será de {novo_salario}')
