#Aprovando Empréstimo
valor_casa = float(input('Qual o valor da casa que deseja financiar? '))
salario = float(input('Informe o valor do seu salario mensal: '))
anos = int(input('Em quantos anos você deseja quitar o financiamento? '))
mensalidade = round(float(valor_casa/(anos*12)), 2)
if mensalidade > ((salario*30)/100):
    print('Seu emprestimo foi negado pois as mensalidades do financiamento serão de R${} reais mensais, durante os {} próximos anos,  o que excede os 30% de seu salário'.format(mensalidade, anos))
else:
    print('Seu emprestimo foi aprovado, as mensalidades do financiamento serão de R${} reais mensais, durante os {} próximos anos, o que está dentro dos 30% permitidos.'.format(mensalidade, anos))