texto = "  Aprendendo com os mestres  "

# Determina o comprimento de um string
print(len(texto)) # Saída: 29

# Divide a string retornando uma lista
# Por padrão o separador é espaço
print(texto.split())
# Saída: ['Aprendendo', 'com', 'os', 'mestres']

# Conta as ocorrências de uma substring
print(texto.count("os")) # Saída: 1

# Remove espaços vazios no ínicio e final da substring
print(texto.strip()) # Saída: Aprendendo com os mestres

# Retorna o índice de ínicio uma substring
print(texto.find("mestres")) # Saída: 20

# Retorna -1 se não encontrar
print(texto.find("masters")) # Saída: -1

# Retorna o índice de ínicio uma substring
print(texto.index("mestres")) # Saída: 20

# Lança uma exceção se não encontrar
print(texto.index("masters"))
# ERRO: ValueError: substring not found
