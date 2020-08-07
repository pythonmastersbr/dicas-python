lista = [10, 20, 30]

lista.append(40) #Adiciona um elemento no final da lista
print(lista) # Saída: [10, 20, 30, 40]

del lista[0] # Remove o elemento no índice zero
print(lista) # Saída: [20, 30, 40]

a = lista.pop(2) #Remove e retorna o elemento no índice 2
print(a) # Saída: 40
print(lista) # Saída: [20, 30]

#Testa se o elemento 20 existe na lista
print(20 in lista)  # Saída: True

#Testa se o elemento 40 existe na lista
print(40 in lista) # Saída: False

# Lista com tipos diferentes
lista2 = [10, "mestres", 3.1415]
print(lista2) # Saída: [10, 'mestres', 3.1415]
