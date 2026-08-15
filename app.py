#Importando nosso resturante.py para um app
from modelos.restaurante import Restaurante


restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_EUA = Restaurante('Lolys Buruger', 'Burguer')
restaurante_japones = Restaurante('Japa', 'Japonesa')

restaurante_EUA.receber_avaliacao('Kleber', 10)
restaurante_EUA.receber_avaliacao('Deborah', 6)
restaurante_EUA.receber_avaliacao('Gui', 9)

restaurante_EUA.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()