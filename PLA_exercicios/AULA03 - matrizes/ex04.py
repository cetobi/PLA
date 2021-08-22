a = [[1,-1,0],[2,3,4],[0,1,-2]]

def exibir(m):
    for linha in m:
       print(linha)

def transposta (matriz):
    t = []
    linA = len(matriz)
    colA = len(matriz[0])
    for i in range(linA):
        t.append([])
        for j in range(colA):
            f = matriz[j][i]
            t[i].append(f)
    return t

aT = transposta(a)

b = []
col = len(a[0])
for i in range(len(a)):
    linha = [0]*col
    b.append(linha)
    for j in range(len(a[0])):
        b[i][j] = a[i][j] + aT[i][j]

exibir(b)