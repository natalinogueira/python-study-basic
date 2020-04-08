n = int(input("Digite valor:"))
digitoAtual = 0
digitoAnterior = -1

while n > 0:
    digitoAtual = n % 10
    if digitoAnterior == digitoAtual:
        print("sim")
        break
    n = n // 10
    if digitoAnterior != digitoAtual and n == 0:
        print("não")
    digitoAnterior = digitoAtual
    
