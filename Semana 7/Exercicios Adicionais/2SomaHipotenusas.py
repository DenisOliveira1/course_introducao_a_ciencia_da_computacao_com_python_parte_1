def testa(hip,cat1,cat2,n):
    if ((cat1**2)+(cat2**2) == (hip**2)):
        print(str(hip)+" "+str(cat1)+" "+str(cat2)+" --------------- "+str((cat1**2)+(cat2**2))+" == "+str(hip**2)+" soma = "+str(hip+cat1+cat2)+" ACHOU")
    #else:
        #print(str(hip)+" "+str(cat1)+" "+str(cat2)+" --------------- "+str((cat1**2)+(cat2**2))+" == "+str(hip**2)+" soma = "+str(hip+cat1+cat2))
        
    
    
def soma_hipotenusas(n):
    somados = []
    
    soma = 0
    cat1 = 1
    cat2 = 1
    hip = 1

    while hip <= n:
        
        while cat1 <= hip:
            
            while cat2 <= hip:
                
                #testa(hip,cat1,cat2,n)
                if ((cat1**2)+(cat2**2) == (hip**2)):
                    if hip not in somados:
                         soma = soma + hip
                         somados.append(hip)               
                cat2 = cat2 + 1
  
            cat1 = cat1 + 1
            cat2 = 1

        hip = hip + 1
        cat1 = 1
        

    return soma


#soma_hipotenusas(25) == 105
            
        
            
        


