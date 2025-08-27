from bd import conectar, criar_tabela

# Criar a tabela ao iniciar o programa
criar_tabela()

def cadastrar():
    print("\n=== CADASTRO DE ESTUDANTE ===")
    nome = input("Nome: ")
    nome_mae = input("Nome da mãe: ")
    nome_pai = input("Nome do pai: ")
    email = input("Email: ")
    idade = input("Idade: ")
    cpf = input("CPF: ")
    turma = input("Turma (1° ano / 2° ano / 3° ano): ")
    senha = input("Senha: ")
    confirmar = input("Confirmar senha: ")

    if senha != confirmar:
        print("⚠️ As senhas não conferem!")
        return

    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO estudantes (nome, nome_mae, nome_pai, email, idade, cpf, turma, senha)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (nome, nome_mae, nome_pai, email, idade, cpf, turma, senha))
        conn.commit()
        print("✅ Estudante cadastrado com sucesso!")
    except Exception as e:
        print(f"Erro ao cadastrar: {e}")
    finally:
        conn.close()

def login():
    print("\n=== LOGIN DE ESTUDANTE ===")
    email = input("Email: ")
    senha = input("Senha: ")

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM estudantes WHERE email=? AND senha=?", (email, senha))
    usuario = cursor.fetchone()
    conn.close()

    if usuario:
        print(f"✅ Bem-vindo(a), {usuario[1]}!")
    else:
        print("❌ Email ou senha incorretos.")

def menu():
    while True:
        print("\n=== MENU ===")
        print("1 - Cadastrar estudante")
        print("2 - Login")
        print("3 - Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            login()
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()