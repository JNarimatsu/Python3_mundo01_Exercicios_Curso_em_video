#Grupo da Maioridade
from datetime import date
maiores = 0
menores = 0
for c in range(1, 8):
    ano = int(input('Digite o ano do seu nascimento: '))
    idade = date.today().year - ano
    if idade >= 18:
        maiores = maiores+1
    else:
        menores = menores+1
print('Temos {} pessoas maiores de idade e {} pessoas menores de idade'.format(maiores, menores))
