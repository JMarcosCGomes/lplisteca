'''
homem de bem
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo 
regulamento de pesca do estado de São Paulo (50 quilos) 
deve pagar uma multa de R$ 4,00 por quilo excedente

leia a variável peso (peso de peixes) e calcule o excesso

Gravar na variável "excesso" a quantidade de quilos além do limite 
e na variável "multa" o valor da multa que João deverá pagar

Imprima os dados do programa com as mensagens adequadas.
'''

peso = int(input("Insira o peso: "))

if peso - 50 > 0:
    excesso = peso - 50
else:
    excesso = 0

multa = excesso*4

print("Peso: " + str(peso))
print("Excesso: " + str(excesso))
print("Multa: " + str(multa))