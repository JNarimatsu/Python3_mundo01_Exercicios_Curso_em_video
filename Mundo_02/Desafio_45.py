#Game: Pedra, papel e tesoura
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('-='*20)
jogador = int(input('''Escolha sua jogada: 
                    [0] Pedra
                    [1] Papel
                    [2] Tesoura
                    '''))
print('Jo..')
sleep(1)
print('Ken...')
sleep(1)
print('Po!!!')
sleep(1)
print('-='*50)
print('O computador jogou {}'.format(itens[computador]))
print('Você jogou {}'.format(itens[jogador]))
print('-='*20)
if computador == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Você ganhou!')
    elif jogador == 2:
        print('Você perdeu!')
elif computador == 1:
    if jogador == 0:
        print('Você perdeu!')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Você ganhou!')
elif computador ==2:
    if jogador == 0:
        print('Você ganhou!')
    elif jogador == 1:
        print('Você perdeu!')
    elif jogador == 2:
        print('Empate')
else:
    print('Jogada inválida!')