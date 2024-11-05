def soma_matrizes(A,B):
    linhas = len(A)
    colunas = len(A[0])
    C = [[0 for _ in  range (colunas)] for _ in range (linhas)] 

    for i in range(linhas):
        for j in range(colunas): 
            C[i] [j] = A[i] [j] + B[i] [j]

    return C    
