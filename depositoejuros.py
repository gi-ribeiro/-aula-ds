deposito_inicial = float(input("Digite o valor do deposito inicial: "))
taxa_juros = float(input("Digite a taxa de juros mensal (%):  "))

saldo = deposito_inicial 
total_juros = 0 

print("mes / saldo")

for mes in range (1,25):
    juros_mensal = saldo* taxa_juros
    saldo += juros_mensal 
    total_juros += juros_mensal
    print(f"{mes}/ R${saldo:.2f}")

print(f" total ganho com juros apos 24 meses: R${total_juros:.2f}")
