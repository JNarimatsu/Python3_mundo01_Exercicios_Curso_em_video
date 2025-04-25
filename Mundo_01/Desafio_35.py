#Analisando triângulos v.1.0
print('-='*20)
print('Analisador de triângulos')
print('-='*20)

s1 = float(input('Digite o comprimento do primeiro segmento: '))
s2 = float(input('Digite o comprimento do segundo segmento: '))
s3 = float(input('Digite o comprimento do terceiro segmento: '))
if s1<s2+s3 and s2<s1+s3 and s3<s1+s2:
    print('Os segmentos acima podem formar um triângulo ', end='')
    if s1 ==s2 ==s3:
        print('equilátero!')
    elif s1!=s2!=s3 and s1!=s3:
        print('escaleno!')
    else:
        print('isóceles!')

else:
    print('Os segmentos não formam um triângulo')
