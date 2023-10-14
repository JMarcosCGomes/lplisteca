'''
Classe Bichinho Virtual:
Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

Atributos: Nome, Fome, Saúde e Idade 

Métodos: 
Alterar Nome, Fome, Saúde e Idade; 
Retornar Nome, Fome, Saúde e Idade 

Obs: Existe mais uma informação que devemos 
levar em consideração, o Humor do nosso tamagushi,
este humor é uma combinação entre os atributos 
Fome e Saúde, ou seja, um campo calculado, 
*então não devemos criar um atributo para
armazenar esta informação *
por que ela pode ser calculada a qualquer momento.
'''


class Pou:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade


# Entao, tratei fome e saude como um numero
# numeros maiores que zero significa quem tem algum nivel de fome/saude
# numeros menores que zero (improvavel) significam que
    '''
# Entao, tratei fome e saude como um numero
Fome:
> 0 -> com um grau x de fome
== 0 -> sem fome
< 0 -> alimentado

Saude:
> 0 -> bem saudavel
== 0 -> sem problema
< 0 -> mal da saude

eu fiz o humor como 'saude - fome' porque assim dá pro usuario escolher uma faixa de numeros pra saude e fome sem problema
(de -50 -- 50; 1 a 100 etc)
'''

    def Humor(self):

        num = int(self.saude) - int(self.fome)

        if num == 0:
            print("Nem feliz nem triste..")
        elif num > 0:
            print("Felicidade me define!")
        else:
            print("Você não tem vergonha de me deixar assim?")

    def retHumor(self):
        return int(self.saude) - int(self.fome)

    def AltNome(self):
        nNome = input("Escreva o nome: ")
        self.nome = nNome

    def retNome(self):
        return self.nome

    def AltFome(self):
        nFome = input("Altere a fome: ")
        self.fome = nFome

    def retFome(self):
        return self.fome

    def AltSaude(self):
        nSaude = input("Escreva a saude: ")
        self.saude = nSaude

    def retSaude(self):
        return self.saude

    def AltIdade(self):
        nIdade = input("Diga a idade: ")
        self.idade = nIdade

    def retIdade(self):
        return self.idade


# comeca aqui
nomeInicial = input("Nome: ")
fomeInicial = input("Fome: ")
saudeInicial = input("Saude: ")
idadeInicial = input("Idade: ")
meuPou = Pou(nomeInicial, fomeInicial, saudeInicial, idadeInicial)


while 1:
    print(" 'a' pra alterar; 'r' pra retornar")
    escolha = input("Escolha: ")

    if escolha == 'a':

        print("s -> saude; f -> fome; i -> idade; n -> nome")
        escolha2 = input("Escolha o que quer alterar: ")

        if escolha2 == 's':
            meuPou.AltSaude()

        elif escolha2 == 'f':
            meuPou.AltFome()

        elif escolha2 == 'i':
            meuPou.AltIdade()

        elif escolha2 == 'n':
            meuPou.AltNome()
        else:
            print("Nao entendi..")

    elif escolha == 'r':

        print("s -> saude; f -> fome; i -> idade; n -> nome; h -> valor do humor; d -> diga algo meu querido Pou")
        escolha2 = input("Escolha o que quer receber: ")

        if escolha2 == 's':
            print(meuPou.retSaude())

        elif escolha2 == 'f':
            print(meuPou.retFome())

        elif escolha2 == 'i':
            print(meuPou.retIdade())

        elif escolha2 == 'n':
            print(meuPou.retNome())

        elif escolha2 == 'h':
            print(meuPou.retHumor())

        elif escolha2 == 'd':
            meuPou.Humor()
        else:
            print("Nao entendi..")
    else:
        break
