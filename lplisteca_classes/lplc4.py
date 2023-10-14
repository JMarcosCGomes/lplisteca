'''
Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura

Métodos: Envelhercer, engordar, emagrecer, crescer. 
Obs: Por padrão, a cada ano que nossa pessoa envelhece, 
sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

'''

class Pessoa:


    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def Engordar(self, extra):
        self.peso += extra

    def Emagrecer(self, valor):
        self.peso -= valor

    def Crescer(self):
        if self.idade < 22:
            self.altura += 0.05

    def Envelhecer(self):
        self.idade += 1
        self.Crescer()

#adicionei pra ver
    def mostraTudo(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Peso: {self.peso}")
        print(f"Altura: {self.altura}")
        print("----------------------")
        
        
alguem = Pessoa("alguem", 19, 45.6, 1.23)

print("Inicial")
alguem.mostraTudo()

print("Engordar")
alguem.Engordar(1.2)
alguem.mostraTudo()

print("Emagrecer")
alguem.Emagrecer(2.8)
alguem.mostraTudo()

print("Envelhecer e crescer")
alguem.Envelhecer()
alguem.mostraTudo()