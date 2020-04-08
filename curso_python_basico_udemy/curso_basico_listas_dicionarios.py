#LISTAS

lista=[1,2,3,4,"goiaba",5]
print(lista)
print(type(lista))

lista.append("banana")
print(lista)

lista.append(6)
print(lista)

print(lista.index(4))
print(lista.index(2))

lista.count(4)

lista.remove("banana")
print(lista)
lista.remove(6)
print(lista)

print(lista.reverse())


lista2=[1, 3, 5, 6, 7, 8,9, 23, 56, 78, 34]
print(lista2)
lista2.sort()
print(lista2)


######

lista_telefones={"josefina": 998980998,"clotilde":987875634, "marciano":978785412}
print(lista_telefones)
lista_telefones["evaristo"]=989897687
print(lista_telefones)

del lista_telefones["clotilde"]
print(lista_telefones)