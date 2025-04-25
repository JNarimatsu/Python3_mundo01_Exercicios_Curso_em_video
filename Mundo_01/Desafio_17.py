#Catetos e Hipotenusa
import math
cat_oposto = float(input('Comprimento do cateto oposto: '))
cat_adjacente = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(cat_oposto, cat_adjacente)
print('A hipotenusa será de {:.2f}'.format(hi))