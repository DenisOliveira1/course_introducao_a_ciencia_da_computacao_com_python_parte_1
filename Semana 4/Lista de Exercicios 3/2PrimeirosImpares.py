n = int(input("Digite o valor de n: "))

cont = 0
aux = 0

while cont != n:
    if aux % 2 != 0:
        print(aux)
        cont = cont + 1
    aux = aux + 1
    
