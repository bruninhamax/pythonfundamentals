# # ======================= FUNÇÕES ===========================

# # Aqui criamos a função 'soma' com os parâmetros obrigatórios x e y
# def soma(x,y):
#     return x + y

# # Ao chamar a função, devemos passar os dois parâmetros, como abaixo
# print(soma(2,3))

# # Esta função não precisa de parâmetros para ser executada:
# def hello():
#     print('Hello, World!')

# # Então não é necessário incluir nenhum parâmetro
# hello()

# # Caso queira criar uma função em que o parâmetro não é obrigatório, é só atribuir algum valor
# def teste(var=None):
#     print(var)

# # Com o args (estrelinha) não é necessário definir a quantidade de parâmetros para a função
# # Porém ao a utilizarmos, ele a transforma em uma tupla, e não vai conseguir modificá-la
# def mostraMaiorValor(*valores):

#     # A função 'max' pega o maior valor
#     print(max(valores))

# mostraMaiorValor(1,3,5,66,21,332,8)

# lista = []

# def listar():

#     global lista
#     print(lista)

# def adiciona(valor):

#     # Aqui estamos usando o 'global', pois a variável 'lista' está fora da nossa função e nós queremos alterá-la
#     global lista
#     return lista.append(valor)

# def remove(valor):

#     global lista
#     return lista.remove(valor)

# adiciona('Batata')
# remove('Batata')

# print(lista)

# carrinho = [{"nome": "Tenis", "valor": 21.70},
#             {"nome": "Camiseta", "valor": 10.33}]

# black_friday = lambda x: x/2

# for c in carrinho:
#     print(f'Nome do produto: {c["nome"]}')
#     print(f'Valor original: {c["valor"]}')
#     print(f'Valor com desconto: {black_friday(c["valor"]):1.2f}')
#     print('-=-'*11)

items = [1,2,3,4,5]

double = list(map(lambda x: x * 2, items))

print(double)

anonimas = [lambda x : x**2,
            lambda x : x**3,
            lambda x : x**4]

for i in anonimas:
    print(i(10))