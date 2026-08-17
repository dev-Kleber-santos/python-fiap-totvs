# Criando a própria função

def cadastrar_produto():
    produto = input('Digite o nome do produto a ser cadastrado: ')
    produto = produto.lower()
    print('Produto {} cadastrado com sucesso !!!'.format(produto))

cadastrar_produto()