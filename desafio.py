n1=float(input('Digite o valor que deseja converter em cm e mm?'))

cm=n1/100
mm=n1/1000

print('O valor de {} metros em centimetros é {} e em milimitros e {}'.format(n1, cm, mm))


altura=int(input('Digite a altura'))
largura=int(input('Digite a largura'))

a= altura * largura

print('A area do local é', a)

tinta= a/2
print('Então a quantidade de tinta para {}m² é {}l'.format(a, tinta))