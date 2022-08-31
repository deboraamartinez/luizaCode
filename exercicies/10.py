# Colete o nome da pessoa, a cidade de nascimento dela, e o ano em que ela nasceu. Depois você irá mostrar os dados coletados em linhas diferentes. E também, deverá informar quantos anos a pessoa terá no ano 2030.

nome = input('Qual o seu nome? ')
cidade = input('Qual sua cidade de nascimento? ')
ano_nascimento = int(input('Em que ano você nasceu? '))
idade_2030 = 2030 - ano_nascimento

print(f'Nome: {nome}')
print(f'Cidade: {cidade}')
print(f'Ano de nascimento: {ano_nascimento}')
print(f'Sua idade em 2030 será: {idade_2030}')
