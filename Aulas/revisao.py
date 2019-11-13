# string = 'palavra' ou "palavra" ou 'numero' ou "numero"
# inteiro = 10 ou 14 ou -10 ou 15
# float = 1.50 ou 10.18 ou -1.50 ou -10.18 ou 10.00
# bool = True ou False

# s = True

# if s is True:
#     print('É true')

# else:
#     print('É False')

# =========================== Strings ====================================

rua = 'verGueiro'
print('String:',rua)

# Mostra a o elemento na 5ª posição da string
print('5º elemento da string:',rua[5])

# Mostra tudo em caixa alta
print('Tudo em caixa alta:',rua.upper())

# Mostra tudo em caixa baixa
print('Tudo em caxa baixa:',rua.lower())

# Deixa a primeira letra maiúscula
print('Primeira letra maiúscula:',rua.capitalize())

endereco = 'Rua Vergueiro 1057'

# Faz a separação da variável, de acordo com o separador especificado. 
# Abaixo o separador especificado é o espaço
print(endereco.split(' '))

# Para popular uma variável em várias linhas, basta incluir a barra ao contrário no final da linha
amazon = '1998,acre,Janeiro,0,1998-01-01 \
1999,Acre,Janeiro,0,1999-01-01'

# Já neste, o separador especificado é a vírgula
print(amazon.split(','))

# ========================= Listas ==============================

# Listas podem guardar diferentes tipos de dados
lista_1 = [1, 2, 3, 'abacaxi', 'carro', 1.4, True]

print(lista_1[0]) # Indexar lita
lista_1.append('casa') # Adiciona coisas à lista
lista_1.pop(0) # Remover pelo index
lista_1.remove('carro') # Remover pelo nome
lista_1.sort() # Mostra em ordem alfabética (não vai funcionra pqe esta lista não está só com string)
lista_1.sort(reverse=True) # Mostra em ordem alfabética ao contrário
lista_1.reverse() # Deixa a lista ao contrário (primeiro elemento será o último, o segundo o penúltimo...)

# ========================= Tuplas ===============================

tupla = (1, 3, 4, 5) # Imutável
tupla = 1, 2, 3 # Tupla também imutável
tupla.count(1) # Conta itens dentro da tupla
tupla.index(0) # Retorna o item do index
