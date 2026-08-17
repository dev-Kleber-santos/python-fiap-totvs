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

12 --
senha = input('Digite a sua senha: ')

letra = False
numero = False

for caractere in senha:
    if caractere.isalpha():
        letra = True

    if caractere.isdigit():
        numero = True

if len(senha) >= 8 and letra and numero:
    print('Senha Forte!')
else:
    print('Senha Fraca!')


13 --

frase = input('Digite uma frase: ')

vogais = 0
consoantes = 0

for letra in frase:
    if letra.isalpha():
        if letra.lower() in 'aeiou':
            vogais += 1
        else:
            consoantes += 1

print('Total de vogais:', vogais)
print('Total de consoantes:', consoantes)

14 -- 
nome = input('Digite o nome completo: ')

partes = nome.split()

primeiro_nome = partes[0]
sobrenome = partes[-1]

username = primeiro_nome[0] + sobrenome

print('Username:', username.lower())

15 --
placa = input('Digite a placa: ')

if len(placa) == 7 and placa[:3].isalpha() and placa[3:].isnumeric():
    print('Placa válida!')
else:
    print('Placa inválida!')

17 --

produtos = ['tv', 'celular', 'tablet', 'notebook', 'fone de ouvido', 'geladeira']

print('Primeiro produto:', produtos[0])
print('Último produto:', produtos[-1])


18 -- 

estoque = ['arroz', 'feijão', 'macarrão', 'óleo', 'açúcar', 'café', 'sal']

print('Quantidade de produtos:', len(estoque))


19 --

vendas_trimestre = [15400, 18700, 21300]

total = sum(vendas_trimestre)

print('Total de vendas:', total)

20 --
produtos = ['mouse', 'teclado', 'monitor']

novo_produto = input('Digite o nome do novo produto: ')

produtos.append(novo_produto)

print('Lista atualizada:', produtos)

21 --

produtos = ['tv', 'celular', 'tablet', 'notebook', 'fone de ouvido', 'geladeira']

produtos.remove('tablet')

print(produtos)

22 --

produtos = ['celular', 'câmera', 'fone de ouvido', 'monitor']

produto = input('Digite o nome do produto: ')

if produto in produtos:
    print('O produto já existe.')
else:
    print('O produto não está cadastrado.')


23 --
fila_atendimento = ['Ana', 'Bruno', 'Carla', 'Diego']

fila_atendimento.insert(1, 'Sr. João')

print(fila_atendimento)

24 --

vendas_vendedores = [15000, 8700, 23000, 4300, 19800]

vendas_vendedores.sort()

print('Menor para o maior:', vendas_vendedores)

vendas_vendedores.sort(reverse=True)

print('Maior para o menor:', vendas_vendedores)

25 --

produtos = ['computador', 'livro', 'celular', 'fone de ouvido', 'tv']

produtos_ecommerce = [
    [8000, 3000],
    [45000, 35],
    [12000, 1800],
    [9000, 250],
    [4200, 2200]
]

if 'livro' in produtos:

    indice = produtos.index('livro')

    quantidade = produtos_ecommerce[indice][0]
    preco = produtos_ecommerce[indice][1]

    imposto = preco * 0.12

    novo_preco = preco + imposto

    produtos_ecommerce[indice][1] = novo_preco

    impacto_total = imposto * quantidade

    print('Novo preço do livro:', novo_preco)
    print('Impacto financeiro total:', impacto_total)

else:
    print('Não existem livros na lista.')


26 --
meses = [
    'jan', 'fev', 'mar', 'abr', 'mai', 'jun',
    'jul', 'ago', 'set', 'out', 'nov', 'dez'
]

vendas_1sem = [22000, 26500, 19800, 15200, 17650, 21000]

vendas_2sem = [18500, 24000, 16200, 13800, 31200, 9200]

vendas = vendas_1sem + vendas_2sem

melhor_venda = max(vendas)
pior_venda = min(vendas)

indice_melhor = vendas.index(melhor_venda)
indice_pior = vendas.index(pior_venda)

melhor_mes = meses[indice_melhor]
pior_mes = meses[indice_pior]

total = sum(vendas)

percentual = (melhor_venda / total) * 100

print('O melhor mês do ano foi', melhor_mes, 'com', melhor_venda, 'vendas')

print('O pior mês do ano foi', pior_mes, 'com', pior_venda, 'vendas')

print('Faturamento total:', total)

print('O melhor mês representou', percentual, '% do total')


27 --
vendas_ano = [15000, 22000, 9800, 31000, 27000, 12000, 18500, 26000]

top3 = []

maior = max(vendas_ano)
top3.append(maior)
vendas_ano.remove(maior)

maior = max(vendas_ano)
top3.append(maior)
vendas_ano.remove(maior)

maior = max(vendas_ano)
top3.append(maior)
vendas_ano.remove(maior)

print('Top 3:', top3)



28 --

produtos = ['celular', 'câmera', 'fone de ouvido', 'monitor']

precos = [1500, 1000, 800, 2000]

produto = input('Digite o produto: ')

if produto in produtos:

    indice = produtos.index(produto)

    preco = precos[indice]

    print('O produto', produto, 'custa R$', preco)

else:
    print('Produto não encontrado. Tente novamente.')



29 --
produtos = ['celular', 'câmera', 'fone de ouvido', 'monitor']

produto = input('Digite o produto: ').lower()

if produto in produtos:
    print('Produto já existente, tente novamente')

else:
    produtos.append(produto)

    print('Produto', produto, 'cadastrado com sucesso')

    print(produtos)

30 --

vendas_vendedor_1 = [1200, 1500, 980, 2200, 1750]

vendas_vendedor_2 = [1600, 1100, 2000, 1450, 1300]

total_vendedor_1 = sum(vendas_vendedor_1)

total_vendedor_2 = sum(vendas_vendedor_2)

if total_vendedor_1 > total_vendedor_2:
    print('O vendedor 1 vendeu mais.')

else:
    print('O vendedor 2 vendeu mais.')

    
vendas = int(input('Digite a quantidade de vendas: '))

if vendas > 5000:

    bonus = vendas * 2 + 1000

elif vendas > 1000:

    bonus = vendas * 2

else:

    bonus = 0

print('Valor do bônus: R$', bonus)



produtos = ['arroz', 'feijão', 'macarrão', 'óleo', 'açúcar', 'café']

estoque = [25, 8, 40, 5, 12, 3]

produto = input('Digite o nome do produto: ').lower()

if produto in produtos:

    indice = produtos.index(produto)

    quantidade = estoque[indice]

    print('O produto', produto, 'possui', quantidade, 'unidades em estoque.')

else:

    print('Produto não encontrado.')

'''
