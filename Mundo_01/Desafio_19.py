#Sorteando um item na lista
import random
aluno_01 = input('Digite o nome do primeiro aluno: ')
aluno_02 = input('Digite o nome do segundo aluno: ')
aluno_03 = input('Digite o nome do terceiro aluno: ')
aluno_04 = input('Digite o nome do quarto aluno: ')
lista = [aluno_01,aluno_02,aluno_03,aluno_04]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))

