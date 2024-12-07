if __name__ == "__main__":
    fotos = input().split("/ ")
    erro = fotos[-1]
    fotos = fotos[0].split(", ")
 
''' Observação de correção
    Uso do __name__:
    A ideia é que tudo o que está fora do "if name == 'main'" seja declarado em forma de função e
    classe, assim essa sfunções podem ser chamadas no if, deixando o código mais limpo e organizado.
'''

l1 = [] # l1 representa uma lista intermediária. 
        # Serve apenas para auxiliar na comparação entre a quantidade de repetições na lista. 
  
l2 = [] # l2 contém o elemento que mais se repete de forma consecutiva na lista. 
        # A lista é composta por um mesmo elemento repetido n vezes. 
  
lista = [fotos[0]] 
contador = 0 
for i in range(len(fotos) - 1): 
    if fotos[contador] == fotos[contador + 1]: 
        if l1 == []: 
            l1.append(fotos[contador]) 
        l1.append(fotos[contador + 1]) 
    else: 
        l1 = [] 
        if fotos[contador + 1] not in lista: 
            lista.append(fotos[contador + 1]) 
    if len(l1) > len(l2): 
        l2 = [] 
        for j in l1: 
            l2.append(j) 
    contador += 1 
  
n = len(l2) 
print(l2[0], n) 
print(len(lista)) 
  
nova_lista = lista 
for p in lista: 
    if p == erro: 
        while p in nova_lista: 
            nova_lista.remove(p) 
 
 
def hifen(titulo):
    novo_titulo = titulo.replace(" ", "-")
    return novo_titulo
 
def minusculas(titulo):
    if titulo is not None:
        lista_dupla = titulo.split("_")
 
        categoria = lista_dupla[0]
        minuscula = lista_dupla[1].lower()
        novo_titulo = str(categoria) + "_" + str(minuscula)
        return novo_titulo
 
 
HA_ = []
CR_ = []
CC_ = []
 
for k in nova_lista:
    k_formatado = minusculas(hifen(k))
    if k.startswith("HA_"):
        HA_.append(k_formatado)
    if k.startswith("CR_"):
        CR_.append(k_formatado)
    if k.startswith("CC_"):
        CC_.append(k_formatado)
 
print(HA_)
print(CR_)
print(CC_)