'''
    OPERADORES EM PYTHON SÃO SÍMBOLOS USADOS PARA REALIZAR OPERAÇÕES EM VALORES OU VARIÁVEIS. 
    ELES PODEM SER CLASSIFICADOS EM VÁRIAS CATEGORIAS:
'''
#------------------------------------------------------------------------------------------------------#
'''
    OPERADORES ARITÍMETICOS: São utilizados para criarmos expressões matemáticas comuns:

Operador	   Nome	                        Função
    +	    Adição	            Realiza a soma de ambos operandos.
    -	    Subtração	        Realiza a subtração de ambos operandos.
    *	    Multiplicação	    Realiza a multiplicação de ambos operandos.
    /	    Divisão	            Realiza a Divisão de ambos operandos.
    //	    Divisão inteira	    Realiza a divisão entre operandos e a parte decimal de ambos operandos.
    %	    Módulo	            Retorna o resto da divisão de ambos operandos.
    **	    Exponenciação	    Retorna o resultado da elevação da potência pelo outro.
'''
quatro = 4
dois = 2

soma = quatro + dois
print(soma)  # Resultado: 6

subtracao = quatro - dois
print(subtracao)  # Resultado: 2

multiplicacao = quatro * dois
print(multiplicacao)  # Resultado: 8

divisao = quatro / dois
print(divisao)  # Resultado: 2.0

divisao_interna = quatro // dois
print(divisao_interna)  # Resultado: 2

modulo = quatro % dois
print(modulo)  # Resultado: 0

exponenciacao = quatro ** dois
print(exponenciacao)  # Resultado: 16

#------------------------------------------------------------------------------------------------#
'''
    OPERADORES DE COMPARAÇÃO OU RELACIONAIS: São usados para comparar dois valores:

Operador	            Nome	                                 Função
    ==	            Igual a	                    Verifica se um valor é igual ao outro
    !=	            Diferente de	            Verifica se um valor é diferente ao outro
    >	            Maior que	                Verifica se um valor é maior que outro
    >=	            Maior ou igual	            Verifica se um valor é maior ou igual ao outro
    <	            Menor que	                Verifica se um valor é menor que outro
    <=	            Menor ou igual	            Verifica se um valor é menor ou igual ao outro
'''
var = 5

if var == 5:
    print('Os valores são iguais') # Os valores são iguais

if var != 7:
    print('O valor não é igual a 7') # O valor não é igual a 5

if var > 2:
    print('O valor da variável é maior de 2') # O valor da variável é maior de 5

if var >= 5:
    print('O valor da variável é maior ou igual a 5') # O valor da variável é maior ou igual a 5

if var < 7:
    print('O valor da variável é menor que 7') # O valor da variável é menor que 7

if var <= 5:
    print('O valor da variável é menor ou igual a 5') # O valor da variável é menor ou igual a 5

#------------------------------------------------------------------------------------------------------------------------------------------#
'''
    OPERADORES DE ATRIBUICÃO: São utilizados no momento da atribuição de valores à variáveis e controlam como a atribuição será realizada.

Operador	     Equivalente a
    =	            x = 1
    +=	            x = x + 1
    -=	            x = x - 1
    *=	            x = x * 1
    /=	            x = x / 1
    %=	            x = x % 1
'''
# Operador +=:
numero = 5
numero += 7
print(numero)  # Resultado será 12

# Operador -=:
numero = 5
numero -= 3
print(numero)  # Resultado será 2

# Operador *=:
numero = 5
numero *= 2
print(numero)  # Resultado será 10

# Operador /=:
numero = 5
numero /= 4
print(numero)  # Resultado será 1.25

# Operador %=:
numero = 5
numero %= 2
print(numero)  # Resultado será 1

#----------------------------------------------------------------------------------------------------------------------#
'''
OPERADORS LOGICOS: Possibilitam construir um tipo de teste muito útil e muito utilizado em qualquer programa Python: 

Operador	                            Definição
    and	                Retorna True se ambas as afirmações forem verdadeiras
    or	                Retorna True se uma das afirmações for verdadeira
    not	                Retorna Falso se o resultado for verdadeiro
'''
num1 = 7
num2 = 4

# Exemplo and
if num1 > 3 and num2 < 8:
    print("As Duas condições são verdadeiras")

# Exemplo or
if num1 > 4 or num2 <= 8:
    print("Uma ou duas das condições são verdadeiras")

# Exemplo not
if not (num1 < 30 and num2 < 8):
    print('Inverte o resultado da condição entre os parânteses')

#--------------------------------------------------------------------------------------------------------------------------------------------------#
'''
OPERADORES DE IDENTIDADE: São utilizados para comparar objetos, verificando se os objetos testados referenciam o mesmo objeto (is) ou não (is not).

Operador	                                    Definição
    is	                    Retorna True se ambas as variáveis são o mesmo objeto
    is not	                Retorna True se ambas as variáveis não forem o mesmo objeto
'''
# Operador is:
lista = [1, 2, 3]
outra_lista = [1, 2, 3]
recebe_lista = lista
print(f"São o mesmo objeto? {lista is recebe_lista}") # São o mesmo objeto? True ------- # Recebe True, pois são o mesmo objeto. 
print(f"São o mesmo objeto? {lista is outra_lista}") # São o mesmo objeto? False ------- # Retorna False, pois são objetos diferentes.

# Operador is not:
tupla = (1, 2, 3)
outra_tupla = (1, 2, 3)
print(f"Os objetos são diferentes? {outra_tupla is tupla}") # Os objetos são diferentes? True

#-----------------------------------------------------------------------------------------------------------------------#
'''
OPERADORES DE ASSOCIAÇÃO: verificar se determinado objeto está associado ou pertence a determinada estrutura de dados.

Operador	                             Função
    in	           Retorna True caso o valor seja encontrado na sequência
    not in	       Retorna True caso o valor não seja encontrado na sequência
'''
lista = ["Python", 'Academy', "Operadores", 'Condições']
print('Python' in lista)  # Saída: True ---- # Verifica se existe a string dentro da lista
print('SQL' not in lista) # Saída: True ---- # Verifica se não existe a string dentro da lista
