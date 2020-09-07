# Concatenamos manualmente as partes da string com o operador +
def exemplo1(nome, pronome):
	return "Olá " + nome + ", tudo bem com " + pronome + "?"

# Aqui usamos o operador % para substituir os 'placeholders' %s
def exemplo2(nome, pronome):
	return "Olá %s, tudo bem com %s?" % (nome, pronome)

#Aqui usamos placeholders nomeados e substituir
def exemplo3(nome, pronome):
	return "Olá %(n)s, tudo bem com %(pn)s?" \
	% {'n':nome, 'pn': pronome}

# Aqui usamos o format usando a estratégia de índices
def exemplo4(nome, pronome):
	return "Olá {0}, tudo bem com {1}?".format(nome, pronome)

# A partir do Python 3.6, f-strings permitem interpolação
def exemplo5(nome, pronome):
	return f"Olá {nome}, tudo bem com {pronome}?"

print(exemplo1("mestre", "você"))
# Saída: Olá mestre, tudo bem com você?

print(exemplo2("mestre", "você")) 
# Saída: Olá mestre, tudo bem com você?

print(exemplo3("mestre", "você"))
# Saída: Olá mestre, tudo bem com você?

print(exemplo4("mestre", "você"))
# Saída: Olá mestre, tudo bem com você?

print(exemplo5("mestre", "você"))
# Saída: Olá mestre, tudo bem com você?
