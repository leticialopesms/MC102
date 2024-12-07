from decimal import Decimal
from recipes_decimal import pi
 
pi_ = pi()
 
def zeta(valor):
    """Define a função zeta."""
    z = 0
    for n in range(1, 101):
        z += 1 / (n ** valor)
    return z
 
def equacao(a, b, c, d, x):
    """Define a equação que relaciona a quantidade x de antimatéria
    necessaria para que o robô possa viajar y anos-luz."""
    numerador = pi_ + a * Decimal(x).exp() - zeta(b * x + pi_)
    denominador = Decimal(- (c * x) ** Decimal(1 / 2)).exp() + (d * (2 * (pi_ ** 3) - x))
    y = Decimal(numerador) / Decimal(denominador)
    return y
 
def busca_binaria(y, a, b, c, d):
    """Realiza a busca binária do valor de x
    com precisão de 32 casas decimais."""
    esquerda = Decimal(0.)
    direita = Decimal(50.)
    while abs(esquerda - direita) > Decimal(10.) ** Decimal(- 32):
        x = (esquerda + direita) / Decimal(2)
        m = equacao(a, b, c, d, x)
        if m < y:
            esquerda = x
        else:
            direita = x
    return x
 
 
def main():
    """Analisa o melhor dentre N saltos que o
    robô pode fazer, caso seja possível."""
    N = int(input())
 
    while N != 0:
        dic = {}
 
        for _ in range(N):
            nome_planeta = input()
            distancia_anos_luz = input()
            dic[nome_planeta] = distancia_anos_luz
 
        a = Decimal(input())
        b = Decimal(input())
        c = Decimal(input())
        d = Decimal(input())
 
        distancia_limite = equacao(a, b, c, d, Decimal(50.))
        maior_distancia = 0
 
        for planeta, distancia in dic.items():
            if Decimal(distancia) < Decimal(distancia_limite):
                if Decimal(distancia) > Decimal(maior_distancia):
                    maior_distancia = distancia
                    melhor_planeta = planeta
 
        if maior_distancia == 0:
            print("GRAU~~")
        else:
            resultado = busca_binaria(Decimal(maior_distancia), a, b, c, d)
            print(melhor_planeta)
            print(f"{resultado:.28f}")
 
        N = int(input())
 
 
if __name__ == main():
    main()