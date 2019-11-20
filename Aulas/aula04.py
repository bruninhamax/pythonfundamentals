# # ================== While ======================

# x = 1

# while x <= 10:

#     print(f"número: {x}")
#     x += 1

# print('O while acabou!')

# a = 500
# while a > 10:
#     print(a)
#     a -= 10

# # ======================= Aicionando valores em uma lista ================
# x = 1
# lista = []
# while x <= 1000:
#     lista.append(x)
#     x += 1

# print(lista)

# # ============================= For =======================================

# l = [1, 2,3, 4, 5, 6, 7, 8, 9]

# for var in l:
#     print(var)

# frutas = ['abacaxi', 'banana', 'pera', 'maca', 'ameixa']

# for num,fruta in enumerate(frutas):
#     print(num ,fruta)


# # No range, devemos classificar um período (abaixo é do 10 ao 2) e os "pulos",
# # ou seja, a variável vai de -1 em -1 de 10 até 2
# for item in range(10, 2, -1):
#     print(item)


# cont = 0

# while cont < 10:
#     print(f'vezes de execução {cont + 1}')
    
#     if cont == 2:
#         print('bloco de condição que interrompe o loop')
#         break
#     cont += 1
    
# t = 0

# while t < 10:
#     print(t)
#     if t == 5:
#         continue
#     t += 1
    
# # ======================== Erros e exceções ==========================

# try:
#     if 'mariana' == nome:
#         print('nome correto')

#     else:
#         print('nome errado')

# except Exception as e:
#     print(e)

# finally:
#     nome = 'mariana'
#     print(nome)

# try:
#     x = int(input('digite o primeiro numero: '))
#     y = int(input('digite o segundo numero: '))
#     print(x + y)

# except ValueError as v:
#     print('esse é um erro', v)


# while True:
#     try:
#         idade = int(input('Digite sua idade: '))
#         if idade < 16:
#             print('Você não pode comprar bebida alcolica e nem tirar titulo de eleitor ')
#             break
#         else:
#             if idade >= 16 and idade < 18:
#                 print('Você pode ter titulo de eleitor')
#                 break
#             else:
#                 print('Você pode  comprar bebida e ter titulo de eleitor')
#                 break
#             break
        
    
#     except Exception as e:
#         print('Isso não é um numero', e)
#         continue


# # ======================= Raise Exception ==========================

# while True:

#     try:
#         login = input('Digite o login: ')

#         if login.lower() == 'bryan':

#             raise NameError('Bryan está banido! ')

#         else:

#             print(f'Bem vindo {login}, acesso permitido! ')
#             break

#     except NameError as e:

#         print(e)

#         continue

# # ========================= Tratamento de erros ===========================

# # =================== Try:

# try:
    
#     x = int(input('Digite o primeiro número: '))
#     y = int(input('Digite o segundo número: '))
#     print(x+y)

# except ValueError as e:

#     print ('Digite apenas números', e)

# # ====================== Usando o continue com While

# while True:

#     try:
#         x = int(input('Digite o primeiro número: '))
#         y = int(input('Digite o segundo número: '))
#         print(x + y)
#         break

#     except Exception as e:

#         print('Digite apenas números!')
#         continue

# # O que estiver dentro do finally vai ser executado mesmo se houver algum erro

#     finally:
#         print('Vou ser executado de qualquer forma hahahahaha')

# # ======================= Raise

# usuarios = ['Ana', 'Caio', 'Felipe']

# while True:

#     try:
#         user = input('Digite o nome de usuario: ')

#         if user == 'Ana':

#             raise NameError('Usuário bloqueado!')
#         else:
#             print(f'Bem-vindo(a), {user}!')
#             break

#     except NameError as n:
#         print(n)
#         continue

try:
    login = input('Digite seu login: ')

    if login.lower() == 'caio':

        raise NameError('Usuário banido!')

    else:

        print(f'Bem-vindo(a), {login}!')

except NameError as n:
    print(n)