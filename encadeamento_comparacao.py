x = 42

# 2 condições combinadas com 'and'
print(10 <= x and x <= 50) # Saída: True

# Condição encadeada
print(10 <= x <= 50) # Saída: True

print(10 <= x <= 40) # Saída: False
print(50 <= x <= 100) # Saída: False

# Função com retorno
def lala():
    print("Python")
    return 42

# Utilização da função na condição encadeada
# Note que a função é chamada 1 única vez e
# portanto, 'Python' é impresso apenas 1 vez
if 10 < lala() < 50: # Saída: python
    print("masters") # Saída: masters
