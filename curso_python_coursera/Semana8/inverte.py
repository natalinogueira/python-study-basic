n = int(input("Digite um número:"))
lista = []
while n != 0:
    lista.append(n)
    n = int(input("Digite um número:"))

listaInversa = []
index = 0
aux = 1
while len(listaInversa) < len(lista):
    index = len(lista) - (len(lista) + aux)
    #print(index)
    listaInversa.append(lista[index])
    #print("tamanho", len(listaInversa))
    aux = aux + 1

for item in listaInversa:
    print(item)
