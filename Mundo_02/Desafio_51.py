#Progressão aritmética
pt = int(input('Digite o primeiro Termo: '))
razao = int(input('Digite a razão: '))
decimo = pt+(10-1)*razao
for c in range(pt, decimo+razao, razao ):
    print('{}'.format(c), end= '-> ')
print('  FIM')