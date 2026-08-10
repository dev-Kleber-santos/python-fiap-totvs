'''
1 --
nome = input('Digite seu nome: ')
nome = nome.strip()
nome1 = len(nome)
print(f'O {nome} tem {nome1} caracteres!')

2 --
nome = input('Digite seu nome: ').title()
print(f'Olá {nome}, seja bem-vindo(a)!')

3 -- 
telefone = input('Digite o telefone (11 dígitos): ').strip()

if len(telefone) == 11 and telefone.isdigit():
    print('Telefone válido!')
else:
    print('Erro: o telefone deve ter 11 dígitos e só números.')

4 --
senha = input('Digite sua senha: ').strip()

if len(senha) <= 2:
    senha_mascarada = senha
else:
    senha_mascarada = senha[:4] + '*' * (len(senha) - 2)

print(f'Senha exibida: {senha_mascarada}')


5 --
arq = input('Digite o nome do arquivo: ')
if arq.endswith(('.jpg', '.png')):
    print('Arquivo enviado é válido no Sistema.')
else:
    print('Arquivo inválido! O sistema aceita apenas arquivos .jpg ou .png.')

6 --
palavra = 'Abacaxi Amarelo'
print(palavra.count('a'))

7 --
nome = input('Digite seu nome: ').strip()
sobrenome = input('Digite seu sobrenome: ').strip()
nome_completo = f'{nome} {sobrenome}'
print(nome_completo)

8 --
palavra = input('Digite uma palavra: ').strip().lower()
palavra_invertida = palavra[::-1]

if palavra == palavra_invertida:
    print('A palavra é um palíndromo!')
else:
    print('A palavra não é um palíndromo.')

9 --
cnpj = input('Digite o CNPJ: ').strip()
cnpj_limpo = cnpj.replace('.', '').replace('/', '').replace('-', '')

if len(cnpj_limpo) == 14 and cnpj_limpo.isdigit():
    print('CNPJ válido!')
    print(f'CNPJ limpo: {cnpj_limpo}')
else:
    print('Erro: o CNPJ deve ter 14 dígitos e só números.')
print(f'Estou removendo traços, pontos e barras para que entre no banco de dados : {cnpj_limpo}')

10 --
email = input('Digite seu e-mail: ').strip()
if email.endswith(('@gmail.com', '@hotmail.com', '@yahoo.com')):
    print('E-mail inválido, aceitamos apenas e-mails corporativos.')
else:
    print('E-mail válido!')

11 --
email = input('Digite seu e-mail: ').strip()
usuario, dominio = email.split('@')

print(f'Usuário: {usuario}')
print(f'Domínio: {dominio}')
'''