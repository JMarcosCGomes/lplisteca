class bombaCombustivel():

    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):

        self.tipo = tipoCombustivel
        self.vpl = valorLitro
        self.qtdComb = quantidadeCombustivel

    def alterarQuantidadeCombustivel(self, valNovo):
        self.qtdComb = int(valNovo)

    def tiraCombustivel(self, valTira):
        self.qtdComb -= valTira

    def abastecerPorValor(self, valor):
        valAbast = valor/self.vpl
        self.tiraCombustivel(valAbast)
        print(f'Valor abastecido: {valAbast}')
        return valAbast

    def abastecerPorLitro(self, qtd):
        valoraPagar = qtd*self.vpl
        self.tiraCombustivel(qtd)
        print(f'O valor a pagar eh {valoraPagar} reais')
        return valoraPagar

    def alteraValor(self, novoValor):
        self.vpl = float(novoValor)

    def alteraCombustivel(self, novoTipo):
        self.tipo = novoTipo

    def mostraValor(self):
        print(self.vpl)
        return self.vpl

    def mostraTipo(self):
        print(self.tipo)
        return self.tipo

    def mostraQtd(self):
        print(self.qtdComb)
        return self.qtdComb


# deixei duas feitas aqui
bomba1 = bombaCombustivel("bom", 4, 2500)
bomba2 = bombaCombustivel("melhor que o seu", 6, 1200)

while 1:
    print(" 'a' para abastecer; 't' para trocar valores; v para ver valores")
    escolha = input("Escolha: ")

    if escolha == 'a':

        print("l -> por litro; v -> por valor")
        escolha2 = input("Escolha como quer abastecer: ")

        if escolha2 == 'l':
            algumNumero = int(input("Quantos litros: "))
            bomba1.abastecerPorLitro(algumNumero)

        elif escolha2 == 'v':
            algumNumero = int(input("Quanto vai pagar: "))
            bomba1.abastecerPorValor(algumNumero)

        else:
            print("Nao entendi..")

    elif escolha == 't':
        print("v -> valor; t -> tipo de combustivel; q -> quantidade de combustivel")
        escolha2 = input("Escolha o que quer receber: ")

        if escolha2 == 'v':
            algumNumero = int(input("Escreva o valor: "))
            bomba1.alteraValor(algumNumero)

        elif escolha2 == 't':
            palavraQualquer = input("Escreva o novo tipo de combustivel: ")
            bomba1.alteraCombustivel(palavraQualquer)
        elif escolha2 == 'q':
            algumNumero = int(
                input("Escreva a nova quantidade de combustivel dessa bomba: "))
            bomba1.alterarQuantidadeCombustivel(algumNumero)
        else:
            print("Nao entendi..")

    elif escolha == 'v':
        print(
            "v -> valor por litro; t -> tipo de combustivel; q -> quantidade de combustivel")
        escolha2 = input("Escolha o que quer ver: ")

        if escolha2 == 'v':
            bomba1.mostraValor()

        elif escolha2 == 't':
            bomba1.mostraTipo()

        elif escolha2 == 'q':
            bomba1.mostraQtd()

        else:
            print("Nao entendi..")

    else:
        break
