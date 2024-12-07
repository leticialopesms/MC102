q = int(input())
if 1 <= q <= 100: 
    T = float(input()) 
    if 0.01 <= T <= 1.00: 
        C = int(input())  
        if 0 <= C <= 1000: 
            n = int(input()) 
            if 1 <= n <= 100: 
                Vp = 0
                for i in range(1, q + 1):
                    Vi = T * i + T * C
                    Vp += Vi
                    print(i, f"{Vi:.2f}", f"{Vp:.2f}")
                Vt = Vp
                print(f"{Vt:.2f}")
 
                m = 0
                while (m + 1) * n <= Vt:
                    PAn = (m + 1) * n
                    m += 1
                    print(PAn)
                print(m)
                print("BATERIA DE TESTES TERMINADA")