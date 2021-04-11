largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

aux = largura
aux2 = altura
while altura > 0:
    while largura > 0:
            if largura == 1 or largura == aux or altura == 1 or altura == aux2:
                print("#",end ="")
            else:
                print(end=" ")   
            largura = largura - 1
    print(end="\n")
    altura = altura - 1
    largura = aux
