n = int(input("Digite um numero: "))

while n >= 0:
    produto = 1
    while n != 0:
        produto = produto * n
        n = n - 1

    print("Fatorial: ", produto)
    
    n = int(input("Digite um numero: "))




