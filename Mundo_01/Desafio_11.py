#Pintando parede
altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
area_parede = altura*largura
tinta = area_parede/2
print('Para pintar uma parede com área de {} m^2 é necessário {} litros de tinta'.format(area_parede,tinta))