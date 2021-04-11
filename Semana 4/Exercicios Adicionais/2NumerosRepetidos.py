n = int(input("Digite m numero inteiro: "))

tam = len(str(n))
vetor = []
tem = False

while tam != 0:
    if n // 10 != 0:
        vetor.append(n % 10)
        n = n // 10
    else:
        vetor.append(n)
        
    tam = tam - 1

tam = len(vetor)
#print (tam)
i = 0

while tam != 1:
    #print (vetor[i]," ", vetor[i+1],"\n")
    if vetor[i] == vetor[i+1]:
        tem = True
        break
    i = i + 1
    tam = tam - 1
    
if tem:
    print("sim")
else:
    print("não")
