a = int(input("Informe valor de A:"))
b = int(input("Informe valor de B:"))
c = int(input("Informe valor de C:"))

import math 
delta = (b**2) - (4 * a * c)

if(delta < 0):
    print("esta equação não possui raízes reais")
elif(delta == 0):
    x = (-b) + math.sqrt(delta)/(2*a)
    print("a raiz desta equação é",x)
elif (delta > 0):
    x = (-b) + math.sqrt(delta)/(2*a)
    y = (-b) - math.sqrt(delta)/(2*a)
    if(x < y):
        print("as raízes da equação são",x,"e",y)
    else:
        print("as raízes da equação são",y,"e",x)



