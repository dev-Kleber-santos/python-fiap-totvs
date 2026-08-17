vendas = [100, 1500, 300, 400, 600, 1890, 800, 256]
meta = 650

meta_batida = 0
for venda in vendas:
    if venda >= meta:
       meta_batida +=1
print(meta_batida)


qtd_funcionario = len(vendas)
print('O Percentual de funcionarios que bateram a meta foi de {:.0%}'.format(meta_batida/qtd_funcionario))
