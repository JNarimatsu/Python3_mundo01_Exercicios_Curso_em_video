#Calculando descontos
preco = float(input('Digite o valor do produto: R$ '))
desconto = (5*preco)/100
preco_desc = preco-desconto
print ('O produto com preço de R${} ficará com o valor de R${} com 5% de desconto'.format(preco,preco_desc))