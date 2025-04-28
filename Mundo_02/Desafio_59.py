#Criando um menu de opções
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
opcao = 0
resultado = 0
while opcao != 5:
    opcao = int(input('''Digite uma opção: 
                    [1] Somar
                    [2] Multiplicar
                    [3] Maior
                    [4] Novos números
                    [5] Sair do programa
                    '''))
    if opcao == 1:
        resultado = n1+n2
        print('A soma dos números {} e {} é igual a {}'.format(n1, n2, resultado))

    elif opcao == 2:
        resultado = n1*n2
        print('O produto dos números {} e {} é {} '.format(n1, n2, resultado))
   
    elif opcao == 3:
        if n1>n2:
            print('{} é maior que {} '.format(n1,n2))
        elif n1<n2:
            print('{} é menor que {}'.format(n1,n2))
        else:
            ('Os números são iguais')
    elif opcao == 4:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
        
    elif opcao ==5:
        print('Programa encerrado!')
    else:
        print('Opção inválida!')
    print('-='*30)
print('Até mais!')


    
