operador,A,B = input().split()
 
while operador != "0":
 
    A = int(A)
    B = int(B)
 
    if operador == "+":
        print(A + B)
    elif operador == "-":
        print(A - B)
    elif operador == "*":
        print(A * B)
    elif operador == "/":
        print (A // B, A % B)
    elif operador == ";":
        congruencia = [] 
        if A == B:
            print(0)
        else:
            if A > B:
                for x in range(1, (A - B) + 1):
                    if (A - B) % x == 0:
                        congruencia.append(x)
            if A < B:
                for x in range(1, (B - A) + 1):
                    if (B - A) % x == 0:
                        congruencia.append(x)
            print(*congruencia)
 
    operador,A,B = input().split()