#Jogo par ou impar
from  random import randint
v=0
while True:
    jogador = int(input('Jogue um valor: '))
    computador = randint (0,10)
    total = jogador  + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')
    print('DEU PAR' if total % 2==0 else 'DEU IMPAR')
    if tipo =='P':
        if total % 2 ==0:
            print('Você venceu!')
            v+=1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2==1:
            print('Você venceu!')
            v+=1
        else: 
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'Game over! Você venceu {v} vezes.')