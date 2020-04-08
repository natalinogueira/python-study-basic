largura = int(input("Digite a largura:"))
altura = int(input("Digite a altura:"))
n = largura
m = altura
while altura > 0:
    while largura > 0:
        if altura == m:
            print("#", end='')
        elif altura == 1:
            print("#", end='')
        elif largura == n and altura > 1:
            print("#", end='')
        elif largura == 1:
            print("#", end='')
        else:
            print(" ", end='')
        largura = largura - 1
    print(end='\n')
    altura = altura - 1
    largura = n
