a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))
d = int(input("Enter d : "))

for i in range(a,b+1):
    if i % d == c:
        print(i, end=" ")