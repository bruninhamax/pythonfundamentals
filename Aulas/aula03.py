# # ====================== Dicionários =====================

# endereco = {'logradouro': 'Rua Vergueiro',
#             'numero':'3057',
#             'bairro':'Vila Mariana',
#             'cidade':'são paulo',
#             'UF':'SP',
#             'cep':'04101-300'
# }

# endereco_2 = {'logradouro': {'user1': 'Rua Vergueiro',
#                              'user2': 'Rua Augusta'
#                             },
#             'numero':{'user1': '3057',
#                       'user2': '1050'
#                      },
#             'bairro':{'user1': 'Vila Mariana',
#                       'user2': 'Cerqueira Cesar'
#                      },
#             'cidade':{'user1': 'são paulo',
#                       'user2': 'são paulo'
#                      },
#             'UF':{'user1': 'SP',
#                   'user2': 'SP'
#                  },
#             'cep':{'user1': '04101-300',
#                    'user2': '01212-030'}
# }

# # print(endereco.keys()) # Retorna só as chaves
# # print(endereco.values()) # Retorna só os valores
# # print(endereco.items()) # Retorna todos os itens

# print(endereco_2,'\n\n')
# # Altera o número do user2:
# # endereco_2.__setitem__('numero', {'user1': '3057',
# #                                   'user2': '1030'})

# # Também altera o número do user2:
# endereco_2['numero']['user2'] = '1030'
# print(endereco_2)
# # print(endereco_2.keys())
# # print(endereco_2.values())

# # Convertendo para dicionário:
# var_dict = dict(nome='Bruna', sobrenome='Maximiano')
# print(var_dict)

# =================== Concatenar e inserir dados ====================

municipios_br = '5.570'
estados_br = '26'

# Usando o format:
brasil = 'O Brasil tem {} estados federados, {} municípios e o Distrito Federal.'.format(estados_br, municipios_br)
print(brasil)

# Usando o fstring:
brasil2 = f'O Brasil tem {estados_br} estados federados, {municipios_br} municípios e o Distrito Federal.'
print(brasil2)

teste = 'teste'
teste2 = 'teste2'

print(teste + ' ' + teste2)

pais = 'Brasil'
print(pais*3)