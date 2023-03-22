import json

with open('dados.json', 'r') as f:
    faturamento = json.load(f)


menor_valor = faturamento[0]['valor']
maior_valor = faturamento[0]['valor']
soma_valores = 0
num_dias_com_faturamento_superior_a_media = 0


for dia in faturamento:
    valor = dia['valor']

    if valor < menor_valor:
        menor_valor = valor

    elif valor > maior_valor:
        maior_valor = valor

    soma_valores += valor


media_mensal = soma_valores / len([dia for dia in faturamento if dia['valor'] > 0])

# Percorrendo os valores de faturamento diário novamente
for dia in faturamento:
    if dia['valor'] > media_mensal:
        num_dias_com_faturamento_superior_a_media += 1

print("Menor valor de faturamento diário: R$ {:.2f}".format(menor_valor))
print("Maior valor de faturamento diário: R$ {:.2f}".format(maior_valor))
print("Número de dias com faturamento superior à média mensal: {}".format(num_dias_com_faturamento_superior_a_media))