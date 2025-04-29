#Tabuada v3.0
cont = 1
while True:
   n = int(input('Digite um número para ver sua tabuada: '))
   print('-='*30)
   if n<0:
     break
   for cont in range (1, 11):
    print(f'{n} x {cont:2} = {n*cont}')
print('-='*30)
   
print('Fim dos cálculos!')