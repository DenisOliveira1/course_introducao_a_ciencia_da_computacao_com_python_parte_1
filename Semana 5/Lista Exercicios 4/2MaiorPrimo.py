def maior_primo (n):
    achou = False
    
    while (not achou) and (n != 0):
        if n % 2 != 0 and n % 3 != 0 and n % 5 != 0 and n % 7 != 0:
            primo = n
            break
        elif n == 2 or n == 3 or  n == 5 or  n == 7:
            primo = n
            break
        else:
            prmo = "sem primos"
        n = n - 1
        
    return primo
        
        
        

