a = int(input("Enter a : "))
b = int(input("Enter b : "))

reversed_num = int(str(a)[::-1]) 

if(reversed_num == str(a) and b == 1 ):
    print("YES")
elif(reversed_num == str(a) and b != 1 ):
    print("NO")
elif(reversed_num != str(a) and b == 1 ):
    print("NO")
else:
    print("YES")