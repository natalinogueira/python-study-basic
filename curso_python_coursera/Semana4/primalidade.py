n = int(input("Digite um número inteiro:"))
aux = 1
restoDivisao = 1
primo = ""
while restoDivisao != 0:
    if n == 2:
        print("primo")
        restoDivisao = 0
    elif n % 2 == 0:
        restoDivisao = 0
        print("não primo")
    else:
        aux = aux + 1
        restoDivisao = n % aux
        if restoDivisao != 0 and aux < n:
            print("não primo")
            restoDivisao = 0
        elif restoDivisao == 0 and aux == n:
            print("primo")
            restoDivisao = 0
