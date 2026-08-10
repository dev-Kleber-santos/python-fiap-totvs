'''
nome = 'maria'
for i in range(1,6):
    print(f'{i} - {nome}')

tab = int(input('Digite o número da tabuada que deseja ver: '))
for i in range(1,11):
    resultado = tab * i
    print(f'A Tabuada de {tab} é -- {tab} x {i} = {resultado}')

for i in range(len(bebidas)):
    print('{} unidades vendidas de {}'.format(producao[i], bebidas[i])) 
'''
bebidas = ['agua', 'coco', 'vinho', 'refri']
producao = [100, 50, 10, 89]


for i in bebidas:
    print(i)
