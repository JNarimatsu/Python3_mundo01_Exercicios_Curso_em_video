#Estatística em produtos 
total_compras = produto_1000 = menor_preco = cont = 0
barato = ''

while True:
    produto = input('Digite o nome do produto: ')
    preco = float(input('Digite o preço do produto: R$ '))
    cont += 1
    total_compras += preco
    if preco >1000:
        produto_1000 +=1
    if cont == 1 or preco < menor_preco:
        menor_preco = preco
        barato = produto
    resposta = ' '
    while resposta not in 'SN':
         resposta = input('Quer continuar? [S/N] ').strip().upper()
    if resposta == 'N':
        break
    print('-='*30)
print('Compras encerradas!')
print(f'O total gasto na compra foi de R${total_compras:.2f}')
print(f'{produto_1000} custando mais de R$1000 reais ')
print(f'O produto mais barato é o {barato} que custa {menor_preco:.2f}')
        



