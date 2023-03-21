#desenvolva um programa que pergute a distância
#de uma viagem emkm. Calcule o preço da passagem
#cobrando R$0,50 por km para viagens até 200km
#e 0,45 para viagens mais longas
#Se for mais longa que 200km pagar R$0,45 por km rodada
#senão vai pagar R$0,50 por km rodado.

distancia = 0
passagem = 0

while True:
    distancia = int(input('Qual a distancia em km que você vai viajar?'))
    if distancia >200:
       passagem += distancia *0.45
       print('Para distancia acima de 200km, você vai pagar 45 centavos a mais por cada km')

    elif distancia <= 200:
         passagem +=distancia * 0.50
         print('Para distancia  até 200km a passagem é 0,50R$')

    continuar = input('Se você desejar continuar (S/N)?').lower()
    if continuar == 'n':
        break
print(' O total que você vai pagar em passagem é {}'. format(passagem))