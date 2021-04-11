f = open("denis.txt", "w")
for i in range(10):
    f.write(str(i)+"\n")

f = open("denis.txt", "r")
tudo = f.readlines()
a = []

for linha in tudo:
    a.append(linha.replace("\n",""))
    #print(linha)

print(a)
f.close() 

p = "oi"
p = p.upper()
print(p)
p = p.lower()
print(p)


