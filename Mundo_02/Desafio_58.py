#Jogo da advinhação
import random
lista = [0, 1, 2, 3, 4, 5,6,7,8,9,10]
escolhido = random.choice(lista)
tentativa = 0
numero = int(input('Advinha em que número estou pensando de 0 a 10: '))
while numero != escolhido:
    numero = int(input('Sinto muito não estou pensando no número {}. Tente um novo número: '.format(numero)))
    tentativa +=1
    if numero == escolhido:
        print('Parabéns, eu realmente estava pensando no número {}'.format(escolhido))
print('Você acertou em {} tentativas'.format(tentativa))
