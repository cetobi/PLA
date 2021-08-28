from operacoes import *

a = [[2,1],[-3,4]]
b = [[0,-1],[2,5]]
c = [[3,0],[6,1]]

#(B+At)*C^-1(3*Bt)

d = transposta(a)
e = inversa2x2(c)
f = transposta(b)
g = somar(b,d)
h = UmMult(f,3)
i = multiplicar(g,e)
j = multiplicar(i,h)

exibir(j)
