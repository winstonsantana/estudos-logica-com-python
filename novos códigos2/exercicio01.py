# Inicializando uma lista de notas
notas = []

# Definindo a quantidade de notas que o usuário deseja inserir
quantidade_de_notas = int(input("Quantas notas você deseja inserir? "))

# Loop para coletar as notas
for i in range(quantidade_de_notas):
    nota = float(input(f"Insira a nota {i + 1}: "))
    notas.append(nota)  # Adiciona a nota à lista

# Calculando a média
soma = sum(notas)  # Soma todas as notas
media = soma / quantidade_de_notas  # Calcula a média

# Exibindo a média
print(f"A média das notas é: {media:.2f}")