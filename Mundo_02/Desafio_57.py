#Validação de Dados
genero = input('Digite seu gênero[F/M]: ').upper().strip()
while genero not in 'MmFf':
    genero = input('Digite uma opção válida! Digite seu sexo: ').upper().strip()
print('Genero {} registrado com sucesso'.format(genero))
