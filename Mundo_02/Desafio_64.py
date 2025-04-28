#Tratando vários valores v1.0
num = 0
cont = 0
soma = 0
num = int(input('Digite um número para ser somado ou 999 para parar o programa: '))
while num != 999 :
    soma += num
    cont+=1
    num = int(input('Digite um número para ser somado ou 999 para parar o programa: '))
   
   
   
print('Foram informado {} números e a soma deles é igual a {}'.format(cont, soma ))