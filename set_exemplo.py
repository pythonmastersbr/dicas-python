#Cria um conjunto com os elementos 1, 2, 3
conjunto = {1, 2, 3}

#Verifica o tipo da variável conjunto
print(type(conjunto)) # Saída: <class 'set'>

# Tenta adicionar o valor 100 no conjunto 2 vezes
conjunto.add(100)
conjunto.add(100)
print(conjunto) # Saída: {1, 2, 3, 100}
#Note que existe apenas um valor 100

# Remove um valor existente
conjunto.remove(100)
print(conjunto) # Saída: {1, 2, 3}

# Ao tentar remover um valor inexistente, 
# um erro será lançado
#conjunto.remove(4) #Descomente para testar
#Erro: KeyError: 4

#Se não tiver certeza que o elemento existe, 
#prefira usar o discard
conjunto.discard(4)
print(conjunto) # Saída: {1, 2, 3}

#Verifica se o valor existe no conjunto
print(4 in conjunto) # Saída: False
print(1 in conjunto) # Saída: True
