def exibir(m):
    for linha in m:
       print(linha)

def transposta (matriz):
    t = []
    for i in range(len(matriz)):
        t.append([])
        for j in range(len(matriz[0])):
            f = matriz[j][i]
            t[i].append(f)
    return t

def multiplicar(A,B):
    C = []

    linA, colA = len(A), len(A[0])
    linB, colB = len(B), len(B[0])

    if (linA != linB and colA != colB):
        print("Matrizes não tem a mesma ordem.")
    else:
        for i in range(linA):
            C.append([])
            for j in range(colB):
                C[i].append(0)
                for k in range(colA):
                    C [i][j] += A[i][k]*B[k][j]                              

    return C

def somar(A,B):
    C = []
    linA, colA = len(A), len(A[0])
    linB, colB = len(B), len(B[0])

    if (linA != linB and colA != colB):
        print("Matrizes não tem a mesma ordem.")
    else:    
        for i in range(linA):
            linha = [0]*colA
            C.append(linha)
            for j in range(colA):
                C[i][j] = A[i][j] + B[i][j]

    return C

def oposta(M):
    op = []
    for i in range(len(M)):
        linha = [0]*len(M[0])
        op.append(linha)
        for j in range(len(M[0])):
            op[i][j] = -M[i][j]
    return op

def subtrair(A,B):
    return somar(A, oposta(B))

def mIdentidade(matriz):
    if (len(matriz) != len(matriz[0])):
        print("Matriz não quadrada.")
    else:
        A = []
        for i in range(len(matriz)):
            linha = [0]*len(matriz[0])
            A.append(linha)
            for j in range(len(matriz[0])):
                if i == j:
                    A[i][j] = 1
                else:   
                    A[i][j] += A[i][j]
        return A

def inversa2x2(matriz):
    if (len(matriz) != len(matriz[0])):
        print("Matriz não quadrada.")
    else:
        a = matriz[0][0]*matriz[1][1]
        b = matriz[0][1]*matriz[1][0]
        c = a - b
        M = []
        for i in range(len(matriz)):
            linha = [0]*len(matriz[0])
            M.append(linha)
            for j in range(len(matriz[0])):
                M[i][j] = float(matriz[i][j]/c)
        d = M[1][1]
        M[1][1] = M[0][0]
        M[0][0] = d
        M[0][1] = -M[0][1]
        M[1][0] = -M[1][0]
        return M

def UmMult(A,D):
    C = []
    linA, colA = len(A), len(A[0])
    B = []
    for i in range(linA):
        linha = [0]*colA
        B.append(linha)
        for j in range(colA):
            B[i][j] = D

    linB, colB = len(B), len(B[0])

    if (linA != linB and colA != colB):
        print("Matrizes não tem a mesma ordem.")
    else:
        for i in range(linA):
            C.append([])
            for j in range(colB):
                C[i].append(0)
                for k in range(colA):
                    C [i][j] += A[i][k]*B[k][j] 
    return C