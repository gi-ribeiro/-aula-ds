#atividede 3

#Vendas mensais

vendas_mensais = [120, 130, 140, 150, 160, 170, 160, 150, 140, 130, 120, 110]

def calcular_total_vendas (vendas):
    """Calcula o total de vendas no ano."""
    return sum(vendas)

def calcular_media_vendas (vendas):
"""Calcula a média mensal de vendas."""
return sum(vendas) / len(vendas)

def determinar_mes_maximo_venda (vendas):
"""Determina o mês com a máxima venda."""
max_venda max(vendas)
mes_maximo vendas.index(max_venda) + 1 # +1 para o indice começar em 1 return mes_maximo, max_venda

#Cálculos
total_vendas = calcular_total_vendas (vendas_mensais)
media_vendas = calcular_media_vendas (vendas_mensais)
mes_maximo, max_venda = determinar_mes_maximo_venda(vendas_mensais)

#Resultados

print("Total de vendas no ano: {total_vendas}")
print("Média mensal de vendas: {media_vendas:.2f}")
print(f"Mēs com a máxima venda: Mēs (mes_maximo} com {max_venda} unidades vendidas."
