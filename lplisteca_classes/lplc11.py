class Carro():

    def __init__(self, consumo, qtd = 0):
        self.consumo = consumo
        self.qtd = qtd

    def andar(self, distancia):
        self.qtd -= distancia/self.consumo

    def obterGasolina(self):
        print(self.qtd)
        return self.qtd
    
    def adicionarGasolina(self, valor):
        self.qtd += valor

meuFusca = Carro(15)
meuFusca.adicionarGasolina(20)
meuFusca.andar(100)
meuFusca.obterGasolina()
