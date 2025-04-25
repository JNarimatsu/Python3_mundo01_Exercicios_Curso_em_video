#Maior e menor valores
salario = float(input('Digite o valor de seu salario: '))
if salario>=1250:
    salario_atual = (salario*10/100) + salario
    print('Salario atualizado é igual a {}'.format(salario_atual))
else:
    salario_atual = (salario*15/100) + salario
    print('Salario atualizado é igual a {}'.format(salario_atual))