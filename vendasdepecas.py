c = 200  # Variável para especificar o valor do lucro.

mes = int(input("Digite o mês que deseja receber o resultado: "))

r = c * mes # Variável para multiplicar o mês digitado pelo usuário(a).

print(f"A quantidade peças para o mês {mes} será {r}.")


# Calculadora de IR(Imposto de Renda) dos funcionários da empresa.

salario = int(input('Digite seu salário:'))

if salario <= 1621.00:
    print("Isento de IR.")
elif salario <= 2826:
    print("Pagará 7.5% de IR.")  
elif salario <= 3751:
    print("Pagará 15% de IR.")     
elif salario <= 4664:
    print("Pagará 22.5% de IR.")    
else:
    print("Pagará 27.5% de IR.")      






