# Função com 2 valores de retorno, a string 'mestres' e o inteiro 42
def lala():
  return 'mestres', 42

#Aqui o resultado da função permanece como tupla
resultado = lala()
print(resultado) # Saída: ('mestres', 42)
print(type(resultado)) # Saída: <class 'tuple'>

#Aqui o resultado da função é desmontado em variáveis
texto, numero = lala()
print(texto) # Saída: mestres
print(type(texto)) # Saída: <class 'str'>
print(numero) # Saída: 42
print(type(numero)) # Saída: <class 'int'>

# Aqui o primeiro valor retornado deve ser ignorado usando o '_'
_, numero = lala()
print(numero) # Saída: 42
