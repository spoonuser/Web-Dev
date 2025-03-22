def boolFunc(a, b):
    if a == 1 or b == 1:
        return 1
    else:
        return 0

a = int(input("Enter a: "))
while a != 0 and a != 1:
    print("a must be 0 or 1")
    a = int(input("Enter a: "))

b = int(input("Enter b: "))
while b != 0 and b != 1:
    print("b must be 0 or 1")
    b = int(input("Enter b: "))

print(boolFunc(a, b))
