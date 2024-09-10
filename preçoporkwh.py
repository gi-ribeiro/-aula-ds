def calcular_preco(kwh_consumidos, tipo_instalacao):
    if tipo_instalacao == 'R':
        if kwh_consumidos <= 500:
            preco = kwh_consumidos * 0.40
        else:
            preco = kwh_consumidos * 0.65
    elif tipo_instalacao == 'C':
        if kwh_consumidos <= 1000:
            preco = kwh_consumidos * 0.55
        else:
            preco = kwh_consumidos * 0.60
    elif tipo_instalacao == 'I':
        if kwh_consumidos <= 5000:
            preco = kwh_consumidos * 0.55
        else:
            preco = kwh_consumidos * 0.60
    else:
        return "Tipo de instalação inválido."
        return f"Preço a pagar: R$ {preco:.2f}"

# Entrada de dados
kwh_consumidos = float(input("Digite a quantidade de kWh consumidos: "))
tipo_instalacao = input("Digite o tipo de instalação (R para Residências, C para Comércios, I para Indústrias): ").upper()

# Exibe o resultado
resultado = calcular_preco(kwh_consumidos, tipo_instalacao)
print(resultado)
