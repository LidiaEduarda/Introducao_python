# end='' ----> Você está dizendo ao Python para permitir que a próxima chamada de print() continue na mesma linha.
# :.<30 ----> 
# : |Este indica a forma como o valor deve ser formatado.
# . |Este é o caractere de preenchimento. Isso significa que, se a string for mais curta que 30 caracteres, os pontos serão adicionados à direita da string até que o comprimento total seja 30 caracteres.
# < |Este é o especificador de alinhamento. Indica que o texto deve ser alinhado à esquerda. Se o caractere de preenchimento não fosse especificado, o espaço em branco seria usado como padrão.
# 30 |Este é o comprimento total do campo. Significa que a string formatada terá exatamente 30 caracteres de comprimento.
# .2f --->
# . |Este indica que queremos um número de ponto flutuante.
# 2 |Este especifica o número de casas decimais a serem exibidas.
# f |Este significa que estamos formatando um número de ponto flutuante.
# float('-inf') ----> Representa o valor de "menos infinito" em Python. Ele é usado para garantir que qualquer número que você comparar com ele será maior.
# ^ ---> Serve para centralizar o texto.
# \n ---> Cria uma nova linha 



# O Python fornece o método type() que retorna o tipo de dados e variáveis. Seu uso é muito simples, basta colocar um objeto, o nome de uma variável ou um valor entre parênteses. 
print(type('LIDIA'))
print(type(1.7))
print(type(2))


# Python fornece o método isinstance() que permite verificar se um objeto ou variável (primeiro parâmetro da função) é uma instância de uma classe ou é de um determinado tipo.
print(isinstance('Lidia, 10', str))
print(isinstance(5, str))
print(isinstance(1.7, float))


# A forma mais utilizada na versão 3 do Python, entretanto, é usar o método format.
nome = "LIDIA EDUARDA"
idade = 25
print('Meu nome é {}, e tenho {} anos de idade.'.format(nome, idade))


# Como controlar o input? Digo a pessoa pode digitar 1 vírgula 62,0 ou 1 ponto 62,0 Qual a forma mais prática de evitar erros no programa?
peso = input("Digite seu peso: ")
peso = float(peso.replace(',', '.'))
altura = input("Digite sua altura: ")
altura = float(altura.replace(',', '.')) 
print(altura, peso)