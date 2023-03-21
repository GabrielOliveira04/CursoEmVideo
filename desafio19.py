import random

a1=str(input('Nome primeiro aluno?'))
a2=str(input('Nome segundo aluno?'))
a3=str(input('Nome terceiro aluno?'))
a4=str(input('Nome quarto aluno?'))

lista= [a1,a2,a3,a4]
sorteio=random.choice(lista)

print('O aluno sorteiado foi {}'.format(sorteio))
