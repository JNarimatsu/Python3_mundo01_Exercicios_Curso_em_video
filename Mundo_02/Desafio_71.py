#Simulador de caixa eletrônico
print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)
valor = int(input('Que valor deseja sacar? R$'))
total = valor 
cedulas = 50
total_cedulas = 0
while True:
    if total>= cedulas:
        total -= cedulas
        total_cedulas += 1
    else:
        print(f'Total de {total_cedulas} cédulas de R${cedulas}')
        if cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 1
        total_cedulas = 0
        if total == 0:
            break