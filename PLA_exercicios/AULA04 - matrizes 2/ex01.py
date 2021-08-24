from operacoes import *

a = [[2,1],[-3,4]]
b = [[0,-1],[2,5]]
c = [[3,0],[6,1]]

#[A+(B-Ct)]*B

x = transposta(c)
y = subtrair(b,x)
z = somar(a,y)
res = multiplicar(z,b)
exibir(res)
