print("1:--------------------")
for i in range(0,5):
    print("valor X = ",i)

print("2:--------------------")
nome="Natali"
for letra in nome:
    print(letra)
print("3:--------------------")
lista=["natali",29,"brasil"]
for valor in lista:
    print(valor)

print("4:-------------------")
num=15
while(num>0):
    print(num)
    num=num-1

print("5:-------------------")
num=20
while True:
    num=num-1
    print(num)
    if(num==2):
        break

print("6:-----------------")
num=10
while True:
    num=num-1
    if(num==4):
        continue
    if(num==2):
        break
print("7:-----------------")
num=10
while True:
    num=num-1
    if(num==4):
        continue
    print(num)
    if(num==2):
        break

print("8:------------------")
for i in range(0,5):
    pass
