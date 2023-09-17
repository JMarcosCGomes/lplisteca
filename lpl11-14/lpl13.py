'''
Tendo como dado de entrada a altura (h) de uma pessoa,
construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
'''
def ofende():
    print("Escreve direito!")

oquee = "9"
peso = "Isso não deveria aparecer no print"
alt = float(input("Insira a altura"))

while(1):
    oquee = input("Homem = 1; Mulher = 0; outra coisa = nada: ")

    if oquee == '1':
        peso = 72.7*alt - 58
        break

    elif oquee == '0':
        peso = 62.1*alt - 44.7
        break

    else:
        ofende()

print(peso)