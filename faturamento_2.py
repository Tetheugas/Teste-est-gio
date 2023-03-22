faturamento_mensal = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total_faturamento = sum(faturamento_mensal.values())

for estado, faturamento in faturamento_mensal.items():
    percentual = (faturamento / total_faturamento) * 100
    print(f"{estado}: {percentual:.2f}%")