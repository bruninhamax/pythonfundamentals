#v1 = input('Digite seu nome e sobrenome: ')
#print('Seu nome e sobrenome: ', v1)

#print(input('Digite seu nome e sobrenome: '))

# Converter variáveis:
# print(int(input('Digite um número')))
# Acima convertermos uma string para inteiro.

# Como saber o tipo de variável:
#numero = 5
#print(type(numero))
# A função "type" retorna o tipo da variável

# primeiro_numero = '5'
# segundo_numero = '23'
# terceiro_numero = '25'

# print (int(primeiro_numero) + int(segundo_numero) + int(terceiro_numero))

# Comparação:
#linguagem = 'java'

#if linguagem == 'python':
#    print('A linguagem é python')

#else:
#    print('A linguagem não é python')

# ============================ LISTAS ===============================

#lista = ['teste', 'carro', 'abacaxi', 'laranja', 'moto', 'timão']

# Remove um elemento da lista:
#lista.pop(3)
#print(lista)

# Insere um elemento numa determinada posição:
#lista.insert(3, 'laranja')

# Adiciona um elemento ao final da lista:
#lista.append(10)
#lista.append('Carros')

# Remove o primeiro elemento da lista:
#lista.pop(0)

# Ordenando a lista:
#lista.sort()
#print(lista)

# Ordenando ao contrário:
#lista.sort(reverse=True)
#print(lista)

# Lista comum:
#lista = ['teste', 'carro', 'abacaxi', 'laranja', 'moto', 'timão', 1, 2, 2, 4, 4, 4, 5, 2, 3, 4, 4, 'abacaxi']

# Lista dentro da lista:
#lista2 = [[1, 2, 3], ['carro', 'moto', 'bike'], 'casa']

# Mostra lista 2
#print(lista2)

# # Mostra o primeiro elemento da lista2 (vai retornar [1, 2, 3])
#print(lista2[0])

# # Mostra o primeiro elemento da primeira lista dentro da lista2
#print(lista2[0][0])

# # Conta quantas vezes "2" aparece na lista
#print(lista.count(2))

# # Conta quantas vezes "abacaxi" aparece na lista
#print(lista.count('abacaxi'))

# # Substitui o segundo elemento da primeira lista dentro da lista2
#lista2[0][1] = 50
#print(lista2)

# # Mostra a primeira posição em que o valor 2 aparece na lista
#print(lista.index(2))

# =========================== TUPLAS ==================================
#tupla=(1, 2, 3, 4, 5, 6)

# Conta quantas vezes o valor 1 aparece na tupla
#print(tupla.count(1))

#tupla2=('Python', 'Java', 'php')

# Mostra o item na posição 2 e faz com que a primeira letra seja maiúscula
#print(tupla2[2].title())

# =========================== DICIONÁRIO ===============================

dicionario = {'nome': 'Bruna', 'sobrenome': 'Maximiano', 'idade': 23}

print(dicionario['nome'])
print(dicionario['sobrenome'])
print(dicionario['idade'])

# Mostra as chaves
print(dicionario.keys())

nome = 'Bruna'
print (f'Meu nome é {nome}')