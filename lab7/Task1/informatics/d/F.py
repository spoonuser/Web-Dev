N = int(input("Enter size of massive:"))  
arr = list(map(int, input().split()))  

count = 0  
for i in range(1, len(arr) - 1): 
    if (arr[i-1] > arr[i] and arr[i+1] >  arr[i]) or (arr[i-1] <  arr[i] and arr[i] <  arr[i]):
        count += 1
        i+=1
print(count)

