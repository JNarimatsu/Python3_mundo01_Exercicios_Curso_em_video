#Radar eletrônico
velocidade = int(input('Digite a velocidade de seu carro em Km/h: '))
if velocidade >80:
    multa = float((velocidade - 80)*7)
    print('Sua velocidade está acima da permitida, sua multa tem o valor de R${:.2f} reais'.format(multa))
else:
    print('Parabéns, você está dentro do limite de velocidade!' )