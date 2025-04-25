from datetime import date
nome = input('Digite seu nome: ')
genero = int(input('''você se identifica com qual genero:
               [1] Masculino
               [2] Feminino
                   '''))
ano = int(input('Qual o ano de seu nascimento? '))
idade = date.today().year - ano
if genero == 1 and idade > 18:
    print('{} tem {} anos e passou da idade de se alistar, você deveria ter se alistado a {} anos'.format(nome, idade, idade-18))
elif genero==1 and idade < 18:
    print('{} tem {} anos e ainda não tem a idade necessária para se alistar, você poderá se alistar em {} anos'.format(nome, idade, 18-idade))
elif genero == 2 and idade > 18:
    print('A participação de mulheres é opcional, e você poderia ter se alistado a {}, quando estava com 18 anos.'.format(idade-18))
elif genero == 2 and idade < 18:
    print('A participação de mulheres é opcional, e você poderá se alistar em {}, quando estiver com 18 anos.'.format(18-idade))
elif genero == 2 and idade == 18:
    print('A participação de mulheres é opcional, como você tem 18 anos, já pode se alistar.'.format())
else:
    print('Como você está com 18 anos ja pode se alistar'.format())