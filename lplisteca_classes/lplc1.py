'''
Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor
'''

class Bola:


    def __init__(self, cor, circ, mat):
        self.cor = cor
        self.circ = circ
        self.mat = mat

    def trocaCor(self, novacor):
        self.cor = novacor

    def mostraCor(self):
        print(self.cor)


bola = Bola("bonita", "14Pi", "resistente")
bola.mostraCor()
bola.trocaCor("mais bonita que a antiga")
bola.mostraCor()