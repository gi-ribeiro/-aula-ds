preço = int(input("Digite o preço da mercadoria: "))
desconto = int(input("Digite o valor do desconto"))

valor_do_desconto = preço * desconto / 100

a_pagar = preço - valor_do_desconto
print(f"valor do desconto: R$ {valor_do_desconto:}")
print(f"preço a pagar: R$")
