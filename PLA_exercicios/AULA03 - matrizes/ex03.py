from typing import Generic


a = [[0,3],[2,-5]]
b = [[-2,4],[0,-1]]
c = [[4,2],[-6,0]]

def matriz(a,b,c):
    d = []
    lin = len(a)
    col = len(a[0]) 
    for i in range(lin):
        d.append([])
        for j in range(col):
            e = a[i][j]+b[i][j]
            f = -4*c[i][j]
            g = e[i][j]*f[i][j]
            d.append(g)
    return d

print(matriz(a,b,c))
