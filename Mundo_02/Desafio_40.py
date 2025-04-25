print('Olá professor! Vamos calcular as notas do primeiro bimestre?')
nome_aluno = input('Digite o nome do aluno: ')
nota01 = float(input('Digite a nota da primeira prova:  '))
nota02 = float(input('Digite a nota da segunda prova: '))
media = float((nota01+nota02)/2)
print('Calculando notas...')
print('-='*50)
if media < 5:
    print('A média do aluno {} foi de {} infelizmente você está reprovado.'.format(nome_aluno, media))
elif media>=5 and media < 7:
    print('A média do aluno {} foi de {} abaixo da média e por isso você está de recuperação'.format(nome_aluno, media))
else:
    print('O aluno {} teve uma média de {} está acima da média, você foi aprovado!'.format(nome_aluno, media))