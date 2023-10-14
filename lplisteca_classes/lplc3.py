

'''
Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB 
(ou Comprimento e Largura,
ou Base e Altura, a escolher)

Métodos: Mudar valor dos lados, Retornar valor dos lados,
calcular Área e calcular Perímetro;

Crie um programa que utilize esta classe.
Ele deve pedir ao usuário que informe as medidades de um local.
Depois, deve criar um objeto com as medidas e calcular 
a quantidade de pisos e de rodapés necessárias para o local.

'''


class Retangulo():

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def mudaBase(self, novaBase):
        self.base = novaBase

    def mudaAltura(self, novaAltura):
        self.altura = novaAltura

    def retBase(self):
        return self.base

    def retAltura(self):
        return self.altura

    def calArea(self):
        return int(self.base) * int(self.altura)

    def calPerimetro(self):
        return int((2*self.base)) + int((2*self.altura))


minhaBase = input("Valor da base: ")
minhaAltura = input("Valor da altura: ")

Chao = Retangulo(minhaBase, minhaAltura)

# coloquei qualquer valor, aqui precisava escolher uma area pro piso e uma pro rodape
qtdPisos = Chao.calArea() / 400
qtdRodape = Chao.calArea() / 240

print(qtdPisos)
print(qtdRodape)
