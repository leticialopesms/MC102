def leitura(texto):
    """Faz a leitura de um arquivo dado na entrada."""
    with open(texto, "r", encoding="utf-8") as arquivo:
        lista1 = []     # Lista que contém os valores de cada item do arquivo de notícia.
        dicionario = {}        # Dicionário relaciona a categoria do item com seu respectivo valor.
 
        for linha in arquivo:
            if ":" in linha:
                linha = linha.split(maxsplit=1)
                if len(linha) > 1:
                    info = linha[1].strip()
            else:
                info = linha.strip()
            lista1.append(info)
 
        noticia = []
        for j in range(6, len(lista1)):
            noticia.append(lista1[j])
 
        dicionario = {"nId": lista1[0],
                      "titulo": lista1[1],
                      "qtdLeitores": int(lista1[2]),
                      "qtdLeitoresFinal": int(lista1[3]),
                      "qtdCliques": int(lista1[4]),
                      "tempo": int(lista1[5]),
                      "noticia": noticia}
    return noticia, dicionario
 
 
def relatorio_individual(dicionario):
    """Cria um relatório individual para cada notícia."""
    nome_relatorio = "relatorio_" + dicionario["nId"] + ".txt"
    with open(nome_relatorio, "w", encoding="utf-8") as relatorio:
        relatorio.write("nId: " + dicionario["nId"] + "\n")
        relatorio.write("qtdLeitores: " + str(dicionario["qtdLeitores"]) + "\n")
        relatorio.write("qtdLeitoresFinal: " + str(dicionario["qtdLeitoresFinal"]) + "\n")
        relatorio.write("qtdCliques: " + str(dicionario["qtdCliques"]) + "\n")
        relatorio.write("tempo: " + str(dicionario["tempo"]))
 
 
def relatorio_final(A, B, C, D, E, F):
    """Cria um relatório final após a leitura de todas as notícias."""
    with open("relatorio_final.txt", "w", encoding="utf-8") as relatorio_f:
        relatorio_f.write(str(A) + "\n")
        relatorio_f.write(str(B) + "\n")
        relatorio_f.write(str(C) + "\n")
        relatorio_f.write(str(D) + "\n")
        relatorio_f.write(str(E) + "\n")
        relatorio_f.write(str(F))
 
 
def main():
    n = int(input())    # Número de arquivos a serem abertos.
 
    soma_leitores = 0
    maior_numero_leitores = 0
    maior_numero_leitores_final = 0
    soma_cliques = 0
    maior_tempo = 0
    soma_paragrafos = 0
 
    for x in range(n):
        txt = input()
        noticia, dic = leitura(txt)
 
        relatorio_individual(dic)
 
        # A
        soma_leitores += dic["qtdLeitores"]
        # B
        if dic["qtdLeitores"] > maior_numero_leitores:
            noticia_mais_leitores = dic["titulo"]
            maior_numero_leitores = dic["qtdLeitores"]
        # C
        if dic["qtdLeitoresFinal"] > maior_numero_leitores_final:
            noticia_mais_leitores_final = dic["titulo"]
            maior_numero_leitores_final = dic["qtdLeitoresFinal"]
        # D 
        soma_cliques += dic["qtdCliques"]
        # E
        if dic["tempo"] > maior_tempo:
            maior_tempo = dic["tempo"]
        # F
        soma_paragrafos += len(noticia)
 
    A = media_leitores = soma_leitores//n
    B = '"' + str(noticia_mais_leitores) + '"' + ' ' + str(maior_numero_leitores)
    C = '"' + str(noticia_mais_leitores_final) + '"' + ' ' + str(maior_numero_leitores_final)
    D = media_cliques = soma_cliques//n
    E = maior_tempo
    F = media_paragrafos = soma_paragrafos//n
 
    relatorio_final(A, B, C, D, E, F)
 
if __name__ == "__main__":
    main()