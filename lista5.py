lista = ['fone', 'casa', 'carro', 'computador', 'celular', 'tablet', 'livro', 'caneta', 'mochila', 'garrafa']
print(lista)
tamanho_lista = len(lista)
print(f'O tamanho da lista é: {tamanho_lista}')
# para adicionar um elemento no final da lista, usamos o método append e para adicionar vários elementos usamos o método extend com []
lista.extend(['chavess','carteira', 'relógio'])
print(f'O tamanho da lista após adicionar produtos é {len(lista)}')

#achando o maior número de vendas na lista de vendas
vendas = [1, 23, 45, 67, 109, 45, 23, 45, 67, 89]
maior_venda = max(vendas) # maior da lista
menor_venda = min(vendas) # menor da lista
print(maior_venda)
print(menor_venda)

i = vendas.index(maior_venda) # índice do maior valor da lista
menor = vendas.index(menor_venda) # índice do menor valor da lista
produto_mais_vendido = lista[i] # produto mais vendido
produto_menos_vendido = lista[menor] # produto menos vendido
print(f'O produto mais vendido foi  {produto_mais_vendido} e está no índice {i} e ele teve {maior_venda} vendas')
print(f'O produto menos vendido foi {produto_menos_vendido} e está no índice {menor} e ele teve {menor_venda} vendas')