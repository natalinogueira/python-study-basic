x1 = int(input("Informe valor inteiro de x1:"))
y1 = int(input("Informe valor inteiro de y1:"))
x2 = int(input("Informe valor inteiro de x2:"))
y2 = int(input("Informe valor inteiro de y2:"))

import math
distancia = math.sqrt(((x2 - x1)**2) + ((y2 -y1)**2))
if (distancia >= 10):
    print("longe")
else:
    print("perto")
