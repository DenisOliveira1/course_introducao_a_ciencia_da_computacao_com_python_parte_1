n = int(input("Digite um número inteiro: "))

soma = 0
passa = True

while passa:
    aux = n % 10
    soma = soma + aux
    
    if n // 10 == n:
        passa = False
    else:
        n = n // 10

print(soma)
