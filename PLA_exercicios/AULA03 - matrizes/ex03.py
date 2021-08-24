#a+b-4*c

a = [[0,3],[2,-5]]
b = [[-2,4],[0,-1]]
c = [[4,2],[-6,0]]

def exibir(m):
    for linha in m:
        print(linha)

linA = len(a)
colA = len(a[0])

d = []
for i in range(linA):
    linha = [0]*colA
    d.append(linha)      
    for j in range(colA):
        d[i][j] = a[i][j] + b[i][j]


e = []
for i in range(linA):
    linha = [0]*colA
    e.append(linha)
    for j in range(colA):
        e[i][j] = -4*c[i][j]


f = []
for i in range(linA):
    linha = [0]*colA
    f.append(linha)
    for j in range(colA):
        f[i][j] = d[i][j]*e[i][j]


exibir(f)