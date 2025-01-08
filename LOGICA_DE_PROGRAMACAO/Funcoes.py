import math

# =============================> FUNÇÕES <================================

"""
São blocos de código reutilizáveis que realizam uma tarefa específica.
Pense nelas como receitas de bolo: você fornece os ingredientes (os dados ou "parâmetros"), 
e a função segue o passo a passo para produzir algo.

Quando usar:
Evitar repetição: Você escreve o código uma vez e pode usá-lo várias vezes.
Organização: Seu código fica mais limpo e fácil de entender.
Facilidade de manutenção: Se precisar mudar algo, você altera só a função, e ela reflete em todo o programa.
"""

# Exemplo: Função sem parametro
def lin():
    print('_' * 30)

lin()
print('  CURSO EM VIDEO'  )
lin()
print('  APRENDA PYTHON'  )
lin()
print('  LÍDIA EDUARDA'  )
lin()


# Exemplo: Função simples que não recebe parâmetros e imprime uma mensagem
def saudacao():
    print("Olá! Bem-vindo ao mundo da programação em Python.")

saudacao()


# Exemplo: Função com parametro
def litle(my_text):
    print('_' * 30)
    print(my_text)
    print('_' * 30)

litle(' CURSO EM VÍDEO ')
litle(' PYTHON É MUITO BOM')
litle(' VAMOS ESTUDAR ')


# Exemplo: Função somando concatenação
def soma(a, b):
    print(f'A = {a} e B = {b}')
    resultado = a + b
    print(f'A SOMA A + B = {resultado} ')

soma(10,5 )
soma(b = 4, a = 2)


# # ----------> RETURN <----------

# Exemplo: Função que return uma soma
def add_two_numbers(number_one, number_two):
    total = number_one + number_two 
    return total

print(add_two_numbers(4,3))
print(add_two_numbers(15,10))


# Exemplo: Função que return exponenciação
def number_to_the_power_of(number_one, number_two):
    return number_one ** number_two 

print(number_to_the_power_of(3,3))

# Exemplo: Função que return uma soma
def sum(a, b):
     result = a + b
     print(result)
     return result
   
sum(5, 5)
sum(4, 4)
sum(3, 3)


# Exemplo: Função que return um comando de entrada
def my_frist_name(name):
    return "Seja bem vindo, " + name

entrada = input("Digite seu primeiro nome:")
print(my_frist_name(entrada)) 

# Exemplo: Função que return uma tupla
# retornar múltiplos valores separados por vírgulas, Python automaticamente cria uma tupla para esses valores.
def dividir_e_resto(dividendo, divisor): 
    quociente = dividendo // divisor
    resto = dividendo % divisor
    return quociente, resto

a, b = dividir_e_resto(10, 3) # A forma como as variáveis quociente e resto são atribuídas é chamada de "desempacotamento de tupla" (tuple unpacking).
print(a) # Estou printando separadamente o resultado - assim ele não returna uma tupla
print(b) # Estou printando separadamente o resultado - assim ele não returna uma tupla


# Exemplo: Função com return Condicional
def par_ou_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"
    
resultado = par_ou_impar(5)
print(resultado)


# Exemplo: Função com return Encerrando a Execução da Função
def verifica_numero(numero):
    if numero > 0:
        return "Positivo"
    print("Este número não é positivo.")
    return "Negativo ou Zero"

print(verifica_numero(10))  # Saída: Positivo
print(verifica_numero(-3)) 


# ----------> NONE - FUNÇÕES <----------

"""
Funções em Python retornam None por padrão se não houver
uma instrução return que especifique um valor de retorno.
"""

# Função sem instrução return nem print 
def minha_funcao():
    x = 10  # Faz algo, mas não retorna nada

resultado = minha_funcao()
print(resultado)


# Função que explicitamente retorna None
def outra_funcao():
    return None

resultado = outra_funcao()
print(resultado)


# # A função retorna None se o elemento não for encontrado na lista, indicando que a busca foi infrutífera.
# def encontrar_elemento(lista, elemento):
#     for item in lista:
#         if item == elemento:
#             return item
#     return None  # Retorna None se o elemento não for encontrado

# minha_lista = [1, 2, 3, 4, 5]
# resultado = encontrar_elemento(minha_lista, 3)

# if resultado is not None:
#     print(f"Elemento encontrado: {resultado}")
# else:
#     print("Elemento não encontrado")


# # ----------> FUNÇÕES NATIVAS <----------

# # Exemplo: Função nativa usando a bliblioteca math (matematica)
# print(math.pow(2,4))


# # Exemplo: Funções nativas para manipular string
# my_text = "Hello, Mundo. Me chamo Lídia Eduarda!" # Minha variavel (my_text), recebe o valor (Hello, mundo. Me chamo Lidia Eduarda!)
# resultado = str.upper(my_text) # Criei uma variavel chamada (resultado) onde apliquei a função (str.upper) para deixar a variavel (my_text) maiuscula.
# print(resultado)


# # ----------> NONE <----------

# """
# None é um tipo especial em Python que representa a ausência de valor ou um valor nulo. 
# None é frequentemente usado para representar a ausência de um valor ou um estado não inicializado.
# É um objeto singleton do tipo NoneType, o que significa que só existe uma instância de None em uma execução de um programa Python. 
# """

# # Comparação: Você pode comparar um valor com None usando o operador is (e não ==) para garantir que você está verificando a identidade do objeto None e não apenas a igualdade de valor
# x = None
# if x is None:
#     print("x é None")


# # Atribuição: Você pode atribuir None a variáveis para indicar que elas ainda não têm um valor útil.
# resultado = None
# print(resultado)


# # Retorno de Função: Funções em Python retornam None por padrão se não houver uma instrução return que especifique um valor de retorno.
# def minha_funcao():
#     pass

# resultado = minha_funcao()
# print(resultado) 


# # Uso em Condicionais: None é tratado como False em contextos booleanos.
# if not None:
#     print("None é considerado False")