def cria_matriz_original(n):
    """Cria a matriz original a partir da entrada de
    n linhas."""
    matriz = []
    for _ in range(n):
        linha = input().split()
        matriz.append(linha)
    return matriz
 
 
def cria_matriz(n, termo = '-'):
    """Cria uma matriz auxiliar para os cálculos dos
    determinantes."""
    matriz = []
    for i in range(n):
        matriz.append([])
        for _ in range(n):
            matriz[i].append(termo)
    return matriz
 
 
def det_laplace(matriz_original, n):
    """Calcula o determinante de uma matriz quadrada
    (n x n) pela Expansão de Laplace."""
    det = 0
    for k in range(n):
        elemento = int(matriz_original[0][k]) 
        matriz_reduzida = cria_matriz(n - 1) 
        j_ = 0 
        for j in range(n): 
            if j != k: 
                i_ = 0 
                for i in range(1, n): 
                    matriz_reduzida[i_][j_] = matriz_original[i][j] 
                    i_ += 1 
                j_ += 1 
        if len(matriz_reduzida) > 1:
            det += elemento * ((-1) ** (0 + k)) * det_laplace(matriz_reduzida, n - 1)
        else:
            det += elemento * ((-1) ** (0 + k)) * int(matriz_reduzida[0][0])
    return det
 
 
def main():
    m = int(input())    # Número de matrizes.
    n = int(input())    # Dimensão das matrizes quadradas (n x n).
 
    produto = 1
    for _ in range(m):
        matriz = cria_matriz_original(n)
        det = det_laplace(matriz, n)
        produto *= det
 
    saida = f"Após as {m} transformações, o objeto {n}-dimensional teve o volume multiplicado no valor {produto}."
    print(saida)
 
if __name__ == "__main__":
    main()