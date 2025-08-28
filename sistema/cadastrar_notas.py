def cadastrar_notas(usuario):
    """
    Cadastra notas para o aluno logado.
    `usuario` é uma tupla com os dados do estudante (do login).
    """
    nome = usuario[1]  # Pega o nome do usuário logado
    idade = usuario[4]  # Pega a idade do usuário logado

    disciplinas = ["Matemática", "Português", "Ciências"]
    notas = {}

    print(f"\n=== Cadastro de notas para {nome} ===")

    for disciplina in disciplinas:
        print(f"\n--- {disciplina} ---")

        # Atividades
        atividades = []
        print("Digite as 3 notas de ATIVIDADES:")
        for i in range(3):
            nota = float(input(f"Atividade {i+1}: "))
            atividades.append(nota)

        # Provas
        provas = []
        print("Digite as 3 notas de PROVAS:")
        for i in range(3):
            nota = float(input(f"Prova {i+1}: "))
            provas.append(nota)

        notas[disciplina] = {
            "atividades": atividades,
            "provas": provas
        }

    # Pontos extras
    pontos_extras = float(input("Digite os pontos extras do aluno (0 se não houver): "))

    # Calcular médias e situação por disciplina
    medias = {}
    situacoes = {}
    for disc, dados in notas.items():
        media = (sum(dados["atividades"]) / len(dados["atividades"]) * 0.4) + \
                (sum(dados["provas"]) / len(dados["provas"]) * 0.6) + pontos_extras
        medias[disc] = media

        if media >= 7:
            situacao = "Aprovado"
        elif media >= 5:
            situacao = "Recuperação"
        else:
            situacao = "Reprovado"
        situacoes[disc] = situacao

    # Salvar em arquivo
    with open("resultado_aluno.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"Aluno: {nome}, Idade: {idade}, Pontos extras: {pontos_extras}\n")
        for disc in disciplinas:
            arquivo.write(f"  {disc} - Atividades: {notas[disc]['atividades']}, "
                          f"Provas: {notas[disc]['provas']}, "
                          f"Média: {medias[disc]:.2f}, Situação: {situacoes[disc]}\n")
        arquivo.write("\n")

    # Mostrar resultados na tela
    print(f"\n--- Resultado final de {nome} ---")
    for disc in disciplinas:
        print(f"{disc}:")
        print(f"  Atividades: {notas[disc]['atividades']}")
        print(f"  Provas: {notas[disc]['provas']}")
        print(f"  Média: {medias[disc]:.2f}")
        print(f"  Situação: {situacoes[disc]}")


def menu_notas(usuario):
    """
    Menu unificado para o aluno logado.
    """
    while True:
        print("\n=== SISTEMA DE NOTAS ===")
        print("1 - Cadastrar notas")
        print("2 - Voltar")
        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar_notas(usuario)
        elif opcao == "2":
            break
        else:
            print("Opção inválida!")
