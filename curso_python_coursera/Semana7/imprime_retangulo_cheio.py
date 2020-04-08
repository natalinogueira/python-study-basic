largura = int(input("Digite a largura:"))
altura = int(input("Digite a altura:"))
n = largura
while altura > 0:
    altura = altura - 1
    while largura > 0:
        print("#", end='')
        largura = largura - 1
    print(end='\n')
    largura = n
