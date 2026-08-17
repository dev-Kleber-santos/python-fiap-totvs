'''
1 --
lista = [1200, 950, 1800, 700, 1330, 990, 1450]

soma = (sum(lista))+(len(lista))
print(soma)

2-- 
n = int(input('digite um número: '))
for i in range(1,11):
 tabuada = n * i
 print(f'A tabuada do {n} x {i } é :{tabuada}')

3 --
numeros = [1, 2, 3, 4, 5, 6, 3, 5, 8, 10, 14, 12, 21, 18]

total_pares = sum(1 for n in numeros if n % 2 == 0)
print(total_pares)

4 --
alunos = ['Beatriz', 'Caio', 'Diego', 'Eliza', 'Fernanda', 'Gustavo']

for i, aluno in enumerate(alunos, start=1):
    print(f'A Lista dos Alunos é {i} {aluno}')
     '''
produtos = ['tv', 'celular', 'tablet', 'notebook', 'mouse', 'teclado']
precos = [2500, 1800, 950, 3200, 80, 120]

desconto = 0.90

for produto, preco in zip(produtos, precos):
    if preco > 1000:
        preco_final = preco * desconto
    else:
        preco_final = preco
    print(f'Produto: {produto} | Preço: R$ {preco_final:.2f}')