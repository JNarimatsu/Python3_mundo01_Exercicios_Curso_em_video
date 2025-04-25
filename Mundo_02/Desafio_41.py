from datetime import date
nome = input('Digite seu nome: ')
ano = int(input('Qual o ano do seu nascimento?'))
idade = date.today().year - ano
if idade <= 9:
    print('{} você tem {} anos e se enquadra na categoria Mirim'.format(nome, idade))
elif idade > 9 and idade <=14:
    print('{} você tem {} anos e se enquadra na categoria Infantil'.format(nome, idade))
elif  idade > 14 and idade <= 19:
    print('{} você tem {} anos e se enquadra na categoria Júnior'.format(nome, idade))
elif idade > 19 and idade <= 25:
    print('{} você tem {} anos e se enquadra na categoria Sênior'.format(nome, idade))
else:
    print('{} você tem {} anos e se enquadra na categoria Master'.format(nome, idade))