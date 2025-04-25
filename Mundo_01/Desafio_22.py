#Analisador de textos
nome = input('Digite seu nome completo: ')
letras = nome.split()
primeiro_nome = letras[0]
comp_nome = len(primeiro_nome)
cont_letras = ''.join(letras)
letras_nome = len(cont_letras)
print(nome.upper())
print(nome.lower())
print('O primeiro nome é o {} e tem {} letras'.format(primeiro_nome, comp_nome))
print('O nome {} tem {} letras'.format(nome, letras_nome))
