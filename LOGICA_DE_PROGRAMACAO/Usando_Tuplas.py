# -------------------------------------- TUPLAS-------------------------------------------------

'''
Definição: Uma tupla é uma coleção imutável (não pode ser alterada).
Sintaxe: Usam parênteses ( ).
Características: -> Após criada, seus valores não podem ser alterados.
                 ->Também podem conter diferentes tipos de dados.
                 ->Mais rápidas e ocupam menos memória que listas.
                 ->Ideais para dados constantes.

Quando usar tuplas? -> Quando os dados não devem ser modificados.
                    -> Para garantir a integridade de informações.
                    -> Em situações onde o desempenho é importante (tuplas são mais rápidas que listas).
              
'''

tupla_produtos = ('Caderno', 24.99,
                  'Canetas', 5.90,
                  'Lapis', 3,
                  'Corretivo', 2.50,
                  'Borracha', 1.50,
                  'Bolsa', 75.94)
print('_' * 40)
print('LISTAGEM DE PREÇOS'.center(40)) #print(f'{"LISTAGEM DE PREÇOS":^40}')                
print('_' * 40)
for posicao in range(0, len(tupla_produtos)):  
    if posicao % 2 == 0:
        print(f'{tupla_produtos[posicao]:.<30}', end='') 
    else:
        print(f'R${tupla_produtos[posicao]:>7.2f}')
print('_' * 40)



