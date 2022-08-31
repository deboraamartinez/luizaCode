# Este programa irá calcular a área de um triângulo. Peça para a pessoa informar a medida numérica da base do triângulo, depois colete o valor da altura. Apresente o valor da área do triângulo.

base = int(input('Informe o valor da base do triângulo: '))
altura = int(input('Informe o valor da altura do triângulo: '))


triangulo = (base * altura) / 2

print(f'A área do triângulo é: {triangulo}')
