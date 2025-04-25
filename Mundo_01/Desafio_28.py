#Jogo da advinhação v.1.0
import random
lista = [0, 1, 2, 3, 4, 5]
escolhido = random.choice(lista)
numero = int(input('Advinha em que número estou pensando de 0 a 5: '))
if numero == escolhido:
    print('Parabéns, eu realmente estava pensando no número {}'.format(escolhido))
else:
    print('Sinto muito o número que eu estava pensando era {} e não o número {}'.format(escolhido, numero))
