n = int(input("Digite m numero inteiro: "))

if n % 2 != 0 and n % 3 != 0 and n % 5 != 0 and n % 7 != 0:
    print("primo")
elif n == 2 or n == 3 or n == 5 or n == 7:
    print("primo")
else:
    print("não primo")
