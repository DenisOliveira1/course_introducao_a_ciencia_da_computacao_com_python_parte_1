a = int(input("Digite um número: "))
b = int(input("Digite um número: "))
c = int(input("Digite um número: "))

if a < b:
    if b < c:
        print("crescente")
    else:
        print("não está em ordem crescente")
else:
    print("não está em ordem crescente")
