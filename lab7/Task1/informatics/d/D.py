N = int(input("Enter size of massive:"))  
arr = list(map(int, input().split())) 
count  = 0
i = 1
for i in range(len(arr)):
    if arr[i-1] < arr[i]:
        count += 1
print(count)