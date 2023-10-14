'''
Desenvolva uma classe Macaco
atributos nome e bucho (estomago)
métodos comer(), verBucho() e digerir().

criando pelo menos dois macacos,
alimentando-os com pelo menos 3 alimentos diferentes
e verificando o conteúdo do estomago a cada refeição.

Experimente fazer com que um macaco coma o outro
'''


class Macaco():

    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, comida):
        self.bucho.append(comida)

    def comerMacaco(self, supostamenteMacaco):

        if (isinstance(supostamenteMacaco, Macaco)):

            self.bucho.append(supostamenteMacaco.bucho)
            self.bucho.append(supostamenteMacaco.nome)
            del supostamenteMacaco

        else:
            print("Isso nem eh macaco!")

    def verBucho(self):
        print(self.bucho)

    def digerir(self):
        self.bucho.pop(0)

# so testar, no caso pra comer o outro macaco tem que declarar sem aspas comerMacaco(nome)
