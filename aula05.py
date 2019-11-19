# ================== Manipulação de arquivos =========================
arq1 = '/home/developer/pythonfundamentals/Arquivos/sherlock.txt'

# # Mostra o conteúdo do arquivo
# print(arq1.read())
# # Mostra a quantida de caracteres (só funciona se usar o read antes)
# print(arq1.tell())
# arq1.seek(0,1)

# print(arq1.read(51))

# arq1.close()

# with open(arq1,'x') as f:

#     f.write('Abrindo arquivo em python')

# with open(arq1,'r+') as f:

#     print(f.read()) # Mostra o arquivo
#     print(f.readlines()) # Mostra o arquivo dentro de uma lista.

# # ===================== Funções

# def soma(x,y):
#     print(x + y)

# soma(1,2)

# produtos = []

# def cadastraProduto(produto):
    
#     produtos.append(produto)

# def listarProdutos():
    
#     for p in produtos:
#         print(p)

# produto = ""
# while produto != 'sair':

#     produto = input('Digite o produto que deseja cadastrar: ')
#     cadastraProduto(produto)
#     print('Produto cadastrado')
    
# produtos.pop(-1)
# listarProdutos()

# def alteraServidor(atual, novo):
#     print(f'O IP atual é: {atual} e o novo é: {novo}')

# alteraServidor('123','321')

# def conexao():
#     r = requests.get('https://google.com')

#     return r.status_code

# conexao()

# def media(x, y):
#     return (x+y)/2

# print(media(10,2))

# # ================== Args (transforma os parâmetros numa tupla)

# def printa(*valores):

#     print(valores)
#     print(valores[0])
#     print(valores[1])

# printa('nome','sobrenome')

# # =================== Kwargs (transforma os parâmetros num dicionário)

# def printa2(**valores):
#     print(valores)

# printa2(var1='valor1', val2='valor2', val3='valor3')

texto = 'Eu sou um cérebro, Watson. O resto é mero apêndice.'

def split_texto(text):
    return text.split(' ')

def lower_texto(text):
    return text.lower()

arquivo_novo = split_texto(lower_texto(texto))

print(arquivo_novo)