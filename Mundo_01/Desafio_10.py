#Conversor de moedas
carteira = float(input('Digite qual o saldo em sua carteira: '))
dolar = float(carteira/5.8559)
print('Com o seu saldo de R${} você consegue comprar ${} em dolares'.format(carteira,dolar))