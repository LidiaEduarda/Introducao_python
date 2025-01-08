'''
    CONVERTER AS EQUAÇOĒS MATEMATICA EM EXPRESSOĒS ARITIMÉTICAS VÁLIDAS NO PYTHON.
    USANDO OPERADORES - DIVERSOS

    Expressão aritmética: é uma combinação de números, operadores aritméticos 
    (como +, -, *, /, **, etc.) e parênteses, que resulta em um valor calculado,
    Apenas calcula um valor com operadores matemáticos (não tem um sinal de igual).
    EX: 3 * (2 + 1)

    Equação: é uma afirmação matemática que expressa a igualdade entre duas expressões. 
    Ela contém um sinal de igual (=) e indica que ambos os lados têm o mesmo valor.
    O objetivo é resolver ou encontrar o valor de uma variável.
    EX: 2x + 3 = 7
'''    

# (2+3) * 4 / por (5-6)
# Eq1. $ 2+3*4/5-6 $
eq1 = (2 + 3) * 4 / (5 - 6)
print("RESULTADO", eq1)


# Raiz quadrada de (2-3) elevado ao quadrado / por 4
# Eq2. $ \sqrt{\frac{(2-3)^{2}}{4}}$ 
eq2 = (((2-3)**2)/4) ** (1/2)
print("A RAIZ QUADRADA É", eq2)


# Cálculo da área e perímetro do retângulo
# Area é igual a base * a altura --- Perimetro é igual a 2 * (base + altura)
#$ area = base \times altura$
#$ perímetro = 2 \times (base + altura)$
base = 7
altura = 8
area = base * altura
perimetro = 2 * (base + altura)
print('A área  do retangulo é igual {} e o perimetro é igual {}.'.format(area, perimetro))


# Cálculo da área e comprimento da circunferência
# Area é igual pi * raio elevado ao quadrado --- Comprimento é igual a 2 * pi * raio
#$ area = \pi \times raio^{2} $
#$ comprimento = 2 \times \pi * raio $
raio = 2
area = 3.14159 * raio ** 2 
comprimento = 2 * 3.14159 * raio
print('Para o raio {}, a área = {} e o comprimento = {}'.format(raio, area, comprimento))


# Cálculo da distância euclidiana entre 2 pontos no plano cartesiano
# distancia é igual a raiz quadrada de (x1 - x2) elevado ao quadrado + (y1 - y2) elevado ao quadrado
# distância = \sqrt{(x_{1}-x_{2})^{2} + (y_{1}-y_{2})^{2}} 
# Calculando a distância entre os pontos (3,4) e (5,6)
x1 = 3
y1 = 4
x2 = 5
y2 = 6
distancia = ((x1-x2)**2 + (y1-y2)**2) ** (1/2)
print(f'A distancia entre ({x1}, {y1}) e ({x2}, {y2}) é = {distancia}.')


# Cálculo do delta e das raízes de uma equação do segundo grau
# Delta é igual b elevado ao quadrado menos 4 *a*c --- X é igual -b +_ raiz quadrada de delta / por 2*a (sob 2a)
#$ \Delta = b^{2} - 4ac $
#$ x = \frac{-b \pm \sqrt{\Delta}}{2a} $
# Calculando o Delta e raízes x1 e x2 para a equação y = x^2 - 5x + 6
a = 1
b = -5
c = 6
delta = b**2 - 4*a*c
x_mais = (-b+delta**(1/2))/2*a
x_menos = (-b-delta**(1/2))/2*a
print(f'Delta é = {delta}, X_mais é = {x_mais} e X_menos é = {x_menos}')



# Cálculo da área do setor circular (fatia de um círculo)
# S é gual a alfa * pi * r elevado ao quadrado / por 360
#$ S = \frac{\alpha \pi r^{2}}{360} $
# Para um círculo de raio 15, calcular a área de uma fatia com angulo = 45 graus (um pizza)
# Isso equivale a calcular a área de uma das 8 fatias de uma pizza com 30 cm de diâmetro
a = 45
r = 15
s = (a * 3.14159 * r **2)/360
print('Num círculo de raio {}cm, o setor circular de ângulo {} terá área = {} cm^2.'.format(r,a,s))


# EX: Estou usando operandores relacionais para retornar um resultado logico  
A = 5
B = 7
C = 2
print(A < B, B == C, A > 10, C > A + B,)
D = 10
E = 5
print(not (D>E) and (E<D), not(D == E) or (E == D))


# EX: Usando operadores logicos para saber se meu codigo forma um triangulo (para ser um triangulo cada lado tem que ser sempre menor que a soma dos outros dois lados)o triangulo é equelatero (todos os lados iguais) ou escaleno (lados diferentes)
L1 = int(input("Digite o priemiro lado:"))
L2 = int(input("Digite o segundo lado:"))
L3 = int(input("Digite o terceiro lado:"))
Triangulo = (L1 < (L2 + L3)) and (L2 < (L1 + L3)) and (L3 < (L1 + L2))
Equelatero = (L1 == L2) and (L2 == L3)
Escaleno = (L1 != L2) and (L2 != L3) and (L1 != L3)
print("Pode formar um TRI?", Triangulo)
print("O triangulo é EQ?", Equelatero)
print("O triangulo é ES?", Escaleno)


# EX: Convertendo reais para dolares
reais = float(input('Quantos reias você tem?'))
dolares = reais / 2.22
print(f'Convertendo em dolar, você tem {dolares}US$ dolares')


# EX: Convertendo temperatura 
TempF = int(input('Digite a temperatura:'))
TempC = (TempF - 32) / 1.8
print('A temparatura em grausC é de', TempC) 


# EX: O usuario digitou dois numeros e eu realizei a soma deles e no final dividi por 2
numero_1 = input("Digite um numero:")
numero_2 = input("Digite um numero:")
soma = int(numero_1) + int(numero_2)
resultado = soma / 2
print(f"A media entre {numero_1} e {numero_2} é = " , resultado)

# EX: Qual é a minha idade
ano_atual = int(input('Em que ano estamos?'))
ano_de_nascimento = int(input('Em que ano você nasceu?'))
sua_idade = ano_atual - ano_de_nascimento
print(f" Você tem {sua_idade} anos de idade")