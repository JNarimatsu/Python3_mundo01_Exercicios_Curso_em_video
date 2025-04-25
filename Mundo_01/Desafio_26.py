#Primeira e última ocorrência de uma string
frase = input('Digite Uma frase: ').strip()
frase = frase.upper()
num_frase = frase.count('A')
print('A frase "{}" tem a letra "A" {} vezes'.format(frase, num_frase))