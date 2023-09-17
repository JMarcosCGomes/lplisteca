'''
Faça um Programa que peça 2 números inteiros e um número real.

Calcule e mostre:
 - o produto do dobro do primeiro com metade do segundo .
 - a soma do triplo do primeiro com o terceiro.
 - o terceiro elevado ao cubo.

'''

pri = int(input("Insira o primeiro numero (inteiro): "))
seg = int(input("Insira o primeiro numero (inteiro): "))
ter = float(input("Insira o terceiro numero (real): "))


p1 = (pri*2) * (float(seg/2))
#p1 = pri*seg = pri*seg*2/2
print("O produto do dobro do primeiro com metade do segundo: ")
print(p1)

p2 = pri*3 + ter
print("A soma do triplo do primeiro com o terceiro: ")
print(p2)

p3 = pow(ter,3)
#p3 = ter*ter*ter
print("O terceiro elevado ao cubo: ")
print(p3)
