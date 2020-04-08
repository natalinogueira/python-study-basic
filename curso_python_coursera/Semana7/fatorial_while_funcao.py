def fatorial(n):
    fatorial = 1
    while n > 1:
        fatorial = fatorial * n
        n = n - 1
    return fatorial

n = 1
while n > 0:
    n = int(input("Informe valor positivo para cálculo de fatorial:"))
    if n < 0:
        print("Valor inválido!")
    else:
        print(fatorial(n))
