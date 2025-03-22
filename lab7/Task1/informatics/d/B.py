N = int(input("Enter size of massive:"))  
arr = list(map(int, input().split())) 

for i in arr:
    if i % 2 == 0:
        print(i, end=' ')