class contaInvestimento:

    def __init__(self, numero, nome, taxaJuros, saldo=0):
        self.numero = numero
        self.nome = nome
        self.taxa = taxaJuros
        self.saldo = saldo

    def adicioneJuros(self):

        porcentagem = self.taxa/100
        valor = self.saldo*porcentagem
        self.saldo += valor

# eh a parte do outro codigo
    '''
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
'''

minhaConta = contaInvestimento(9, "eu", 10, 1000)

minhaConta.adicioneJuros()
minhaConta.adicioneJuros()
minhaConta.adicioneJuros()
minhaConta.adicioneJuros()
minhaConta.adicioneJuros()

print(minhaConta.saldo)