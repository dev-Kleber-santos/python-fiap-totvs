produtos = ['tv', 'geladeira', 'fogão', 'microondas', 'liquidificador']
precos = [1500, 2500, 1200, 800, 300]
'''
i = produtos.index('fogão')
print(i)
preco_produto = precos[i]
print('O preço do Fogão é: {}'.format(preco_produto))
'''
i = precos.index(800)
print(i)
produto_preco = produtos[i]
print('O produto que custa 800 é: {}'.format(produto_preco))