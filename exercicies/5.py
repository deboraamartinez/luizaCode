# Calcule a área de um quadrado cujo lado seja 2 cm.
lado = 2
area = lado * lado
print(area)

# Uma mala custa R$120,00. Esta recebeu 5% de desconto. Quanto você irá pagar por ela.

mala = 120
valor_desconto = mala * 0.05
valor_mala = mala - valor_desconto
print(f'O valor do desconto é ${valor_desconto} e a mala custa ${valor_mala}')

# Um carro está viajando a uma velocidade média de 100 Km/h, o trecho de viagem será 200 Km. Quantas horas irá demorar a viagem.

velocidade_media = 100
deslocamento = 200
tempo = deslocamento / velocidade_media
print(f'A viagem vai demorar {tempo} horas')

# João tem 2 pirulitos, Maria 3 pirulitos e Sofia 1 pirulito. Calcule o total de pirulitos e sua média.

joao = 2
maria = 3
sofia = 1

total = joao + maria + sofia
media = total/3

print(f'O valor total de pirulitos é {total} e a média é {media}')

# Davi tem 13 anos e sua irmã tem 7 anos. Guarde na variável eh_mais_velho a verificação se a idade de Davi é maior que a idade de sua irmã.

davi = 13
irma = 7
if davi > irma:
    print('Davi é mais velho')
