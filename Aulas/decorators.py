# def oi(nome='Pedro'):
#     return "Oi, " + nome

#     def ola():
#         return 'aqui você está na função olá'

#     def boasvindas():
#         return 'aqui você está na função boasvindas'

def inc(x):
    return x + 1

def dec(x):
    return x -1

def operacao(func, x):

    resultado = func(x)
    return resultado

print(operacao(inc, 10))