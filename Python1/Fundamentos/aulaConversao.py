# Conversão Implicita
a = 15
print(f'A variável a é do tipo: {type(a)}')

b = 10.6
a = a + b
print(f'Valor da soma: {a}')

print(f'A variável a é do tipo: {type(a)}')

# Conversão Explicita

a = 1
print(type(a))
a = str(a)
print(type(a))

b = ['a', 'b', 'c', 'd']
print(type(b))
b = tuple(b)
print(type(b))
print(b)
