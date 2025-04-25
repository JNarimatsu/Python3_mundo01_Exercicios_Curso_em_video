#Custo da viagem
viagem = int(input('Informe a distância de sua viagem em Km: '))
if viagem <=200:
    passagem = viagem * 0.50
    print('O valor da sua passagem é de R${} reais'.format(passagem))
else:
    passagem = viagem*0.45
    print('O valor da sua passagem é de R${} reais'.format(passagem))