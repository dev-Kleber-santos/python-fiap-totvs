produtos = ['tv', 'celular', 'tablet', 'notebook', 'mouse', 'teclado']
precos = [250, 1000, 450, 2000, 130, 45]

for preco in precos:
    print(f'{preco * 1.1:.2f}')

for i in range(len(precos)):
    produto = produtos[i]   
    preco = precos[i]
    print(f'O produto {produto} custa: R$ {preco}')

for i, preco in enumerate(precos):
    produto = produtos[i]
    print(f'O Preço desse {produto} é {preco}')
