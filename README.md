# Sistema Escolar

## Objetivo

Desenvolver um sistema de gerenciamento de alunos que permita o **cadastro de estudantes**, o **registro de notas de atividades e provas**, o **controle de presença** e o **cálculo de médias**. O sistema possibilita avaliar a situação do aluno (aprovado, recuperação ou reprovado) de forma automatizada e organizada.

---

## Funcionalidades

Após o login, o usuário poderá acessar as seguintes funcionalidades:

1. **Cadastro de estudantes**
   - Registro de informações como:
     - Nome completo
     - Nome da mãe e do pai
     - Email
     - Idade
     - CPF
     - Turma
     - Senha
   - Validação de dados, incluindo confirmação de senha e verificação de email duplicado.

2. **Controle de presença**
   - Registro da presença do aluno.
   - Cálculo da porcentagem de presença.
   - Exibição de relatório com a situação do aluno com base na frequência.

3. **Sistema de notas e listas**
   - Cadastro de notas de **atividades e provas** por disciplina.
   - Cálculo de média ponderada (atividades 40% e provas 60% por padrão).
   - Inclusão de **pontos extras**, caso existam.
   - Determinação automática da **situação do aluno**:
     - Aprovado
     - Recuperação
     - Reprovado
   - Armazenamento dos resultados em arquivo (`resultado_aluno.txt`) para histórico.

4. **Cálculo de média**
   - Possibilita calcular a média final do aluno com base nas notas cadastradas.
   - Exibição detalhada de notas, médias e situação por disciplina.

5. **Cadastro e visualização de notas unificado**
   - O aluno logado registra suas próprias notas.
   - Não é necessário digitar nome ou idade manualmente.
   - O sistema gera o relatório completo com médias e situação final.

---

## Fluxo do Sistema

1. **Menu Principal**
   - Cadastrar estudante
   - Login
   - Sair

2. **Menu do Aluno (após login)**
   - Controle de presença
   - Sistema de listas/antigas notas
   - Logout
   - Cadastrar e calcular notas (novo sistema integrado)

3. **Processo de notas**
   - Seleção da disciplina (Matemática, Português, Ciências)
   - Registro das 3 notas de atividades
   - Registro das 3 notas de provas
   - Inclusão de pontos extras (opcional)
   - Cálculo automático da média e situação
   - Armazenamento em arquivo e exibição na tela

---

## Tecnologias Utilizadas

- **Python 3.12**
- **SQLite** para armazenamento de dados de estudantes
- Arquivos de texto para registro de resultados
- Estrutura modular com arquivos separados para:
  - Cadastro de estudantes (`sistema_cadastro.py`)
  - Controle de presença (`controle_presenca.py`)
  - Registro e cálculo de notas (`notas_sistema.py`)
  - Registro de notas/notas antigas (`listas.py`)
  - Menus e integração (`main.py`)

---

## Benefícios

- Automação do cálculo de médias e controle de presença.
- Registro seguro e organizado de todas as informações do aluno.
- Fácil expansão para inclusão de novas disciplinas, pesos diferentes e relatórios detalhados.
- Integração direta entre login e cadastro de notas, garantindo que cada aluno registre apenas suas próprias informações.

## Fluxograma do sistema

![alt text](<Captura de tela 2025-08-28 094310.png>)