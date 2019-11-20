# # ================= ORIENTAÇÃO A OBJETO ================

# class Servidor:
#     memoria = None
#     disco = None
#     cpu = None

# dns = Servidor()

# dns.memoria = 2048
# dns.disco = 50
# dns.cpu = 2

# print(f'O servidor tem as seguintes configurações:\
#      \nCPU: {dns.cpu}\
#         \nDisco: {dns.disco}\
#             \nMemória: {dns.memoria}')

# class PrimeiraClasse:
#     def __init__(self):
#         print('Acessando o método construtor')

#     def metodo(self):
#         print('Acessando método')

# classe = PrimeiraClasse()

# classe.metodo()

class Passaro():

    def __init__(self):

        self.asa = 2
        self.bico = 1
        self.penas = True
        self.patas = 2
        self.rabo = True

    def voar(self):

        if self.asa < 2:

            self.t = 1
            print('Pássaro deficiente')

        else:
            
            print('Voando...')
            self.t = 0

    def pousar(self):

        if self.t == 1:

            pass

        else:

            print('Pousando...')

    def dormir(self):

        print('Dormindo...')

    def acordar(self):
        
        print('Acordando...')

sabia = Passaro()

sabia.patas = 1
sabia.asa = 1
sabia.rabo = None

sabia.voar()
sabia.pousar()
sabia.dormir()
sabia.acordar()