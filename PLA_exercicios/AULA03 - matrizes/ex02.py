def exibir(m):
    for linha in m:
       print(linha)

a = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]

lin = len(a)
col = len(a[0])

for i in range(lin):
    for j in range(col):
        if i == j:
            a[i][j] = i + j
        else:
            a[i][j] = (2*i)*(-2*j)


b = a[1][1]
c = a[2][3]
res = b + c
exibir(a)
print("\n")
print(b," + ",c," = ",res)