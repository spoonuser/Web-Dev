N = int(input("Enter size of massive:"))  
arr = list(map(int, input().split())) 
count = 0
for i in arr:
    if i > 0:
        count+=1
print(count)