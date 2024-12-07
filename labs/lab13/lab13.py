def prefixar(dic, raiz, obj, pasta_do_obj): 
    """Adiciona o nome de uma pasta raiz como prefixo do nome de cada arquivo 
    e subpasta, propagando essa mudança para o conteúdo das subpastas.""" 
    if pasta_do_obj not in dic: 
        return pasta_do_obj + "_" + obj 
    return prefixar(dic, raiz, pasta_do_obj, dic[pasta_do_obj]) + "_" + obj 
  
def main(): 
    pasta_raiz, n = input().split() 
    par = {} 
    for _ in range(int(n)): 
        objeto, pasta = input().split() 
        par[objeto] = pasta 
        print(prefixar(par, pasta_raiz, objeto, pasta)) 
  
if __name__ == "__main__": 
    main() 