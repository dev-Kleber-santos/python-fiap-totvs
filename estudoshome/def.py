import psycopg2
"""
def porta_magica(palavra):
    if palavra =='Abracadabra':
        return 'A porta abriu! Plin'
    else:
        return 'Palavra errada ! A porta continua Fechada!'
resultado = porta_magica("Abracadabra")
print(resultado)

def verificar_idade(idade):
    if idade >= 10:
        return 'Voce pode entra!'
    else:
        return 'Voce nao pode entrar!'
resultado = verificar_idade(10)
print(resultado)

#Função que avalia se o item é um doce ou não
def avaliar_comida(item):
    if item == 'chocolate' or item == 'Pirulito':
        return 'É um doce gostoso!'
    else:
        return 'Não é um doce!'
resultado = avaliar_comida('maça')
print(resultado)

def avaliar_comida(lanche):
    if lanche == 'carne':
        return 'É uma comida gostosa!'
    else:
        return 'Não é uma comida gostosa!'

comidas = ['carne', 'maçã', 'banana', 'chocolate', 'arroz']
for lanche in comidas:
    mensagem = avaliar_comida(lanche)
    print('O T-Rex pegou:', lanche, '->', mensagem)


def academia(treino):
    if (
        treino == "Biceps"
        or treino == "Triceps"
        or treino == "Perna"
        or treino == "Ombro"
        or treino == 'Costas'
    ):
        return 'Muito bem Aluno !!'
    elif (
        treino != 'Biceps'
        or treino != "Triceps"
        or treino != "Perna"
        or treino != "Ombro"
        or treino != 'Costas'

    ):
        return 'Treino não encontrado'
    else:
        return 'Voce não treinou hoje'

treino_escolhido = input("Qual Músculo voce treinou hoje: ").capitalize()
mensagem = academia(treino_escolhido)
print('O Aluno Treinou', treino_escolhido, 'hoje', mensagem)

telefone_magico = psycopg2.connect(
    dbname='castelo_de_jogos',
    user='rei_kleber',
    password='senha_correta',
    host='nuvem_magica'
)

def remedio(beber):
    if (
        beber == 'Ibuprofeno'
        or beber == 'Dipirona' 
        or beber == 'Parecetamol'
    ):
        return 'Voce tomou a dose do dia!'
    elif (
        beber != 'Ibuprofeno'
        or beber != 'Dipirona'
        or beber != 'Parecetamol'
    ):
        return 'Voce não tomou o remedio correto'
    else:
        return 'Voce nao tomou nenhum remedio'
remedio_escolhido = input('Qual foi o Rémedio que voce tomou ? ').capitalize()
mensagem = remedio(remedio_escolhido)
print(f'O Paciente tomou,', remedio_escolhido,mensagem)
"""
