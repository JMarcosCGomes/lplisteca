'''
Classe Conta Corrente: 
Crie uma classe para implementar uma conta corrente. 
A classe deve possuir os seguintes atributos:
número da conta, nome do correntista e saldo. 

Os métodos são os seguintes: 
alterarNome, depósito e saque;
No construtor, saldo é opcional, com valor default zero
e os demais atributos são obrigatórios.
'''


class CC:

    def __init__(self, numero, nome, saldo=0):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo

    def alterarNome(self, novoNome):
        nomeAntigo = self.nome
        self.nome = novoNome
        print(f"O nome foi alterado de'{nomeAntigo}', para '{novoNome}'")

    def deposito(self, extra):
        self.saldo += extra
        print(f"Deposito efetuado, novo saldo: {self.saldo}")

    def saque(self, valor):
        if self.saldo < valor:
            print("Saldo insuficiente")
        else:
            self.saldo -= valor
            print(f"Saque efetuado, novo saldo: {self.saldo}")


alguem = CC(12345, "pessoa")
alguem.saque(300)
alguem.alterarNome("pessoa mudada")
alguem.deposito(500)
alguem.saque(430)