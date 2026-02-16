from datetime import datetime
import csv

class Pessoa:
    def __init__(self, nome: str, data_nascimento: str) -> None:

        self.nome = nome
        try: 
            self.data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
        except:
            raise ValueError("Data inválida! Use o formato dd/mm/aaaa.")   

    def calcular_idade(self) -> int:
        """Retorna a idade atual da pessoa."""
        hoje = datetime.today()
        idade = hoje.year - self.data_nascimento.year
        if (hoje.month, hoje.day) < (self.data_nascimento.month, self.data_nascimento.day):
            idade -= 1
        return idade
    
def cadastrar_pessoas() -> list[Pessoa]:
    """Cadastrar múltiplas pessoas e retorna a lista"""
    pessoas: list[Pessoa] = []
    qtd = int(input("Adicione o número de pessoas:"))

    for i in range(qtd):
        print(f"\nCadastro {i+1}")
        nome = input("Nome:")
        while True:
            try:
                data_nasc = input("Data de nascimento (dd/mm/aaaa): ")
                pessoa = Pessoa(nome, data_nasc)
                pessoas.append(pessoa)
                break
            except ValueError as e:
                print(e)
                print("Tente novamente.")
    return pessoas

def salvar_csv(pessoas: list[Pessoa], arquivo: str = "pessoas.csv") -> None:
    """Salva os dados das pessoas em um arquivo CSV."""   
    with open(arquivo, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)  
        writer.writerow(["Nome", "Idade"])
        for p in pessoas:
            writer.writerow([p.nome, p.calcular_idade()]) 
    print(f"\n Dados salvos em {arquivo}") 

def exibir_pessoas(pessoas: list[Pessoa]) -> None:
    """Mostra todas as pessoas cadastradas."""
    print("\n Pessoas Cadastradas:") 
    print("-" * 30)
    for p in pessoas:
        print(f"Nome: {p.nome} | Idade: {p.calcular_idade()}")

# Execução principal
if __name__ == "__main__":
    pessoas = cadastrar_pessoas()
    exibir_pessoas(pessoas)  
    salvar_csv(pessoas) 

                      


