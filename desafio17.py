import math
cat=float(input('Qual o cumprimento do cateto oposto?'))
adj=float(input('QUal o cumprimento do cateto adjacente?'))
hipotenusa= (cat**2 + adj**2)* (1/2)
print('O valor do cateto é {} e do adjacecnte é {} a hipotenusa é {}'.format(cat, adj, int(hipotenusa)))
#Ou faz assim se de vez de escreve a formula acima sendo mais rapido com a função math
hipotenusa2= math.hypot(cat,adj)
print('A  hipotenusa two é {}'.format(int(hipotenusa2)))
