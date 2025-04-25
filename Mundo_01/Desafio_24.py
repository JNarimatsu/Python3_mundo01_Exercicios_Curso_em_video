#Verificando as primeiras letras de um texto
cidade = input('Digite o nome de sua cidade: ').strip()
cidade = cidade.upper().split()
print('SANTO' in cidade[0])