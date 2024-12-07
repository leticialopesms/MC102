def max(dicionario, valor_):
    '''Define o valor máximo de uma lista de acordo com a ancestralidade.'''
    lista = sorted(dicionario, key = dicionario.get)
 
    for x in dicionario:
        if x not in valor_:
            lista.remove(x)
 
    maximo = lista[-1]
    return maximo
 
 
def main():
    n = int(input())            # n = quantidade de espécies no cladograma.
 
    especie_id = {}             # Dicionário que relaciona a espécie com seu id.
    especie_caract = {}         # Dicionário que relaciona a espécie com uma lista de suas características.
 
    for i in range(n):
        entrada_especies = input().split("|")
        id, nome_especie, nome_cientifico = entrada_especies[0].split()
        caracteristicas = entrada_especies[1].split()
 
        especie = f"{nome_especie} {nome_cientifico}"
 
        especie_id[especie] = id
        especie_caract[especie] = caracteristicas
 
 
 
    m = int(input())            # m = quantidade de características.
 
    caract_pares = {}           # Dicionário que relaciona a característica da espécie a seus pares de proteínas.
    caract_ancestralidade = {}  # Dicionário que relaciona cada característica a sua ancestralidade.
    ancestralidade = []         # Lista de ancestralidade das características.
 
    for j in range(m):
        caracteristica = input()
        ancestralidade.append(caracteristica)
        fita1 = input()
        fita2 = input()
        tamanho_fita = len(fita1)
 
        lista_de_pares = []
 
        for k in range(tamanho_fita):
            pares = fita1[k] + fita2[k]
            lista_de_pares.append(pares)
        caract_pares[caracteristica] = lista_de_pares
 
        if j == 0:
            mais_ancestral = caracteristica
            pares_ancestrais = lista_de_pares
 
 
 
    for chave, valor in caract_pares.items(): 
        mutacoes = 0 
        for k in range(len(valor)): 
            if valor[k] > pares_ancestrais[k]: 
                mutacoes += 1 
        caract_ancestralidade[chave] = mutacoes 
    ancestralidade = sorted(caract_ancestralidade, key = caract_ancestralidade.get) 
  
  
  
    for j in range(m): 
        caracteristica = ancestralidade[j] 
        print("CARACTERÍSTICA:", caracteristica) 
  
        for chave, valor in especie_caract.items(): 
            if max(caract_ancestralidade, valor) == caracteristica: 
                print(especie_id[chave], chave) 
 
if __name__ == "__main__":
    main()