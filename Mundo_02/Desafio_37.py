numero = int(input('Que número deseja converter? '))
escolha = int(input(''' 
                    Digite [1] para binário
                    Digite [2] para octal 
                    Digite [3] para hexadecimal
                    '''))

if escolha == 1:
    print('O valor {} convertido para binário é igual a {}'.format(numero, bin(numero) [2:] ))
elif escolha == 2:
    print('O valor {} convertido para octal é igual a {}'.format(numero, oct(numero) [2:] ))

elif escolha == 3:
    print('O valor {} convertido para hexadecimal é igual a {}'.format(numero, hex(numero) [2:]))
else:
    print('Opção inválida. Digite uma opção válida')
