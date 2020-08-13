def lala1(valor): 
  if valor:
    return valor 
  else:
    return None # Retorno explícito de None

def lala2(valor):
  if valor:
    return valor
  else:
    return # Retorno vazio explícito (bare return)

def lala3(valor):
  if valor:
    return valor
  # Retorno implícito

print(type(lala1(False))) # Saída: <class 'NoneType'>
print(type(lala2(False))) # Saída: <class 'NoneType'>
print(type(lala3(False))) # Saída: <class 'NoneType'>
