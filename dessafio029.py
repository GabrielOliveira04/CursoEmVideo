##escreva um programa em python 3 que vai lê a velocidade do carro
##se ele ultrapassar 80km/h, mostre uma menssagem dizendo que ele foi multado
#a multa vai custar R$7 reaiss por cada km acima do limite.

velocidade = 0
multa = 0

while True:
    velocidade=int(input('Digite a velocidadee atual do carro em km/h:'))

    if velocidade >80:
        multa += 7
        print('Você ultrappasssou do limite tome uma muta de R$7,00')

    continuar = input('Você deseja continuar? (S/N').lower()
    if continuar == 'n':
        break
print('O total de multas é R${}'.format(multa))