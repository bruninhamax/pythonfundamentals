# # ======================= AULA 1 - 11/11/2019 ================================

# # Faça um programa que imprima o nome do seu time
#print ('Corinthians!!!')

# # Faça um programa que peça um número e imprima esse número
#print(input('Digite um número: '))

# # ======================= AULA 2 - 12/11/2019 ================================

# # Faça um programa que receba 'F' ou 'M' e mostre feminino ou masculino
# print('Informe seu sexo:')
# print('F para feminino')
# print('M para masculino')
# sexo = str.capitalize(input())

# if sexo == 'F':
#     print('Sexo feminino')

# elif sexo == 'M':
#     print('Sexo masculino')

# else:
#     print('Valor inválido')

# # Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo
# try:

#     n = int(input('Digite um número: '))

#     if n > 0:
#         print('Número positivo')

#     elif n < 0:
#         print('Número negativo')

#     else:
#         print('Número neutro')

# except ValueError as e:

#     print('Valor não numérico')

# # Dada a lista ['Corinthians', [1, 2, 3, 4, 5] ,'Palmeiras', 'São Paulo', [10, 11, 12, 13, 14],'Flamengo', 'Vasco']
# lista = ['Corinthians', [1, 2, 3, 4, 5] ,'Palmeiras', 'São Paulo', [10, 11, 12, 13, 14],'Flamengo', 'Vasco']
# print(lista)

# # printem 3, 13, 
# print(lista[1][2], lista[4][3], lista[-1])

# # printem 5, São Paulo, 14
# print(lista[1][-1], lista[3], lista[4][-1])

# # Mudem o valor do 4 para 30
# lista[1][-2] = 30

# # Mudem o valor do 10 para 100
# lista[4][0] = 100

# # Mudem o valor do 14 para 150
# lista[4][-1] = 150

# # Mudem o valor Vasco para Bragantino
# lista[-1] = 'Bragantino'

# print(lista)

# # ======================= AULA 3 - 13/11/2019 ================================

# # =============== Dicionário:

# dados = {'cidades': {
#             'saopaulo': {
#                 'nome': 'Sao Paulo',
#                 'municipios': 645,
#                 'populacao': 12.18
#             },
#             'riodejaneiro':{
#                 'nome': 'Rio de Janeiro',
#                 'municipios': 92,
#                 'populacao': 6.32
#             },
#             'minasgerais': {
#                 'nome': 'Minas Gerais',
#                 'municipios': 31,
#                 'populacao': 20.87
#             }
#         }
#     }

# # Print a quantidade de municípios de Minas
# print('Municípios de Minas:', dados['cidades']['minasgerais']['municipios'])

# # Print a quantidade de municípios do Rio
# print('Municípios do Rio:',dados['cidades']['riodejaneiro']['municipios'])

# # Print a população de Minas em milhões
# print('População de Minas:', dados['cidades']['minasgerais']['populacao']*1000000)

# # Print a população de São Paulo em Milhões
# print('População do Rio:', dados['cidades']['saopaulo']['populacao']*1000000)

# # Print o nome de São Paulo
# print('Nome da cidade de SP:', dados['cidades']['saopaulo']['nome'])

# ============ Conversão de tipos:

# Dado a variável var = 15, peça que o usuário digite um número e multiplique por var

var = 15
print(int(input('Digite um número: ')) * var)