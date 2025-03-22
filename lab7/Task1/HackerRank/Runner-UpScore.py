if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))  
    arr = sorted(set(arr), reverse=True)  
    
    if len(arr) < 2:
        print("No second largest number") 
    else:
        print(arr[1]) 
