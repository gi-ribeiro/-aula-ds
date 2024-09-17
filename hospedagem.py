dias_hospedado = float(input("Digite a quantidade de dias hospedagem: "))

preco_por_dia = 100.0
dias_hospedado = 2
custo_total = (dias_hospedado * preco_por_dia) + (dias_hospedado * dias_hospedado)

print(f"O preço total a pagar é: R${custo_total:.2f}")
