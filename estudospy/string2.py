faturamento = float(input('Digite o valor do faturamento: '))
custo = float(input('Digite o valor do custo: '))
lucro = faturamento - custo
print('O faturamento é: {}'.format(faturamento))
print('O custo é: {}'.format(custo))
print('O lucro é: {}'.format(lucro))
print('O lucro foi de: {:.2f}, o faturamento foi de: {:.2f}, e o custo foi de: {:.2f}'.format(lucro, faturamento, custo))