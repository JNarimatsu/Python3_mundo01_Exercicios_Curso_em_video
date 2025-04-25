#Reajuste Salarial
salario = float(input('Digite o salário do colaborador: R$'))
aumento = float(salario*15/100)
novo_salario = float(salario+aumento)
print('O novo salario do colaborador com aumento de 15% será R${}'.format(novo_salario))