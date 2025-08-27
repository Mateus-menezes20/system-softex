notas = []  # Lista vazia para armazenar as notas do aluno

qtd = int(input('Quantas notas deseja cadastrar para o aluno? '))  
# Pergunta ao usuário quantas notas o aluno terá e salva esse número em 'qtd'

# Cadastro das notas
for i in range(qtd):  # Loop que se repete 'qtd' vezes (quantidade de notas)
    nota = float(input(f'Digite a {i+1}ª nota do aluno: '))  
    # Pede a nota do aluno (convertida para número decimal com float)
    notas.append(nota)  
    # Adiciona a nota digitada à lista 'notas' na sequência digitada

# Calcular a soma das notas manualmente
soma = 0  # Variável que acumula o valor das notas
contador = 0  # Variável que conta quantas notas foram somadas
for n in notas:  # Percorre cada nota armazenada na lista 'notas'
    soma += n  # Adiciona o valor da nota à variável 'soma'
    contador += 1  # Soma 1 ao contador (para saber quantas notas foram lidas)

# Calcula a média
media = soma / contador  # Divide a soma das notas pelo total de notas
print(f'\nMédia do aluno: {media:.2f}')  
# Mostra a média com 2 casas decimais, pulando uma linha antes (\n)

# Situação do aluno (baseada na média final)
if media >= 6:  # Se a média for 6 ou maior
    situacao = 'Aprovado'  # Define situação como aprovado
elif media>= 5: # Caso contrário (Se a média for 5)
    situacao = 'recuperação'  # Define situação como recuperação
else:  # Caso contrário (média menor que 5)
    situacao = 'Reprovado'  # Define situação como reprovado

print(f'Situação do aluno: {situacao}')  
# Exibe a situação final do aluno (aprovado, recuperação ou reprovado)

#Autora: Ingrid