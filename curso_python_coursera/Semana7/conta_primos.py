print("Programa: Quantidade de Números Primos [2 até n]!")

def ehPrimo(x):
    fator = 2
    if x == 2:
        return True
    while (x % fator) != 0 and fator <= (x/2):
        fator = fator + 1
    if x % fator == 0:
        return False
    else:
        return True

def n_primos(x):
    n = 2
    listaPrimos = ""
    while n <= x:
        if ehPrimo(n):
            print(n, end=" ")
        n = n+ 1

x = int(input("Digite numéro maior que 2:"))
n_primos(x)
