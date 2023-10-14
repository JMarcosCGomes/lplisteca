'''
Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado
 e calcular Área;
'''
class Quadrado:


    def __init__(self, lado):
        self.lado = lado

    def mudaLado(self, novo_lado):
        self.lado = novo_lado

    def retLado(self):
        return self.lado
    
    def calcArea(self):
        return self.lado*self.lado


quad = Quadrado(8)

print(f'O lado atual do quadrado eh {quad.retLado()}, a area eh {quad.calcArea()}')

quad.mudaLado(15)
print(f'O lado alterado do quadrado eh {quad.retLado()}, a area eh {quad.calcArea()}')