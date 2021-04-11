def fatorial(n):
    produto = 1
    while n != 0:
        produto = produto * n
        n = n - 1

    print("Fatorial: ", produto)
    
    n = int(input("Digite um numero: "))



n = int(input("Digite um numero: "))
while n >= 0:
    fatorial(n)




