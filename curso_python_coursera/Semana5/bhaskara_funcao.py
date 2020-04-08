a = int(input("Informe valor de A:"))
b = int(input("Informe valor de B:"))
c = int(input("Informe valor de C:"))

delta = (b**2) - (4 * a * c)
raizes = 0

def raiz(delta):
    import math 
    if(delta < 0):
        return "Esta equação não possui raízes reais"
    elif(delta == 0):
        x = (-b) + math.sqrt(delta)/(2*a)
        return "A raiz desta equação é " + str(x)
    elif (delta > 0):
        x = (-b) + math.sqrt(delta)/(2*a)
        y = (-b) - math.sqrt(delta)/(2*a)
        if(x < y):
            return "As raízes da equação são " + str(x) + " e " + str(y)
        else:
            return "As raízes da equação são " + str(y) + " e " + str(x)


raizes = raiz(delta)
print(raizes)


