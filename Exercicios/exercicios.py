# # ======================= AULA 1 - 11/11/2019 ================================

# # Faça um programa que imprima o nome do seu time
# print ('Corinthians!!!')

# # Faça um programa que peça um número e imprima esse número
# print(input('Digite um número: '))

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

# # ============ Conversão de tipos:

# # Dado a variável var = 15, peça que o usuário digite um número e multiplique por var

# var = 15
# print(int(input('Digite um número: ')) * var)

# # ==================== Exercício da aula04 (não fui) =========================

# # Programa para o cálculo de uma folha de pagamento, Os descontos são do Imposto de Renda, que
# # depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a
# # 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
# # O Salário Líquido corresponde ao Salário Bruto menos os descontos.
# # O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# # Desconto do IR:
# # Salário Bruto Desconto IR
# # Até 1.900 isento
# # De 1.901 até 2.800 7%
# # De 2.801 até 3.700 15%
# # de 3.701 até 4.600 22%
# # Acima de 4.600 27%

# print('\n============== SOFTWARE DE FOLHA DE PAGAMENTO ==============\n')

# valhora = float(input('Valor da hora: '))
# horatotal = float(input('Total de horas trabalhadas: '))

# bruto = valhora * horatotal
# sind = bruto * 0.03

# if bruto > 4600:

#     aliqt = 27

# elif bruto >= 3701 and bruto <= 4600:

#     aliqt = 22

# elif bruto >= 2801 and bruto <= 3700:

#     aliqt = 15

# elif bruto >= 1901 and bruto <= 2800:

#     aliqt = 7

# else:

#     aliqt = 0

# ir = bruto * (aliqt/100.0)
# liq = bruto - ir - sind
# fgts = bruto * 0.11
# descontos = ir + sind

# print(f'\nSalário bruto ({valhora}) * ({horatotal}): R$ {bruto:4.2f}')
# print(f'(-) Imposto de Renda ({aliqt}%): R$ {ir}')
# print(f'(-) Sindicato (3%): R$ {sind:4.2f}')
# print(f'FGTS (11%): R$ {fgts:4.2f}')
# print(f'Total de descontos: R$ {descontos:4.2f}')
# print(f'Salário líquido: R$ {liq:4.2f}')

# # Criar uma função que muda o valor de nome e printa na tela
# nome = 'João'

# def mudaNome(novo_nome):

#     nome = novo_nome
#     return nome

# print(mudaNome('Bruna'))

# # Criar uma função que pega o conteúdo da variável texto e deixa em caixa alta

# texto = 'Eu sou um cérebro, Watson. O resto é mero apêndice.'

# def upper_texto(text):
#     return text.upper()

# print(upper_texto(texto))

# # Crie uma função que peça 2 números e retorne o maior
# # se o valor for igual, retorna "Valroes iguais"
# # guarde em uma variável e print

# def maior(x, y):

#     if (x == y):
#         return 'Valores iguais'

#     else:
#         return max(x,y)

# n = maior(1,2)
# print(n)

# # Crie uma função que receba um número indefinido de valores numéricos 
# # com *args e retorne os valores ordenados de forma decrescente

# def ordena(*val):
#     return sorted(val, reverse=True)

# n2 = ordena(5,2,6,1,8,2)
# print(n2)