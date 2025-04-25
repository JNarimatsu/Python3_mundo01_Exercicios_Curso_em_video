#Analisador Completo
somaidade = 0
maior_idade_homem = 0
nomevelho = ''
totalmulher20 = 0
for p in range(1, 5):
    print('_____ {}ª ______'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade <20:
        totalmulher20 += 1
mediaidade = somaidade/4
print('-='*20)
print('A média da idade do grupo é de {} anos '.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {} '.format(maior_idade_homem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos '.format(totalmulher20))
print('-='*20)
