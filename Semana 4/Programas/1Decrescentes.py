decrescente = True
anterior = int(input("Digite o primeiro número: "))
valor = 1

while valor != 0 and decrescente:
    valor = int(input("Digite o proximo número: "))
    if valor > anterior:
        decrescente = False
    anterior = valor
if decrescente:
    print("A sequencia está em ordem descrescente :-)")
else:
    print("A sequencia não está em ordem descrescente :-(")
