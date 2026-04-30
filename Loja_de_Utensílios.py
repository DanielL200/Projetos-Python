# Função para calcular o lucro obtido no mês:

def calcular_lucro():
    lucro_por_mes = 200
    mes = int(input("Digite o mês: "))
    lucro_total = lucro_por_mes * mes
    print(f"Lucro no mês {mes}: {lucro_total}")


# Calculadora de IR(Imposto de Renda) dos funcionários da empresa.

def calcular_ir():
    salario = float(input("Digite seu salário: R$"))    

    if salario <= 1621.00:
        print("Isento de IR(Imposto de Renda).")
    elif salario <= 2826:
        print("Pagará 7.5% de IR(Imposto de Renda).")  
    elif salario <= 3751:
        print("Pagará 15% de IR(Imposto de Renda).")     
    elif salario <= 4664:
        print("Pagará 22.5% de IR(Imposto de Renda).")    
    else:
        print("Pagará 27.5% de IR(Imposto de Renda).")   


# Função para calcular o desconto do preço do produto:

def calcular_desconto():
    valor = float(input('Digite o valor da compra: R$ '))

    if valor >= 1000:
        desconto = valor * 0.15
    elif valor >= 500:
        desconto = valor * 0.10
    elif valor >= 100:
        desconto = valor * 0.05
    else:
        desconto = 0

    print(f"Valor final: R$ {valor - desconto:.2f}")


calcular_lucro()
calcular_ir()
calcular_desconto()






