n = int(input('insira o numero'))

i = 0
while (n/(10**i)>1):
    i += 1

#i = numero de algarismos

alg = i*[0]
t = 0
while (t < i):
    while(n%(10**(t+1)) != 0):
        n -= 1*(10**t)
        alg[t] += 1
    t +=1
print(alg)

resultado = True
c = 0
while c < (i/2):
    if (alg[c] != alg[(i-1)-c]):
        resultado = False
    c += 1

if (resultado == True):
    fala = 'é'
else:
    fala = 'não é'
print(f'seu número {fala} um palíndromo')