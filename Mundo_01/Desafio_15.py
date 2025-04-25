#Aluguel de carros
dia = float(input('Digite a quatidade de dias de alguel: '))
km = float(input('Digite a quantidade de quilômetros pecorridos: '))
valor_total = float(dia*60)+(km*0.15)
print('o total a pagar por {} dias e {} Km é de R${}'.format(dia, km, valor_total))