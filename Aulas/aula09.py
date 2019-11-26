# # ======================= Testes ========================= 

# a = 2
# b = 2

# # Testando se a é igual a b. Se não for, mostrará a mensagem
# assert a == b, 'a é diferente de b'

# # Testando se a é diferente de b. Se não for, mostrará a mensagem
# assert a != b, 'a é igual a b'

# def somar(x, y):
#     return x + y

# def subtrair(x, y):
#     return x - y

# def dividir(x, y):
#     return x / y


# assert somar(2,2) == 4, f'Obtido: {somar(2,2)}, Esperado: 4'
# assert somar(3,3) == 6, f'Obtido: {somar(3,3)}, Esperado: 6'

# assert subtrair(2,2) == 0, f'Obtido: {subtrair(2,2)}, Esperado: 0'
# assert subtrair(5,2) == 3, f'Obtido: {subtrair(5,2)}, Esperado: 3'

# assert dividir(10,2) == 5, f'Obtido: {dividir(10,2)}, Esperado: 5'
# assert dividir(3,3) == 1, f'Obtido: {dividir(3,3)}, Esperado:1'

# from unittest import TestCase, main


# def somar(x, y):
#     return x + y

# def subtrair(x, y):
#     return x - y

def validar_par(num: int) -> bool:

    '''
    Função para validar um número par.

    Args:
        num - recebe um número do tipo inteiro

    Retorno: Booleano
    '''

    if isinstance(num, int):
        
        return True if num % 2 == 0 else False

    elif isinstance(num, str):

        if num.isnumeric():
            return True if int(num) % 2 == 0 else False

    else:

        return None

