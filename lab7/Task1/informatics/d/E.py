N = int(input("Enter size of massive:"))  
arr = list(map(int, input().split()))  

count = 0  
for i in range(1, len(arr)): 
    if (arr[i-1] > 0 and arr[i] > 0) or (arr[i-1] < 0 and arr[i] < 0):
        count += 1

if count > 0:
    print("YES")
else:
    print("NO")
