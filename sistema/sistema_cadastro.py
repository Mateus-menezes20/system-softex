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

    # Verificar se o email já existe
    cursor.execute("SELECT * FROM estudantes WHERE email=?", (email,))
    if cursor.fetchone():
        print("⚠️ Este e-mail já está cadastrado!")
        conn.close()
        return

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
        return usuario  # Retorna o usuário para o menu principal
    else:
        print("⚠️ Email ou senha incorretos.")
        return None
