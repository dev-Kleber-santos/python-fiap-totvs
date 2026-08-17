vendas = (
    ('Jõao', 15000),
    ('Kleber', 50000),
    ('Julia', 10000),
    ('Fernando', 8000),
    ('Deborah', 9000),
    ('Jorge', 5000)
)

meta_venda = 10000

for item in vendas:
    if item[1] >= meta_venda:
        print('O vendedor {} Bateu a Meta !!! fez: {} vendas'.format(item[0], item[1]))