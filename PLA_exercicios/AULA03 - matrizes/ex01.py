def exibir(m):
    for linha in m:
       print(linha)

a = [[0,0],[0,0],[0,0]]

lin = len(a)
col = len(a[0])

for i in range(lin):
    for j in range(col):
        if i == j:
            a[i][j] = 1
        else:
            a[i][j] = i**2

exibir(a)