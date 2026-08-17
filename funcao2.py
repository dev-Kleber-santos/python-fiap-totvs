import statistics

vendas = [350, 50, 100, 500, 30, 3, 3, 3, 3, 4, 4, 4, 2, 2, 2]

media_vendas = (sum(vendas)/len(vendas))
print(media_vendas)

mediana = statistics.median(vendas)
print(mediana)


moda = statistics.mode(vendas)
print(moda)
