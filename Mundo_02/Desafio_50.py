#Soma de pares
soma = 0
cont = 0

for c in range(0, 6):
    n = int(input('Digite número: '))
    if n %2 == 0:
        soma = soma + n
    else:
        soma = soma
print('A somatória é {}'.format(soma))