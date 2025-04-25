#Seno, cosseno e tangente 
import math
angulo = float(input('Digite o angulo que você deseja: '))
#é necessário informar como radiano
seno = math.sin(math.radians(angulo))
print('O ângulo de {} tem SENO de {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O ângulo de {} tem COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O ângulo de {} tem Tangente de {:.2f}'.format(angulo, tangente))