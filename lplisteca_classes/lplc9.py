'''
Possua uma classe chamada Ponto, com os atributos x e y.
Possua uma classe chamada Retangulo, com os atributos largura e altura.
Possua uma função para imprimir os valores da classe Ponto
Possua uma função para encontrar o centro de um Retângulo.
Você deve criar alguns objetos da classe Retangulo.

Cada objeto deve ter um vértice de partida, por exemplo, 
o vértice inferior esquerdo do retângulo, 
que deve ser um objeto da classe Ponto.


A função para encontrar o centro do retângulo deve retornar 
o valor para um objeto do
tipo ponto que indique os valores de x e y para o centro do objeto.

O valor do centro do objeto deve ser mostrado na tela

Crie um menu para alterar
os valores do retângulo e imprimir o centro deste retângulo.
'''


class Ponto():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def retx(self):
        return self.x

    def rety(self):
        return self.y

    def retxy(self):
        return self.x, self.y


class Retangulo():

    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.verticeInicial = Ponto(0, 0)

    def achaCentro(self):
        centroX = int(self.largura)/2
        centroY = int(self.altura)/2
        self.centro = Ponto(centroX, centroY)
        return self.centro.retxy()

    def alteraLar(self, novaLarg):
        self.largura = novaLarg

    def alteraAlt(self, novaAlt):
        self.altura = novaAlt


priRetangulo = Retangulo(120, 60)
segRetangulo = Retangulo(46, 85)
terRetangulo = Retangulo(131, 223)

meuPonto = Ponto(50, 20)
seuPonto = Ponto(70, 40)

algumNumero = 0


while 1:
    print(" 'a' pra alterar valores; 'i' imprimir valores")
    escolha = input("Escolha: ")

    if escolha == 'a':

        print("l -> largura; a -> altura")
        escolha2 = input("Escolha o que quer alterar: ")

        if escolha2 == 'l':
            algumNumero = input("Escreva o novo valor da largura: ")
            priRetangulo.alteraLar(algumNumero)

        elif escolha2 == 'f':
            algumNumero = input("Escreva o novo valor da altura: ")
            priRetangulo.alteraAlt(algumNumero)

        else:
            print("Nao entendi..")

    elif escolha == 'i':
        print("c -> centro; x -> x do meuPonto, y -> do meuPonto, xy -> x e y do MeuPonto")
        escolha2 = input("Escolha o que quer receber: ")

        if escolha2 == 'c':
            print(priRetangulo.achaCentro())

        elif escolha2 == 'x':
            print(meuPonto.retx())

        elif escolha2 == 'y':
            print(meuPonto.rety())

        elif escolha2 == 'xy':
            print(meuPonto.retxy())
        else:
            print("Nao entendi..")
    else:
        break
