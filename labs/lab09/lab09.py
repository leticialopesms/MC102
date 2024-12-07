l, a = input().split() 
l = int(l)          # l = largura 
a = int(a)          # a = altura 
  
n = int(input())    # n = quantidade de operações 
  
  
def matriz_original(altura): 
    '''Cria a matriz original a partir da entrada de n linhas.''' 
    matriz = [] 
    for _ in range(altura): 
        linha = input().split() 
        matriz.append(linha) 
    return matriz 
  
  
def criar_matriz(altura, largura, termo = ' '): 
    '''Cria uma matriz auxiliar para as operações.''' 
    matriz = [] 
    for i in range(altura): 
        matriz.append([]) 
        for _ in range(largura): 
            matriz[i].append(termo) 
    return matriz 
  
  
def selecao(matriz, x_selecao, y_selecao, largura, altura): 
    '''Determina a área selecionada.''' 
    matriz_selecionada = criar_matriz(altura, largura) 
  
    for i in range(altura): 
        for j in range(largura): 
            matriz_selecionada[i][j] = matriz[i + y_selecao][j + x_selecao] 
    return matriz_selecionada 
  
  
def rotacao(matriz, matriz_selecionada, x_selecao, y_selecao): 
    '''Rotaciona a matriz em 90° no sentido horário.''' 
    altura = len(matriz_selecionada) 
    largura = len(matriz_selecionada[0]) 
  
    matriz_nula = criar_matriz(altura, largura, termo = '000') 
    for i in range(altura): 
        for j in range(largura): 
            matriz[i + y_selecao][j + x_selecao] = matriz_nula[i][j] 
  
    matriz_rotacionada = criar_matriz(largura, altura) 
    for i in range(altura): 
        for j in range(largura): 
            matriz_rotacionada[j][(altura - 1) - i] = matriz_selecionada[i][j] 
  
    for i in range(largura): 
        for j in range(altura): 
            matriz[i + y_selecao][j + x_selecao] = matriz_rotacionada[i][j] 
    return matriz 
  
  
def copia(matriz, matriz_selecionada, y_copia, x_copia): 
    '''Faz uma cópia da área selecionada e a sobrepõe em outra área da matriz. 
    A área selecionada é preservada.''' 
    altura = len(matriz_selecionada) 
    largura = len(matriz_selecionada[0]) 
  
    for i in range(altura): 
        for j in range(largura): 
            matriz[i + y_copia][j + x_copia] = matriz_selecionada[i][j] 
    return matriz 
  
  
def recorte(matriz, matriz_selecionada, y_selecao, x_selecao, y_recorte, x_recorte): 
    '''Recorta a área selecionada e a sobrepõe em outra área da matriz. 
    A área selecionada passa a ter somente elementos nulos.''' 
    altura = len(matriz_selecionada) 
    largura = len(matriz_selecionada[0]) 
  
    matriz_nula = criar_matriz(altura, largura, termo = '000') 
    for i in range(altura): 
        for j in range(largura): 
            matriz[i + y_selecao][j + x_selecao] = matriz_nula[i][j] 
  
    for i in range(altura): 
        for j in range(largura): 
            matriz[i + y_recorte][j + x_recorte] = matriz_selecionada[i][j] 
    return matriz 
  
  
def espelhamento(matriz, matriz_selecionada, y_selecao, x_selecao, orientacao_de_espelhamento): 
    '''Espelha a área selecionada.''' 
    altura = len(matriz_selecionada) 
    largura = len(matriz_selecionada[0]) 
  
    if orientacao_de_espelhamento == 'h': 
        matriz_espelhada = [] 
        for linha in matriz_selecionada: 
            linha_espelhada = linha[::-1] 
            matriz_espelhada.append(linha_espelhada) 
  
    if orientacao_de_espelhamento == 'v': 
        matriz_espelhada = criar_matriz(altura, largura) 
        for i in range(altura): 
            linha = matriz_selecionada[(altura - 1) - i] 
            for j in range(largura): 
                elemento = linha[j] 
                matriz_espelhada[i][j] = elemento 
  
    for i in range(altura): 
        for j in range(largura): 
            matriz[i + y_selecao][j + x_selecao] = matriz_espelhada[i][j] 
    return matriz 
  
  
def imprimir(matriz): 
    '''Imprime a matriz na forma convencional.''' 
    for linha in matriz: 
        for i in range(len(linha)): 
            if i == len(linha) - 1: 
                print(linha[i]) 
            else: 
                print(linha[i], end=" ") 
  
  
# Criação da matriz original 
m = matriz_original(a) 
  
x, y = 0, 0 
l_ = len(m[0]) 
a_ = len(m) 
  
# Criação da matriz com a área selecionada inicial para as operações. 
area_selecionada = selecao(m, x, y, l_, a_) 
  
for _ in range(n): 
    operacoes = input().split() 
    op = operacoes[0] 
  
    if op.strip() == 'selecao': 
        x = int(operacoes[1]) 
        y = int(operacoes[2]) 
        l_ = int(operacoes[3]) 
        a_ = int(operacoes[4]) 
  
    if op.strip() == 'rotacao': 
        m = rotacao(m, area_selecionada, x, y) 
  
    if op.strip() == 'recorte': 
        x_recorte = int(operacoes[1]) 
        y_recorte = int(operacoes[2]) 
        m = recorte(m, area_selecionada, y, x, y_recorte, x_recorte) 
  
    if op.strip() == 'copia': 
        x_copia = int(operacoes[1]) 
        y_copia = int(operacoes[2]) 
        m = copia(m, area_selecionada, y_copia, x_copia) 
  
    if op.strip() == 'espelhamento': 
        orientacao = operacoes[1] 
        m = espelhamento(m, area_selecionada, y, x, orientacao) 
  
    area_selecionada = selecao(m, x, y, l_, a_) 
    operacoes = [] 
  
imprimir(m) 