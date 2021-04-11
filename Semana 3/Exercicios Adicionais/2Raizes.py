import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

d = (b**2)-(4*a*c)

if d == 0:
    r1 = (-b + math.sqrt(d))/(2*a)
    print("a raiz desta equação é",r1)
elif d < 0:
    print("esta equação não possui raízes reais")
else:
    r1 = (-b + math.sqrt(d))/(2*a)
    r2 = (-b - math.sqrt(d))/(2*a)
    if r2>r1:
        print("as raízes da equação são",r1,"e",r2)
    else:
        print("as raízes da equação são",r2,"e",r1)
