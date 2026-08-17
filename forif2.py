funcionarios = [
    "Ana Silva", "Bruno Costa", "Carla Mendes", "Daniel Souza", "Eduardo Lima",
    "Fernanda Rocha", "Gabriel Alves", "Helena Martins", "Igor Cardoso", "Juliana Ribeiro",
    "Lucas Fernandes", "Mariana Pinto", "Nicolas Castro", "Olivia Moreira", "Pedro Santos",
    "Quintino Ramos", "Rafael Barbosa", "Sofia Correia", "Thiago Araujo", "Vanessa Melo",
    "Wagner Farias", "Ximena Torres", "Yasmin Duarte", "Zuleica Lopes", "Beatriz Azevedo",
    "Carlos Eduardo", "Diana Freitas", "Enzo Gabriel", "Flavia Lima", "Gustavo Henrique"
]

for funcionario in funcionarios:
    print(funcionario)

for i, funcionario in enumerate(funcionarios):
    print('O nome do funcionario: {} é {}'.format(i, funcionario))


produtos = [
    "Notebook Dell Inspiron",
    "Mouse Sem Fio Logitech",
    "Teclado Mecânico RGB",
    "Monitor 24 Polegadas LG",
    "Cadeira Ergonômica de Escritório",
    "Impressora Multifuncional HP",
    "Cartucho de Tinta Preto",
    "Papel Sulfite A4 (Resma)",
    "Caneta Esferográfica Azul",
    "Bloco de Notas Adesivas (Post-it)",
    "Grampeador de Mesa",
    "Clipes de Papel Galvanizados",
    "Pasta Suspensa Kraft",
    "Armário de Aço para Arquivo",
    "Mesa de Escritório em L",
    "Calculadora Científica",
    "Projetor Multimídia Epson",
    "Cabo HDMI 2 metros",
    "Filtro de Linha 6 Tomadas",
    "Roteador Wi-Fi Gigabit",
    "HD Externo 1TB",
    "Pen Drive 64GB",
    "Headset Gamer com Microfone",
    "Webcam Full HD 1080p",
    "Suporte para Notebook",
    "Luminária de Mesa LED",
    "Frigobar 120 Litros",
    "Cafeteira Elétrica 15 Xícaras",
    "Bebedouro de Água de Mesa",
    "Extintor de Incêndio ABC"
]

produtos_estoque = [
    "Notebook", "Mouse", "Teclado", 
    "Monitor", "Cadeira", "Impressora"
]

estoque = [435, 543, 678, 787, 544, 654]
estoque_minimo = 500

for i, qtde in enumerate(estoque):
    if qtde < estoque_minimo:
            print('O produto {} está abaixo do estoque mínimo (quantidade: {})'.format(produtos_estoque[i], qtde))
'''
for produto in produtos:
    print(produto)
for i,  produto in enumerate(produtos):
    print('O Nome do produto de estoque: {} é {}'.format(i, produto))
'''
