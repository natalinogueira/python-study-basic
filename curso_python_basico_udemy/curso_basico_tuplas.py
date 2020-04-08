
#TUPLAS
#Isso é algo novo? TUPLA?
#Semelhante a lista, mas possui valores IMUTÁVEIS: Não podem ser alterados

tuplas=("du", "dudu", "edu")
print(len(tuplas))
print(tuplas)
print(tuplas[0])
print(tuplas[1])
print(tuplas[2])

print(tuplas[0:2])
print(len(tuplas))

print(tuplas+tuplas) # Concatenação de tuplas
print(tuplas*5) #Multiplicação tuplas

print("du" in tuplas)

lista=[1,2,"tais"]
print(lista)
tuplas2=tuple(lista) # Transformar lista em tupla
print(tuplas2)