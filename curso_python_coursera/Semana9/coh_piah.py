'''4.79 - Tamanho médio de palavra: Média simples do número de caracteres por palavra.
    Tamanho médio de palavra é a soma dos tamanhos das palavras dividida pelo número total de palavras.
    Exemplo: "O gato caçava o rato" (1+4+6+1+4)/5= 3.2 - sum(len(palavra))/Total_palavras
   ================================================================================================================
   0.72 - Relação Type-Token: Número de palavras diferentes utilizadas em um texto divididas pelo total de palavras.
   Relação Type-Token é o número de palavras diferentes dividido pelo número total de palavras.
   Por exemplo, na frase "O gato caçava o rato", temos 5 palavras no total (o, gato, caçava, o, rato)
   mas somente 4 diferentes (o, gato, caçava, rato).
   Nessa frase: O gato caçava o rato, a relação Type-Token vale 4/5=0.8
   ================================================================================================================
   0.56 - Razão Hapax Legomana: Número de palavras utilizadas uma vez dividido pelo número total de palavras.
   Razão Hapax Legomana é o número de palavras que aparecem uma única vez dividido pelo total de palavras.
   Por exemplo, na frase "O gato caçava o rato", temos 5 palavras no total (o, gato, caçava, o, rato)
   mas somente 3 que aparecem só uma vez (gato, caçava, rato).
   Nessa frase "O gato caçava o rato", a relação Hapax Legomana vale 3/5=0.6
   ================================================================================================================
   80.5 - Tamanho médio de sentença: Média simples do número de caracteres por sentença.
   Tamanho médio de sentença é a soma dos números de caracteres em todas as sentenças dividida pelo número de sentenças
   (os caracteres que separam uma sentença da outra NÃO devem ser contabilizados como parte da sentença).
    Ex:sum(caractere todas as sentenças)/total de sentenças
   ================================================================================================================
   2.5 - Complexidade de sentença: Média simples do número de frases por sentença.
   Complexidade de sentença é o número total de frases divido pelo número de sentenças.
    Ex: Total frases/ total de sentenças
   ================================================================================================================
   31.6 - Tamanho médio de frase: Média simples do número de caracteres por frase.
   Tamanho médio de frase é a soma do número de caracteres em cada frase dividida pelo número de frases no texto
   (os caracteres que separam uma frase da outra não devem ser contabilizados como parte da frase).
    Ex: sum(caracteres) cada frase/total frases.
   ================================================================================================================'''

'''Após calcular esses valores para cada texto, você deve comparar com a assinatura fornecida para os infectados por COH-PIAH.
    O grau de similaridade entre dois textos, a e b, é dado pela fórmula:'''

#import unicodedata
#from unicodedata import normalize
import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e
        devolve uma assinatura a ser comparada com os textos fornecidos'''

    print("Bem-vindo ao detector automático de COH-PIAH.")
    #Valores dos traços linguisticos do Modelo a ser comparado:
    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal] 

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")
    return textos


def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas
        dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e
    devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e
    devolve uma lista das palavras dentro da frase'''
    return frase.split()


def n_palavras_unicas(lista_palavras):
     '''Essa funcao recebe uma lista de palavras e
        devolve o numero de palavras que aparecem uma unica vez'''
     freq = dict()
     unicas = 0
     for palavra in lista_palavras:
         p = palavra.lower()
         if p in freq:
             if freq[p] ==1:
                 unicas -= 1
             freq[p] +=1
         else:
             freq[p] = 1
             unicas += 1
     return unicas


def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e
    devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] +=1
        else:
            freq[p] = 1
    return len(freq)

def total_palavras(texto):
    somaPalavras = 0
    lista_sentencas = separa_sentencas(texto)
    for setenca in lista_sentencas:
        lista_frases = separa_frases(setenca)
        for frase in lista_frases:
            lista_palavras = separa_palavras(frase)
            somaPalavras += len(lista_palavras)
    #print("somaPalavras =",somaPalavras)
    return somaPalavras

def calcula_tamanho_medio_palavra(texto):
    somaLetras = 0
    somaPalavras =  total_palavras(texto)
    lista_sentencas = separa_sentencas(texto)
    for setenca in lista_sentencas:
        lista_frases = separa_frases(setenca)
        for frase in lista_frases:
            lista_palavras = separa_palavras(frase)
            for palavra in lista_palavras:
                somaLetras += len(palavra)
    #print()
    #print("somaPalavras =", somaPalavras)
    #print("somaLetras =", somaLetras)
    return somaLetras/somaPalavras


def calcula_relacao_type_token(texto):
    total_palavras_diferentes = 0
    listaTotalPalavras = []
    totalPalavras = total_palavras(texto)
    lista_sentencas = separa_sentencas(texto)
    for setenca in lista_sentencas:
        lista_frases = separa_frases(setenca)
        for frase in lista_frases:
            lista_palavras = separa_palavras(frase)
            for palavra in lista_palavras:
                listaTotalPalavras.append(palavra)
            
    total_palavras_diferentes = n_palavras_diferentes(listaTotalPalavras)
    #print("listaTotalPalavras:", listaTotalPalavras)

    #print("total_palavras_diferentes =",total_palavras_diferentes)
    #print("total_palavras =",totalPalavras)
    return total_palavras_diferentes/totalPalavras

def calcula_razao_hapax_legomana(texto):
    total_palavras_unicas = 0
    listaTotalPalavras = []
    totalPalavras = total_palavras(texto)
    lista_sentencas = separa_sentencas(texto)
    for setenca in lista_sentencas:
        lista_frases = separa_frases(setenca)
        for frase in lista_frases:
            lista_palavras = separa_palavras(frase)
            for palavra in lista_palavras:
                listaTotalPalavras.append(palavra)
    total_palavras_unicas = n_palavras_unicas(listaTotalPalavras)
    #print("listaTotalPalavras:", listaTotalPalavras)

    #print("total_palavras_unicas =",total_palavras_unicas)
    #print("total_palavras =",totalPalavras)
    return total_palavras_unicas/totalPalavras

def calcula_tamanho_medio_sentenca(texto):
    lista_sentencas = separa_sentencas(texto)
    somaSentencas = 0
    qtdeSetencas = 0
    for setenca in lista_sentencas:
        #print()
        #print("[",setenca,"]")
        somaSentencas += len(setenca)
        qtdeSetencas += 1
    #print()                   
    #print("somaSentencas =", somaSentencas)
    #print("qtdeSetencas =", qtdeSetencas)
    return somaSentencas/qtdeSetencas

def calcula_total_setencas(texto):
    somaSentencas = 0
    lista_sentencas = separa_sentencas(texto)
    for setenca in lista_sentencas:
        #print(len(setenca))
        somaSentencas += 1
    #print("somaSentencas =", somaSentencas)
    return somaSentencas

def calcula_total_frases(texto):
    lista_sentencas = separa_sentencas(texto)
    somaFrases = 0
    for sentenca in lista_sentencas:
        #print("sentenca:",sentenca)
        lista_frases = separa_frases(sentenca)
        for frase in lista_frases:
            #print(len(frase))
            somaFrases += 1

    #print("somaFrases =", somaFrases)
    return somaFrases

def calcula_complexidade_media_sentenca(texto):
    #Ex: Total frases/ total de sentenças
    #print(texto)
    somaSentencas = calcula_total_setencas(texto)
    somaFrases = calcula_total_frases(texto)
    #print("somaSentencas =", somaSentencas)
    #sprint("somaFrases =", somaFrases)
    return somaFrases/somaSentencas

def calcula_tamanho_medio_frase(texto):
    #Ex: sum(caracteres) cada frase/total frases.
    total_frases = calcula_total_frases(texto)
    lista_sentencas = separa_sentencas(texto)
    somaFrases = 0
    for sentenca in lista_sentencas:
        lista_frases = separa_frases(sentenca)
        for frase in lista_frases:
            somaFrases += len(frase)
    #print("total_frases =", total_frases)
    #print("somaFrases =", somaFrases)
    return somaFrases/total_frases

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto
    e deve devolver a assinatura do texto.'''
    wal = calcula_tamanho_medio_palavra(texto)
    ttr = calcula_relacao_type_token(texto)
    hlr = calcula_razao_hapax_legomana(texto)
    sal = calcula_tamanho_medio_sentenca(texto)
    sac = calcula_complexidade_media_sentenca(texto)
    pal = calcula_tamanho_medio_frase(texto)
    return [wal, ttr, hlr, sal, sac, pal]

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    '''Sab é o grau de similaridade entre os textos a e b;
       fi,a é o valor de cada traço linguístico i no texto a; e
       fi,b é o valor de cada traço linguístico i no texto b.'''
    Sab = 0
    matriz = []
    matriz.append(as_a)
    matriz.append(as_b)
    somaDifAB = 0
    for lin in range(len(matriz) - 1):
        for col in range(len(matriz[lin])):
            #print(as_a[col],",", as_b[col])
            #print("[",lin,"][",col,"]")
            #print("as_a[",as_a[col],"]", "as_b[",as_b[col],"]")
            somaDifAB += abs(as_a[col] - as_b[col])
    #print("somaDifAB =",somaDifAB)
    Sab = somaDifAB/6
    #print("Sab = ",Sab)
    return Sab


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos
        e deve devolver o numero (1 a n) do texto
        com maior probabilidade de ter sido infectado por COH-PIAH.'''
    texto_coh_piah = 0
    aux = 1
    lista_assinaturas = []
    Sab = 0
    SabAux = 0
    for texto in textos:
        lista_assinaturas.append(calcula_assinatura(texto))
    for assinatura in lista_assinaturas:
        #print(assinatura)
        Sab = compara_assinatura(ass_cp, assinatura)
        #print("texto",aux,"Sab",Sab)
        if SabAux == 0:
            SabAux = Sab
            texto_coh_piah = aux
        else:
            if Sab <= SabAux:
                SabAux = Sab
                texto_coh_piah = aux
        aux += 1
    return texto_coh_piah

def main():
    ass_default = le_assinatura()
    lista_textos = le_textos()

    coh_piah = avalia_textos(lista_textos, ass_default)
    print("O autor do texto",coh_piah," está infectado com COH-PIAH")
