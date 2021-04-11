n = int(input("Digite um numero: "))

r1 = n % 3
r2 = n % 5

if r1 == 0 and r2 == 0:
    print("FizzBuzz")
else:
    print(n)
