print("Programa: Soma elementos da lista!")

def soma_elementos(lista):
    soma = 0
    for item in lista:
        soma = soma + item
    return soma

lista = [1,2,3,4,5]
print(soma_elementos(lista))
