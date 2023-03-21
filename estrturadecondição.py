import random

print('-----Jogo de Adivinhação----')

numero_aleatorio = random.randint(1,10)
tentativas = 3

while tentativas > 0:
    number = int(input('Escolha um número:'))

    if number == numero_aleatorio:
        print('Parabéns você acertou o número era {}'.format(numero_aleatorio))
        break
    else:
        print('Você errou tente novamente')
        tentativas -= 1

if tentativas == 0:
    print('Você estourou seu número de tentativas o número aleatório era {}'.format(numero_aleatorio))
