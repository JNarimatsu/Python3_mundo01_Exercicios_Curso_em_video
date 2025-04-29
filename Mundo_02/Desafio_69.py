#Análise de dados do grupo
cont_18 =0
cont_m = 0
cont_f_20 = 0
while True:
    idade = int(input('Digite sua idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = input('Digite seu sexo [F/M]: ').strip().upper()[0]
    if idade >=18:
        cont_18 +=1
    if sexo == 'M':
        cont_m +=1
    if sexo == 'F' and idade <20:
        cont_f_20 +=1

    resposta =' '
    while resposta not in 'SN':
        resposta = input('Quer continuar? [S/N] ').strip().upper()
    if resposta == 'N':
        break
        
    print('-='*30)
print('Cadastro encerrado!')
print('-='*30)
print(f'Total de pessoas com mais de 18 anos: {cont_18}')
print(f'Ao todo temos {cont_m} homens cadastrados')
print(f'E temos {cont_f_20} Mulheres com menos de 20 anos' )