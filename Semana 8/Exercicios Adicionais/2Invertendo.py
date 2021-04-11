a = []
n = int(input("Digite um número: "))

while n != 0: 
    a.append(n);
    n = int(input("Digite um número: "))

#a.reverse()
#for i in a:
    #print(i)
print("")
for i in range(len(a)-1,-1,-1):
    print(a[i])
