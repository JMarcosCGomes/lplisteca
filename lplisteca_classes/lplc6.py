'''
Classe TV: Faça um programa que simule um televisor 
criando-o como um objeto. 

O usuário deve ser capaz de informaro número do canal
e aumentar ou diminuir o volume. 

Certifique-se de que o número do canal 
e o nível do volume permanecem dentro de faixas válidas.
canal 1-99
volume 0-100
'''


class TV:

    def __init__(self, numero, volume):
        self.numero = int(numero)
        self.volume = int(volume)
        # self.numero = numero
        # self.volume = volume

    def altera(self, valor):
        self.numero = valor

    def aumenta(self, valor):
        self.volume += valor

    def diminui(self, valor):
        self.volume -= valor


while 1:
    variavel = int(input("Escreva o numero do canal: "))
    if ((variavel < 1) or (variavel > 99)):
        continue
    else:
        break
canalAtual = variavel

variavel = int(input("Escreva o volume: "))
if variavel > 100:
    variavel = 100
elif variavel < 0:
    variavel = 0
volumeAtual = variavel


minhaTeve = TV(canalAtual, volumeAtual)
print(minhaTeve.numero)
print(minhaTeve.volume)

print("Alterar o canal = c, Aumentar = a, Diminuir = d, o resto eh sair")

while 1:

    escolha = input("Escolha: ")

    if escolha == 'c':
        while 1:
            canalNovo = int(input("Escreva o numero do canal: "))
            if ((canalNovo < 1) or (canalNovo > 99)):
                continue
            else:
                break
        minhaTeve.numero = canalNovo
        print(minhaTeve.numero)

    # fiz assim porque se o usuario escrever numero negativo ainda funcionaria
    elif escolha == 'a':

        npa = int(input("Escreva o numero: "))
        if (minhaTeve.volume + npa) < 0:
            minhaTeve.volume = 0
        elif (minhaTeve.volume + npa) > 100:
            minhaTeve.volume = 100
        else:
            minhaTeve.aumenta(npa)
        print(minhaTeve.volume)

    elif escolha == 'd':

        npd = int(input("Escreva o numero: "))
        if (minhaTeve.volume - npd) < 0:
            minhaTeve.volume = 0
        elif (minhaTeve.volume - npd) > 100:
            minhaTeve.volume = 100
        else:
            minhaTeve.diminui(npd)
        print(minhaTeve.volume)
    else:
        break
