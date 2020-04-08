print("Programa: Fatores Primos")
n = int(input("Informe valor inteiro positivo:"))

fator = 2
multiplicidade = 0
while n > 1:
    while n % fator == 0:
        multiplicidade = multiplicidade + 1
        n = n / fator
    if multiplicidade != 0:
        print("fator",fator,"multiplicidade",multiplicidade)
    multiplicidade = 0
    fator = fator + 1
    
    
        
