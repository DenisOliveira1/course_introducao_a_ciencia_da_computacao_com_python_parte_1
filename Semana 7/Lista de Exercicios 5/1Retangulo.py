largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

aux = largura
while altura > 0:
    while largura > 0:
             print("#",end ="")
             largura = largura - 1
    print(end="\n")
    altura = altura - 1
    largura = aux
print(end="\n")
