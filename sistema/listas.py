# listas_notas.py

def registrar_resultado_3_notas():
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    media = (nota1 + nota2 + nota3) / 3
    situacao = "Aprovado" if media >= 7 else "Reprovado"

    print(f"\nAluno: {nome}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")

    with open("resultado_aluno.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"Aluno: {nome} | Média: {media:.2f} | Situação: {situacao}\n")


def calcular_media():
    nome = input("Nome do aluno: ")
    qtd = int(input("Quantas notas deseja cadastrar? "))
    notas = []
    for i in range(qtd):
        nota = float(input(f"Digite a nota {i+1}: "))
        notas.append(nota)

    pontos_extras = float(input("Digite os pontos extras (0 se não houver): "))
    media = (sum(notas) / len(notas)) + pontos_extras

    print(f"\nAluno: {nome}")
    print(f"Notas: {notas}")
    print(f"Pontos extras: {pontos_extras}")
    print(f"Média final: {media:.2f}")

    situacao = "Aprovado" if media >= 7 else "Reprovado"
    print(f"Situação: {situacao}")

    with open("resultado_aluno.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"Aluno: {nome} | Notas: {notas} | Extras: {pontos_extras} | Média: {media:.2f} | Situação: {situacao}\n")


def menu_listas_notas():
    while True:
        print("\n=== SISTEMA DE LISTAS/NOTAS ===")
        print("1 - Registrar 3 notas")
        print("2 - Calcular média com extras")
        print("3 - Voltar")
        opcao = input("Escolha: ")

        if opcao == "1":
            registrar_resultado_3_notas()
        elif opcao == "2":
            calcular_media()
        elif opcao == "3":
            break
        else:
            print("Opção inválida!")

# Só executa se rodar diretamente este arquivo
if __name__ == "__main__":
    menu_listas_notas()
