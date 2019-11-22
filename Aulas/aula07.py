# # ============= POO (Herança e Polimorfismo) ==============

# # =============== Herança:

# class Pai():
#     '''Classe Pai'''

#     def __init__(self):
#         self.sobrenome = 'Pereira'

#     def get_sobrenome(self):
#         print(self.sobrenome)

# class Filho(Pai):

#     def __init__(self):

#         # Como o sobrenoma já está na classe Pai() e o Filho() herdou o pai, não é necessário colocar o sobrenome de novo
#         super().__init__()

# joao = Pai()
# joaquim = Filho()

# class Animal():

#     def __init__(self, raca, idade):

#         self.olhos = True
#         self.orgaos = True
#         self.raca = raca
#         self.idade = idade

#     def Nascer(self):

#         print('Nasceu')

#     def AlimentarSe(self):

#         print('Se alimentando')

#     def Morrer(self):

#         print('Morreu')

#     def get_raca(self):

#         print(self.raca)

#     def get_idade(self):

#         print(self.idade)

# class Mamifero(Animal):

#     def __init__(self, raca, idade):

#         super().__init__(raca, idade)
#         self.pele = True
#         self.mamilos = True

# class Humano(Mamifero):

#     def __init__(self, nome, idade, pensa=True):

#         super().__init__()
#         self.nome = nome
#         self.idade = idade
#         self.pensa = pensa
#         self.bracos = 2
#         self.pernas = 2
#         self.cabeca = 1
#         self.tronco = 1

#     def Pensar(self):

        # print('Pensando')

# humano1 = Humano('João',21)

# humano1.Nascer()
# humano1.AlimentarSe()
# humano1.Morrer()
# print(humano1.bracos)
# print(humano1.nome, humano1.idade, humano1.pensa)
# humano1.Pensar()

# cachorro = Mamifero('Pastor', 7)

# print(cachorro.get_idade(), cachorro.get_raca())

# ============== Polimorfismo:
# A classe herdeira tem uma função com o mesmo nome de uma função que existe na classe pai, mas com outra(s) funcionalidades

class Pai():

    def trabalhar(self):
        print('Trabalhando de Engenheiro')

class Filho(Pai):

    def trabalhar(self):
        print('Trabalhando de Programador')

# Neste arquivo, o comando abaixo imprimirá a mensagem "Eu sou o __main__"
# Em outros arquiv, imprimirá "Eu sou o aula07", pois o comando não está nele e sim neste arquivo.

print(f'Eu sou o {__name__}')

if __name__ == "__main__":

    joao = Pai()
    joaquim = Filho()

    joao.trabalhar()
    joaquim.trabalhar()