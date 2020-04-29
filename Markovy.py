import numpy as np
k = int(input("K:"))
N = int(input("N:"))

File = open('gabo.txt', encoding='utf8').read()

modelo = File.split()
check = False
line = File[:k]
ju= len(line)
print(line[ju-1:])
if(line[ju-1:] == " "):
    check=True
    line = line[0:ju-1]
    
def hazpar(modelo):
    for i in range(len(modelo)-1):
        yield (modelo[i], modelo[i+1])
        
pares = hazpar(modelo)

dictP = {}

for palabra1, palabra2 in pares:
    if palabra1 in dictP.keys():
        dictP[palabra1].append(palabra2)
    else:
        dictP[palabra1] = [palabra2]
 
ppalabra = np.random.choice(modelo)

sw=True
ll=len(line)

while sw:
    
    if(line[ll-1] != ppalabra[0]):
        ppalabra = np.random.choice(modelo)  
    else:
        print("son iguales")
        sw=False

cMarkov = [ppalabra]

n_words = N

for i in range(n_words):
    cMarkov.append(np.random.choice(dictP[cMarkov[-1]]))

uuu=' '.join(cMarkov)
uuu = uuu[1:len(uuu)]

if check:
    cunt= line + uuu + " "
    print(cunt[:N])
else:
    cunt= line + uuu 
    print(cunt[:N])

