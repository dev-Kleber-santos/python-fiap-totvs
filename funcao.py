vendas = [1500, 900, 6500, 4000, 1000, 450, 340]
dias = ['Segunda-Feira', 'Terça-Feira', 'Quarta-Feira', 'Quinta-Feira', 'Sexta-Feira', 'Sabado', 'Domingo']
'''
usuario_correto = 'kleber'
senha_correta = '12345'
id_digitado = input('Digite o seu id: ')
senha_digitada = input('Digite a sua senha: ')

def acesso(user, senha):
    if user == usuario_correto and senha == senha_correta:
        return 'Correto logou com sucesso'
    else:
        return 'Erro de login'
resultado = acesso(id_digitado, senha_digitada)
print(resultado)
'''


