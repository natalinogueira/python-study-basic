print("Programa: Valores Primos!")
def primo(n):
    aux =  1
    restoDivisao = 1
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        aux = aux + 1#2
        restoDivisao = n % aux
        if restoDivisao == 0 and aux < n:
            return False
        elif restoDivisao == 0 and aux == n:
            return True


n = int(input("Informe valor > 1:"))
while n > 1:
    if primo(n):
        print(primo(n))
        print("Primo!")
        n = 0
    else:
        print(n," não é primo!")
        n = int(input("Informe valor > 1:"))
