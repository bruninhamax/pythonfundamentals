class ContaBancaria():

    def __init__(self, cliente, conta, ag=8, banco=999, saldo=0):

        self.cliente = cliente
        self.conta = conta
        self.ag = ag
        self.banco = banco
        self.saldo = saldo

    def depositar(self):

        try:

            deposito = float(input('Digite o valor para depósito: R$ '))
            print(f'Saldo anterior: R$ {self.saldo}')
            print(f'Deposito: R$ {deposito}')
            self.saldo += deposito
            print(f'Novo saldo: R$ {self.saldo}')
            print('-'*20)

        except ValueError:

            print('Digite apenas números')
            print('-'*20)

    def sacar(self):

        try:

            saque = float(input('Digite o valor para saque: R$ '))

            if saque <= self.saldo:

                print(f'Saldo anterior: R$ {self.saldo}')
                print(f'Saque: R$ {saque}')
                self.saldo -= saque
                print(f'Novo saldo: R$ {self.saldo}')
                print('-'*20)

            else:
                print('Saldo insuficiente')
                print(f'Saldo atual: R$ {self.saldo}')
                print('-'*20)

        except ValueError:

            print('Digite apenas números!')
            print('-'*20)

    def extrato(self):
        print('Extrato')
        print('=' * 20)
        print(f'Agência: 0{self.ag} Conta: {self.conta}')
        print(f'Cliente: {self.cliente}')
        print(f'Saldo: {self.saldo}')
        print('-'*20)

op = 1

cliente = ContaBancaria(input('Digite o nome do cliente: '), input('Digite o número da conta: '))

print('============== OldBank =============')
print('========= Seja bem-vindo(a) ========')

while op > 0:

    try:

        print('Selecione uma opção:')
        print('Para fazer um depósito, digite 1')
        print('Para fazer um saque, digite 2')
        print('Para ver o extrato, digite 3')
        print('Para finalizar, digite 0')
        op = int(input('> '))

        if op > 3:

            raise ValueError

        elif op == 1:

            cliente.depositar()

        elif op == 2:

            cliente.sacar()

        elif op == 3:

            cliente.extrato()

    except ValueError as t:

        print('Digite apenas números de 0 a 3')
        print('-'*20)

print(f'Obrigada por usar nosso banco, {cliente.cliente}!')