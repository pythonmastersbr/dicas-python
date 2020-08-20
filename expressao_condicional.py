# Função utilizando condições tradicionais
def teste_condicao(valor):
    if valor % 2 == 0:
        return 'par'
    return 'ímpar'

print(teste_condicao(0)) # Saída: par
print(teste_condicao(1)) # Saída: ímpar

# Função utilizando expressões condicionais,
# válido a partir do Python 2.5
def teste_expressao(valor):
    return 'par' if valor % 2 == 0 else 'ímpar'

print(teste_expressao(0)) # Saída: par
print(teste_expressao(1)) # Saída: ímpar

# Expressões condicionais suportam 'short-circuit',
# portanto a divisão por zero não é executada
print('lala' if True else 1/0) # Saída: lala
