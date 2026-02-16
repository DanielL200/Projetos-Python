from datetime import datetime

class Pessoa:
    def __init__(self, nome, data_nascimento):

        self.nome = nome
        
        self.data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")

    def calcular_idade(self):
        hoje = datetime.today()
        idade = hoje.year - self.data_nascimento.year

        if (hoje.month, hoje.day) < (self.data_nascimento.month, self.data_nascimento.day):
            idade -= 1
        return idade        

nome = input("Digite seu nome:")
data_nascimento = input("Digite sua data de nascimento:")

p1 = Pessoa(nome, data_nascimento)

print(f"Nome: {nome}")
print(f"Idade: {p1.calcular_idade()}")