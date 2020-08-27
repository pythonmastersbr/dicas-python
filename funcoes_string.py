texto = "aprendendo COM OS mestres"

# Testa se uma string começa com outra string
print(texto.startswith("aprendendo")) # Saída: True
print(texto.startswith("Texto")) # Saída: False

# Testa se uma string termina com outra string
print(texto.endswith("mestres")) # Saída: True
print(texto.endswith("Texto")) # Saída: False

# Converte uma string para letras minúsculas
print(texto.lower()) # Saída: aprendendo com os mestres

# Converte uma string para letras maiúsculas
print(texto.upper()) # Saída: APRENDENDO COM OS MESTRES

# Converte apenas a primeira letra para maíuscula,
# o resto permanece em minúsculas
print(texto.capitalize()) # Saída: Aprendendo com os mestres

# Converte a primeira letra de cada palavra para maíuscula
# o resto permanece em minúsculas
print(texto.title()) # Saída: Aprendendo Com Os Mestres

# Substitui parte do conteúdo de uma string por outro
print(texto.replace("OS mestres", "python masters"))
# Saída: Aprendendo COM python masters
