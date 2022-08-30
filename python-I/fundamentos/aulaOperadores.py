semana = False
feriado = True
nome = 'Debora'


print(type(semana))
print(type(feriado))

print('Meu nome é', nome)

soma = 4+2
print(soma)

subtracao = 4-2
print(subtracao)

multplicacao = 2*2
print(multplicacao)

divisao = 2/2
print(divisao)

# Operadores

variavel = 5

if variavel == 5:
    print('Tudo igual')
if variavel != 7:
    print('O valor não é igual a 7')
if variavel > 2:
    print('O valor é maior que 2')

# operadores lógicos

num1 = 7
num2 = 4

if num1 > 3 and num2 < 8:
    print('Ambas condições são verdadeiras')
if num1 > 4 or num2 <= 8:
    print('Uma das condições é verdadeira')
if not (num1 < 30 and num2 < 8):
    print('Inverte o resultado da condição entre os parâmetros')
