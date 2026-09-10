# Sistema de desconto progressivo

valor = float(input("Digite o valor total da compra: R$ "))

if valor < 200:
    desconto = 0.05
elif valor < 300:
    desconto = 0.10
else:
    desconto = 0.15

valor_desconto = valor * desconto
valor_final = valor - valor_desconto

print("\n--- RESUMO DA COMPRA ---")
print(f"Valor da compra: R$ {valor:.2f}")
print(f"Desconto: {desconto * 100:.0f}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Valor final: R$ {valor_final:.2f}")
