from operacoes import *

a = [[2,1],[-3,4]]
b = [[0,-1],[2,5]]
c = [[3,0],[6,1]]

#(B+At)*C^-1(3*Bt)

d = transposta(a)
e = inversa2x2(c)
f = transposta(b)
g = b+d

h = []
'''for n in range(len(b)):
    linha = [0]*len(b[0])
    for m in range(len(b[0])):
        h[n][m] = (f[n][m])*3'''

#i = multiplicar(g,e)
#j = multiplicar(i,h)

exibir(e)
