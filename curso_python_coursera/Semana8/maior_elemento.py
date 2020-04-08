print("Programa: Maior elemento da lista!")

def maior_elemento(lista):
    aux = 0
    tam = len(lista) - 1
    maiorValor = 0
    while aux <= tam:
        if maiorValor == 0:
            maiorValor = lista[aux]
        for item in lista:
            if item >= maiorValor:
                maiorValor = item
        aux = aux + 1
    return maiorValor

lista = [7,3987,100,10,456,34,33,1000,45,23546,150]
print(maior_elemento(lista))
