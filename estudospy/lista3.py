produtos = ['tv', 'geladeira', 'fogão', 'microondas', 'liquidificador']
estoque = [10, 5, 2, 8, 15]

produto = input('Digite o nome do produto: ').strip().lower()

print(produto)
print(produtos)

if produto in produtos:
    i = produtos.index(produto)
    print(f'A quantidade em estoque do produto {produtos[i]} é: {estoque[i]}')
else:
    print('Produto não encontrado no estoque.')