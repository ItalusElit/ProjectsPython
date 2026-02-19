# PRIMEIRO PROJECT EM PYTHON estudando lógica de repetição e cálculos financeiros
# criado por: Ítalo Gabriel

def calcular():
    print("="*35)
    print("   SIMULADOR DE JUROS COMPOSTOS")
    print("="*35)

# pegando os dados (usando float para aceitar centavos)
    capital = float(input("Quanto você quer investir inicialmente? R$ "))
    aporte = float(input("Qual será o aporte mensal? R$ "))
    taxa_anual = float(input("Qual a taxa de juros anual? (em %) "))
    tempo_anos = int(input("Por quantos anos vai deixar render? "))

# lógica para converter taxa anual em mensal (simplificada)
    taxa_mensal = (taxa_anual / 100) / 12
    meses = tempo_anos * 12
    saldo = capital

    print(f"\nCalculando rendimento para {meses} meses...")

# O "for" que faz a mágica acontecer mensalmente
    for mes in range(1, meses + 1):
        saldo += aporte # adiciona o dinheiro do mês
        saldo += saldo * taxa_mensal # aplica os juros sobre o montante atual
    
    print("-" * 35)
    print(f"RESULTADO APÓS {tempo_anos} ANOS:")
    print(f"Total acumulado: R$ {saldo:.2f}")
    print("-" * 35)
    print("Projeto de estudo - Engenharia de Software")

if __name__ == "__main__":
    calcular()