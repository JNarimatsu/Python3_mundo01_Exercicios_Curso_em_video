#Progressão aritmética v2.0
pt = int(input('Digite o primeiro Termo: '))
razao = int(input('Digite a razão: '))
termo = pt
cont = 1
while cont <=10:

    print('{}'.format(termo), end= ' -> ')
    termo += razao
    cont +=1
print('  FIM')