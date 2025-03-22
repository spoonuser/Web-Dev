import math
a = int(input("Enter a : "))
b = int(input("Enter b : "))

for i in range(a,b+1):
    if math.sqrt(i) % 1 == 0:
        print(i, end=" ")