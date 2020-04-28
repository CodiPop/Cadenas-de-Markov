import numpy as np

abc = open('gabo.txt').read()


##k = int(input("K:"))
k=25
n = int(input("N:"))
line = abc[:k]
modelo = abc.split()

def h_pares(modelo):
    for i in range(len(modelo)-1):
        yield (modelo[i], modelo[i+1])
        
pares = h_pares(modelo)

Lkeys = {}

for palabra1, palabra2 in pares:
    if palabra1 in Lkeys.keys():
        Lkeys[palabra1].append(palabra2)
    else:
        Lkeys[palabra1] = [palabra2]

ppalabra = np.random.choice(modelo)

while ppalabra.islower():
    ppalabra = np.random.choice(modelo)

cMarkov = [ppalabra]

for i in range(k):
    cMarkov.append(np.random.choice(Lkeys[cMarkov[-1]]))

CADENA = ' '.join(cMarkov)
casiqueno=line + CADENA
##Muestra cadna generada
print(CADENA)
##Muestra line + la cadena generada con restriccion de longitud N
print(casiqueno[0:n])


