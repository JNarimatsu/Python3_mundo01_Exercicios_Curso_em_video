#Gerenciador de pagamentos
valor = float(input('Digite o valor do produto: '))
opcoes_pag = int(input('''Informe a opção de pagamento: 
                       [1] Dinheiro ou Cheque
                       [2] Cartão a vista
                       [3] Cartão em até 2x
                       [4] Cartão acima de 3x
                       '''))
if opcoes_pag == 1:
    print('Valor a pagar {}'.format(valor-(valor*10/100)))
elif opcoes_pag == 2:
    print ('Valor a pagar {}'.format(valor-(valor*5/100)))
elif opcoes_pag == 3:
    print(('Valor a pagar {}'.format(valor)))
elif opcoes_pag == 4:
    print(('Valor a pagar {}'.format(valor+(valor*20/100))))
else:
    print('Algo deu errado, digite uma opção válida!')