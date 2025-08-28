# controle_presenca.py

def controle_presenca():
    meses = [
        "FEVEREIRO", "MARÇO", "ABRIL", "MAIO", "JUNHO",
        "AGOSTO", "SETEMBRO", "OUTUBRO", "NOVEMBRO"
    ]

    total_dias = 0
    for mes in meses:
        qtd_dias = int(input(f"Digite a quantidade de presenças no mês de {mes}: "))
        total_dias += qtd_dias

    frequencia = total_dias * 0.75
    porcentagem = (frequencia / 200) * 100

    if frequencia >= 150:
        print("\n[APROVADO]")
        print(f"Quantidade de dias: {int(frequencia)} // Porcentagem: {int(porcentagem)}%")
    else:
        print("\n[REPROVADO]")
        print(f"Quantidade de dias: {int(frequencia)} // Porcentagem: {int(porcentagem)}%")

# Só executa se rodar diretamente este arquivo
if __name__ == "__main__":
    controle_presenca()
