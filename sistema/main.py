from bd import criar_tabela
from sistema_cadastro import cadastrar, login
from controle_presenca import controle_presenca
from listas import menu_listas_notas
from cadastrar_notas import menu_notas  # Novo sistema unificado

def menu_principal():
    criar_tabela()
    while True:
        print("\n=== SISTEMA ESCOLAR ===")
        print("1 - Cadastrar estudante")
        print("2 - Login")
        print("3 - Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            usuario = login()
            if usuario:
                menu_usuario(usuario)
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("⚠️ Opção inválida!")

def menu_usuario(usuario):
    while True:
        print(f"\n=== MENU DO ALUNO ({usuario[1]}) ===")
        print("1 - Controle de presença")
        print("2 - Sistema de listas/antigas notas")  # Caso queira manter
        print("3 - Logout")
        print("4 - Cadastrar e calcular notas")  # Novo sistema integrado
        opcao = input("Escolha: ")

        if opcao == "1":
            controle_presenca()
        elif opcao == "2":
            menu_listas_notas()
        elif opcao == "3":
            print("✅ Logout realizado.")
            break
        elif opcao == "4":
            menu_notas(usuario)
        else:
            print("⚠️ Opção inválida!")

if __name__ == "__main__":
    menu_principal()
