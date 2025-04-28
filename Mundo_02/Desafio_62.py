#Progressão aritmética v3.0
print('-='*30)
pt = int(input('Digite o primeiro Termo: '))
razao = int(input('Digite a razão: '))
termo = pt
cont = 1
total = 0
mais = 10
while mais !=0:
    total = total + mais
    while cont <= total:

        print('{}'.format(termo), end= ' -> ')
        termo += razao
        cont +=1
    print('  PAUSA ')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))