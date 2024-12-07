import datetime
 
def insercao(dic, lista):
    """Insere uma quantidade de produtos no estoque."""
    produto_ = lista[1]
    qtd_ = int(lista[2])
    categoria_ = lista[3]
    preco_ = lista[4]
    vencimento_ = lista[5]
    dic[produto_] = [qtd_, categoria_, preco_, vencimento_]
    return dic
 
def remocao(dic, lista):
    """Remove, se possível, uma quantidade de produtos do estoque."""
    produto_ = lista[1]
    qtd_ = int(lista[2])
    # x = estoque[produto]
    if produto_ not in dic or qtd_ > dic[produto_][0]:
        print("ERROR")
    else:
        dic[produto_][0] -= qtd_
        print("SUCCESS")
    return dic
 
def venda(dic, lista, saldo):
    """Remove uma quantidade de produtos do
    estoque para a venda e retorna o saldo."""
    produto_ = lista[0]
    qtd_ = int(lista[1])
    preco_ = float(dic[produto_][2])
    dic[produto_][0] -= qtd_
    saldo += preco_ * qtd_
    return dic, saldo
 
def organizacao(dic):
    """Organiza o dicionário em ordem alfabética
    de acordo com as categorias."""
    dic_ordenado = {}
    for produto_ in dic:
        qtd_ = dic[produto_][0]
        categoria_ = dic[produto_][1]
        dic_ordenado[produto_, qtd_] = categoria_
    pares = sorted(dic_ordenado.items(), key=lambda x: x[1])
 
    dic_ordenado = {}
    for chave_valor in pares:
        tupla = chave_valor[0]
        categoria_ = chave_valor[1]
        dic_ordenado[tupla] = categoria_
    return dic_ordenado
 
def main():
    modo = input()
    estoque = {}
    saldo_atual = 0
 
    while modo != "0":
        N = int(input())    # Elementos a serem processados.
 
        if modo == "1": # ESTOQUE
            for i in range(N):
                entrada = input().split()
                operacao = entrada[0]
 
                if operacao == "0":
                    estoque = insercao(estoque, entrada)
 
                if operacao == "1":
                    estoque = remocao(estoque, entrada)
 
        if modo == "2": # CAIXA
            for j in range(N):
                entrada = input().split()
                estoque, saldo_atual = venda(estoque, entrada, saldo_atual)
 
 
        modo = input()
 
    # Verificação da data atual.
    data = input()
    dia_a = data[0:2]
    mes_a = data[2:4]
    ano_a = data[4:8]
    data_atual = datetime.date(int(ano_a), int(mes_a), int(dia_a))
 
    # Organização do estoque em ordem alfabética de categoria.
    estoque_ordenado = organizacao(estoque)
 
    # ESTOQUE
    print("* ESTOQUE")
    categorias_impressas = []
    for produto_qtd in estoque_ordenado:
        produto = produto_qtd[0]
        qtd = produto_qtd[1]
        categoria = estoque_ordenado[produto_qtd]
        if qtd > 0:
            if categoria not in categorias_impressas:
                print("- " + categoria)
                categorias_impressas.append(categoria)
            print(produto, qtd)
 
    # SALDO
    print("* SALDO " + f"{saldo_atual:.2f}")
 
    # REPOSICAO
    c = 0
    for produto in estoque:
        if estoque[produto][0] == 0:
            if c == 0:
                print("* REPOSICAO")
                c += 1
            print(produto)
 
    # PROMOCAO
    c = 0
    for produto in estoque:
        vencimento = estoque[produto][3]
        dia_v = vencimento[0:2]
        mes_v = vencimento[2:4]
        ano_v = vencimento[4:8]
        data_de_vencimento = datetime.date(int(ano_v), int(mes_v), int(dia_v))
        if data_de_vencimento - data_atual < datetime.timedelta(days=7):
            if estoque[produto][0] != 0:
                if c == 0:
                    print("* PROMOCAO")
                    c += 1
                print(produto)
 
if __name__ == "__main__":
    main()