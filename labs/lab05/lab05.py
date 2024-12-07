vida_s,ataque_s,defesa_s = input().split() 
  
vida_s = int(vida_s)        # vida_s = pontos de vida de Sarah 
ataque_s = int(ataque_s)    # ataque_s = pontos de ataque de Sarah 
defesa_s = int(defesa_s)    # defesa_s = pontos de defesa de Sarah 
  
vida_c,ataque_c,defesa_c = input().split() 
  
vida_c = int(vida_c)        # vida_c = pontos de vida iniciais do clone 
ataque_c = int(ataque_c)    # ataque_c = pontos de ataque iniciais do clone 
defesa_c = int(defesa_c)    # defesa_c = pontos de defesa iniciais do clone 
  
x = int(input()) 
# Esse 'x' dado na entrada corresponde à semente a ser usada na função 'gerador_de_numeros'. 
  
def gerador_de_numeros(): 
    '''Gera números pseudo-aleatórios em cada rodada a partir do valor anterior de x.''' 
    global x 
    x = (7 * x + 111) % 1024 
    print("MENSAGEM DEBUG - número gerado:", x) 
  
def fim(vida): 
    '''Verifica se a partida chegou ao fim ou não.''' 
    if vida <= 0: 
        return True 
    return False 
  
def vez_de_atacar(): 
    '''Identifica o atacante e o atacado em cada rodada.''' 
    if rodada % 2 != 0: 
        global atacante 
        atacante = "Sarah" 
        global atacado 
        atacado = "O clone" 
    else: 
        atacante = "O clone" 
        atacado = "Sarah" 
  
def soco(): 
    '''Calcula o dano causado pela habilidade soco.''' 
    m = x % 3 

    if atacante == "Sarah": 
        if ataque_s < defesa_c: 
            dano = 0 
        else: 
            dano = (ataque_s - defesa_c) * m 
            global vida_c 
            vida_c -= dano 
  
    if atacante == "O clone": 
        if ataque_c < defesa_s: 
            dano = 0 
        else: 
            dano = (ataque_c - defesa_s) * m 
            global vida_s 
            vida_s -= dano 
  
    print(atacado, "sofreu", dano, "pontos de dano!") 
  
def arremesso_de_facas(): 
    '''Calcula o dano causado pela habilidade arremesso de facas.''' 
    n = x % 6 
  
    dano = 0 
  
    for i in range(1, n + 1): 
        dano_i = 0 
        if atacante == "Sarah": 
            dano_i = ataque_s // 3 ** i 
            dano += dano_i 
        if atacante == "O clone": 
            dano_i = ataque_c // 3 ** i 
            dano += dano_i 
  
    if atacante == "Sarah": 
        global vida_c 
        vida_c -= dano 
    if atacante == "O clone": 
        global vida_s 
        vida_s -= dano 
  
    print(atacado, "sofreu", dano, "pontos de dano!") 
  
def invocacao_de_fada(): 
    '''Calcula a cura recebida e os efeitos da habilidade invocação de fada.''' 
    global x 
    p = x % 100 
  
    gerador_de_numeros() 
  
    q = x 
  
    # Parte 1: verifica a cura recebida. 
    if atacante == "Sarah": 
        global vida_s 
        vida_s += p 
    if atacante == "O clone": 
        global vida_c 
        vida_c += p 
  
    print(atacante, "ganhou", p, "pontos de vida!") 
  
    # Parte 2: verifica o ataque ou a defesa incrementados. 
    if q < 100 and q % 2 != 0: 
        if atacante == "Sarah": 
            global ataque_s 
            ataque_s += q 
        if atacante == "O clone": 
            global ataque_c 
            ataque_c += q 
        print(atacante, "ganhou", q, "pontos de ataque!") 
  
    if q < 100 and q % 2 == 0 and q != 0: 
        if atacante == "Sarah": 
            global defesa_s 
            defesa_s += q 
        if atacante == "O clone": 
            global defesa_c 
            defesa_c += q 
        print(atacante, "ganhou", q, "pontos de defesa!") 
  
    # Parte 3: verifica se o monstro invadiu, ou não, o castelo. 
    if q >= 1019: 
        if atacante == "Sarah": 
            vida_c = 0 
            sarah_ganhou = """O quê? A fada trouxe um monstro gigante com ela! 
                            O Clone e o castelo foram destruídos, 
                            e Sarah agora tem um novo pet. 
                            FINAL SECRETO - PARABENS???""" 
            print(sarah_ganhou) 
  
        if atacante == "O clone": 
            vida_s = 0 
            clone_ganhou = """O quê? A fada trouxe um monstro gigante com ela! 
                            Sarah foi derrotada...""" 
            print(clone_ganhou) 
  
        global monstro 
        monstro = True 
  
monstro = False     # Situação inicial da variável 'monstro'. 
  
rodada = 1 
  
while not fim(vida_s) and not fim(vida_c): 
    gerador_de_numeros() 
    vez_de_atacar() 
  
    habilidade = input() 
    if habilidade == "soco": 
        soco() 
    if habilidade == "facas": 
        arremesso_de_facas() 
    if habilidade == "fada": 
        invocacao_de_fada() 
  
    rodada += 1 
  
if not monstro: 
    if vida_s <= 0: 
        print("Sarah foi derrotada...") 
    if vida_c <= 0: 
        print("O clone foi derrotado! Sarah venceu!") 
        print("FIM - PARABENS") 