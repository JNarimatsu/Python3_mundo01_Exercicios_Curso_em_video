#Vários números com flag
n= s = 0
cont = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
    cont +=1
print(f'Foram digitados {cont} números e a soma vale {s}')