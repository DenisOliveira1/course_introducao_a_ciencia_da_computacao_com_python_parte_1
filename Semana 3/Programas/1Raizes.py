import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

d = (b**2)-(4*a*c)

if d == 0:
    r1 = (-b + math.sqrt(d))/(2*a)
    print("A unica raiz é:",r1)
else:
    r1 = (-b + math.sqrt(d))/(2*a)
    r2 = (-b - math.sqrt(d))/(2*a)
    print("A primeira raiz é:",r1)
    print("A segunda raiz é:",r2)
