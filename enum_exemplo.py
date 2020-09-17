from enum import Enum, IntEnum

#Define uma enumeração
class Cor(Enum):
	VERMELHO = 1
	VERDE = 2
	AZUL = 3

#Itera pelos membros do enum
for c in Cor:
	print(c) 

# Saída: Cor.VERMELHO 
# Cor.VERDE
# Cor.AZUL

c1 = Cor.VERMELHO
print(type(c1)) # Saída: <enum 'Cor'>
print(c1 == Cor.VERMELHO) # Saída: True
print(c1 == Cor.VERDE) # Saída: False

#Define uma enumeração que suporta comparação com inteiros
class Cor2(IntEnum):
	VERMELHO = 1
	VERDE = 2
	AZUL = 3

print(Cor.VERMELHO == 1) # Saída: False
print(Cor2.VERMELHO == 1) # Saída: True
