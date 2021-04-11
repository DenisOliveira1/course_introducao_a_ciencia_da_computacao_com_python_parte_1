meuCartao = int(input("Digite o numero do seu cartão: "))

cartaoLido = 1
encontreiMeuCartao = False

while cartaoLido != 0 and not encontreiMeuCartao:
    cartaoLido = int(input("Digite o numero do proximo cartao: "))
    if cartaoLido == meuCartao:
        encontreiMeuCartao = True
if encontreiMeuCartao:
    print("Eba!!! Meu cartao esta lá!")
else:
     print("Xi, Meu cartao não esta lá...")
    
