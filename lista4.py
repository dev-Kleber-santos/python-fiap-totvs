lista =   ['fone', 'casa', 'carro', 'computador', 'celular', 'tablet', 'livro', 'caneta', 'mochila', 'garrafa']
lista.append('chave')

lista[0] = 'faca'
print(lista)

lista.remove('faca')
print(lista)

produto_apagado = input('Digite o produto que deseja apagar: '  )
if produto_apagado in lista:
    lista.remove(produto_apagado)
    print(f'O produto {produto_apagado} foi apagado da lista.')
    print(lista)
else:
    print(f'O produto {produto_apagado} não está na lista.')