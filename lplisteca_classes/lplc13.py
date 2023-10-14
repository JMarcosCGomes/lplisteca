'''
questao 13 e 14
'''

class Funcionario():

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def mostraNome(self):
        print(self.nome)
        return self.nome

    def mostraSalario(self):
        print(self.salario)
        return self.salario
    
    def aumentarSalario(self, porcentual):
        porcentagem = porcentual/100
        valor = self.salario*porcentagem
        self.salario += valor
    
harry = Funcionario("Harry Sobrenome", 1234)
harry.mostraNome()
harry.mostraSalario()
harry.aumentarSalario(10)
harry.mostraNome()
harry.mostraSalario()
