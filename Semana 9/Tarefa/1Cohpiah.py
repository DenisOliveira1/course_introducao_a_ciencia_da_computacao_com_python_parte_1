import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

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
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(a,b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    somatorio = 0
    for i in range(len(a)):
        
        calculo = (a[i] - b[i])
        if calculo < 0:
            calculo = calculo*(-1)
        somatorio = somatorio + calculo
        #print (calculo)
        
    return somatorio/6

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    #texto = Oi,tudo bom?kkk.
    
    listaSentencas = []
    listaSentencas = separa_sentencas(texto)                                        #separa em .!?
    #listaSentencas[0] = Oi,tudo bom
    #listaSentencas[1] = kkk
    
    listaFrases = []#array de array
    for i in listaSentencas:
        listaFrases.append(separa_frases(i))                                        #separa em ,:;
    #listaFrases[0][0] = Oi
    #listaFrases[0][1] = tudo bom
    #listaFrases[1][0] = kkk

    listaPalavras = [] #array de array de array
    for i in range(len(listaFrases)):
        for j in listaFrases[i]:
            listaPalavras.append(separa_palavras(j))                                #separa em palavras
    #listaPalavras[0][0] = Oi
    #listaPalavras[1][0] = tudo
    #listaPalavras[1][1] = bom
    #listaPalavras[2][0] = kkk

    #teste1 ----------------------------------------------
    #print("\nTeste1:", end = "\n")
    #print(listaSentencas)
    #print(listaFrases)
    #print(listaPalavras)
    #print(listaPalavras[0][0])
    #print(listaPalavras[1][0])
    #print(listaPalavras[1][1])
    #print(listaPalavras[2][0])
    #print("")
    #teste1 ----------------------------------------------

    todasPalavras = []#array
    somaTamanhoPalavras = 0
    for i in range(len(listaPalavras)):
        for j in listaPalavras[i]:
                somaTamanhoPalavras = somaTamanhoPalavras + len(j)
                todasPalavras.append(j)
                
    wal = somaTamanhoPalavras/len(todasPalavras)                                    #tamanho medio de palavra


    ttr =  n_palavras_diferentes(todasPalavras)/len(todasPalavras)                  #relação Type-Token
                                 
    hlr = n_palavras_unicas(todasPalavras)/len(todasPalavras)                       #Razão Hapax Legomana

    somaTamanhosSentencas = 0
    for i in listaSentencas:
        sentencaSemEspacos = i
        somaTamanhosSentencas = somaTamanhosSentencas + len(sentencaSemEspacos)                  

    #print(somaTamanhosSentencas)
    #print(len(listaSentencas))
    
    sal = somaTamanhosSentencas/len(listaSentencas)                                 #tamanho médio de sentença

    somaTamanhosFrase = 0
    todasFrases = []#array
    for i in range(len(listaFrases)):
        for j in listaFrases[i]:
            fraseSemEspacos = j
            somaTamanhosFrase = somaTamanhosFrase + len(fraseSemEspacos)
            todasFrases.append(j)
            
    pal = somaTamanhosFrase/len(todasFrases)  
                                 
    sac = len(todasFrases)/len(listaSentencas)                                      #complexidade média da sentença
    #print(len(todasFrases))
    
    pal = somaTamanhosFrase/len(todasFrases)                                        #tamanho medio de frase
    #print(somaTamanhosFrase)
    
    #teste2 ----------------------------------------------
    print([wal, ttr, hlr, sal, sac, pal])
    #teste2 ----------------------------------------------
    
    return [wal, ttr, hlr, sal, sac, pal]

def avalia_textos(textos, assinaturaReferencia):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''

    assinaturaTextos = []#array de arrays
    for i in textos:
        assinaturaTextos.append(calcula_assinatura(i))

    resultados = []#array
    for i in assinaturaTextos:
        resultados.append(compara_assinatura(i, assinaturaReferencia))

    menorResultado = resultados[0]
    for i in resultados:
        if i < menorResultado:
            menorResultado = i
    return resultados.index(menorResultado)+1
    

#assinaturaReferencia = le_assinatura()#array
assinaturaReferencia = [4.79,0.72,0.56,80.5,2.5,31.6]
textos = le_textos()#array
resultadoFinal = avalia_textos(textos, assinaturaReferencia)
print("")
print("O autor do texto",resultadoFinal,"está infectado com COH-PIAH")
