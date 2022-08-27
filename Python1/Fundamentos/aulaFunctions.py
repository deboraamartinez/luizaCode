from functools import reduce

lista1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lista_somada = map(lambda x: x+x, lista1)
print(list(lista_somada))

lista2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = filter(lambda x: x % 2 == 0, lista2)
print(list(pares))


lista3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
soma = reduce(lambda x, y: x+y, lista3, 0)
print(soma)


def foo(value):
    print(f'Olá, esse é o parametros: {value}')


foo('Luiza Code')

# Parâmetros


def calcula_salario(valor, horas=220):
    return valor*horas


print(calcula_salario(35))

# *args e  **kwargs


def foo(*args):
    print(f'conteudo: {args}')

    for i in args:
        print(i)


foo('Hello', 'Moças')

# ** Kwargs - É a abreviação de keyword arguments, ele permite passar um dicionário com inúmeras chaves para a função


def foo(**kwargs):
    print(f'O nome dela(e) é: {kwargs.get("nome")}')


foo(nome='Jhon', idade='28', pais='Brasil')
