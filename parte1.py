valor = float(input("Digite o valor total da compra: R$ "))

if valor < 200:
    desconto = 0.05
elif valor < 300:
    desconto = 0.10
else:
    desconto = 0.15
