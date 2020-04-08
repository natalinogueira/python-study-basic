def maior_primo(x):
    primo = Primo(x)
    if primo == True:
        return x
    else:
        while x >= 2:
            x = x - 1
            primo = Primo(x)
            if primo == True:
                return x
        return x
        

def Primo(k):
    aux =  1
    restoDivisao = 1
    primo = 0
    while restoDivisao != 0:
        if k == 2:
            return True
        elif k % 2 == 0:
            restoDivisao = 0
            return False
        else:
            aux = aux + 1
            restoDivisao = k % aux
            if restoDivisao == 0 and aux < k:
                return False
            elif restoDivisao == 0 and aux == k:
                return True


#print(maior_primo(8))
#print(maior_primo(7))
#print(maior_primo(100))
