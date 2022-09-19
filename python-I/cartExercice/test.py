def add_item_cart(item, cart):
    cart.append(item)
    return cart


def execute():
    cart = []
    id_user = input('Insira o id do usuário: ')
    id_product = input('Insira o id do produto: ')
    price_product = input('Insira o valor do produto: ')
    quantity_product = input('Insira a quantidade de produto: ')
    item = [id_user, id_product, price_product, quantity_product]
    cart = add_item_cart(item, cart)
    print(f'O seu carrinho é: {cart}')


execute()
execute()
