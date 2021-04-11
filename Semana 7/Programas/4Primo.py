def verifica(x):
    fator = 2
    if x == 2: # exceção
        return True
    
    while x % fator != 0 and fator <= x/2:#1#2
        fator = fator + 1
        
    if x % fator == 0:#3
        return False
    else:
        return True
        

n = int(input("Digite um numero: "))

while n > 0:
    if verifica(n):
        print("sim primo")
    else:
        print("não primo")
    n = int(input("Digite um numero: "))

#1 - achar um fator que consiga dividir n e nao ter resto
#2 - ou estar todas as possibilidades
    
#3 - #verifica se foi a condiçao 1 que aconteceu no while acima

        
