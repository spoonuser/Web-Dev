a = int(input("Enter a: "))
i = 2
while i <= a:
    if a % i == 0:
        print(i)
        break
    i += 1 