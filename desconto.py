valor = float(input('Digite o valor da compra: R$ '))

if valor >= 1000:
    desconto = valor * 0.15
elif valor >= 500:
    desconto = valor * 0.10
elif valor >= 100:
    desconto = valor * 0.05
else:
    desconto = 0

valor_final = valor - desconto

print(f"Valor original: R$ {valor:.2f}")      
print(f"Desconto: R$ {desconto:.2f}")        
print(f"Valor final: R$ {valor_final:.2f}")  