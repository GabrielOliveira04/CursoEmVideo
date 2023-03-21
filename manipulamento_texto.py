nome = str(input('Digite seu nome por favor:'))
primeiro_nome = nome.split()[0]
print('Seu nome com letra maiscula {}'.format(nome.upper()))
print('Seu nome com letra minuscula {}'.format(nome.lower()))
print('Seu nome tem esse total de letras {}'.format(len(nome.replace(" ",""))))
print('Quantas letras tem o primeiro nome{}'.format(len(primeiro_nome)))