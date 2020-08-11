#Cria um dicionário com 3 chaves: nome, idade e sexo
pessoa = {'nome': 'José', 'idade': 95, 'sexo':'M'}
print(pessoa) # Saída: {'nome': 'José', 'idade': 95, 'sexo': 'M'}
 
#Verifica o tipo da variável pessoa
print(type(pessoa)) # Saída: <class 'dict'>
 
#Obtém o valor da chave nome
print(pessoa['nome']) # Saída: José
print(pessoa.get('nome')) # Saída: José
 
#Tenta obter o valor da chave 'sobrenome'
#print(pessoa['sobrenome']) # Descomente para testar
# Erro: KeyError: 'sobrenome'
 
#Obtém o valor da chave 'sobrenome',
#porém como a chave não existe, usa o valor 'N/D'
print(pessoa.get('sobrenome', 'N/D')) # Saída: N/D
 
del pessoa['sexo'] # Remove a chave 'sexo' do dicionário
 
pessoa['pais'] = 'brasil' # Adiciona a chave pais
print(pessoa)
# Saída: {'nome': 'José', 'idade': 95, 'pais': 'brasil'}
 
#Verifica se a chave existe no dicionário
print('sexo' in pessoa) # Saída: False
print('idade' in pessoa) # Saída: True
