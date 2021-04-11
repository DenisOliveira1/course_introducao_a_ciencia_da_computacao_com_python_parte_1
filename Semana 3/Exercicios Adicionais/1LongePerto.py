x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if x1-x2 >= 10 or y1-y2 >= 10 or x2-x1 >= 10 or y2-y1 >= 10:
    print("longe")
else:
    print("perto")
