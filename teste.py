import pandas as pd

# Criando um DataFrame
dados = {
    "Nome": ["Ana", "Bruno", "Carlos", "Daniela"],
    "Idade": [22, 30, 28, 35],
    "Cidade": ["Florianópolis", "São Paulo", "Curitiba", "Porto Alegre"]
}

df = pd.DataFrame(dados)

# Exibindo o DataFrame
print("=== DataFrame Criado ===")
print(df)

# Informações do DataFrame
print("\n=== Informações ===")
print(df.info())

# Estatísticas das colunas numéricas
print("\n=== Estatísticas ===")
print(df.describe())

# Filtrando pessoas com idade maior ou igual a 30
print("\n=== Pessoas com 30 anos ou mais ===")
print(df[df["Idade"] >= 30])

# Adicionando uma nova coluna
df["Maior de Idade"] = df["Idade"] >= 18

print("\n=== DataFrame Atualizado ===")
print(df)

# Salvando em CSV
df.to_csv("dados.csv", index=False)

print("\nArquivo 'dados.csv' criado com sucesso!")

