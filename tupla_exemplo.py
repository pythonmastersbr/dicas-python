tupla = (10, 20, 30)

#Tenta adicionar um elemento na tupla
#tupla.append(40) #Descomente para testar
# Erro: AttributeError: 'tuple' object has no attribute 'append'

# Tenta remover o elemento no índice zero
#del tupla[0] #Descomente para testar
# Erro: TypeError: 'tuple' object doesn't support item deletion

#Tenta remover e retornar elemento no índice 2
#a = tupla.pop(2) #Descomente para testar
# Erro: AttributeError: 'tuple' object has no attribute 'pop'

#Testa se o elemento 20 existe na tupla
print(20 in tupla)  # Saída: True

#Testa se o elemento 40 existe na tupla
print(40 in tupla) # Saída: False

# Tupla com tipos diferentes
tupla2 = (10, "mestres", 3.1415)
print(tupla2) # Saída: (10, 'mestres', 3.1415)
