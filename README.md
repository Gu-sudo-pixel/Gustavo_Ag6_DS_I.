consumo = float(input("digite o consumo de energia (kwh)"))
bandeira = input("digite a bandeira tarifaria (verde/amarelo/vermelho)").strip().lower()

if consumo <=100:
    valorbase = consumo * 0,50
elif consumo <=200:
    valorbase = consumo * 0.75
else:
    valorbase = consumo * 1.00



if (bandeira == "verde"):
    taxa = 0
elif (bandeira == "amarela"):
    taxa = consumo * 0.02

elif (bandeira == "vermelho"):
    taxa = consumo * 0.5
else:
    print("bandeira inválido")
    taxa = 0

#calculando o total
ValorTotal = valorbase * taxa

print("conta de luz")
print(f"consumo {consumo}")
print(f"valor base {valorbase}")
print(f"taxa extra {taxa}")
print(f"total a pagar {ValorTotal}")



