print("Programa: Remove elementos repetidos!")

def remove_repetidos(lista):
    aux = 0
    tam = len(lista) - 1
    while aux <= tam:
        valorRepetido = 0
        for item in lista:
            if item == lista[aux]:
                valorRepetido = valorRepetido + 1
        if valorRepetido > 1:
            del lista[aux]
        novoTamLista = len(lista) - 1
        aux = aux + 1
        if novoTamLista != tam:
            tam = novoTamLista
            aux = aux - 1
    return sorted(lista)

lista = [7,3,33,12,3,3,3,7,12,100]
print(remove_repetidos(lista))

