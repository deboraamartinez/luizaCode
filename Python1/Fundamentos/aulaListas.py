# Listas

letters = ['a', 'b', 'c', 'd']
print(f'O nome Debora começa com a letra {letters[3]}')

lista = [0, 5, 8, 10, 35, 15, 7, 4, 12, 22, 3, 2, 9, 1]

lista_numeros_maior_10 = []
for i in lista:
    if i > 10:
        lista_numeros_maior_10.append(i)
print(f'Resultado da lista: {lista_numeros_maior_10}')
# Mesma coisa que o exemplo acima
lista_numeros_maior_10 = [i for i in lista if i > 10]
print(f'Resultado da lista: {lista_numeros_maior_10}')

# Formas de manusear Listas:

list_append = []
for i in lista:
    list_append.append(i+1)
print(f'Append: {list_append}')

list_append.extend([0, 0, 0, 0])
print(f'Extend: {list_append}')

list_append.insert(8, 'Meio da lista')
print(f'Insert: {list_append}')

list_append.remove('Meio da lista')
print(f'Remove: {list_append}')

list_append.pop(4)
print(f'Pop: {list_append}')

print(f'Index: {list_append.index(11)}')

list_append.sort()
print(f'Sort: {list_append}')

list_append.reverse()
print(f'Reverse {list_append}')

list_new = list_append.copy()
print(f'Copy: {list_new}')

# Dada uma quantidade de n números, listar somente os numeoros pares

lista = [i for i in range(10) if i % 2 == 0]
print(lista)

# Forma incorreta de utilizar
i = 0
lista = []

while i < 10:
    if i % 2 == 10:
        lista.append(1)
print(lista)
