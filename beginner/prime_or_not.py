num=int(input("Enter a number:"))
for i in range(2,1001):
    if (num%i)!=0 and num%1==0:
        print("Prime number")
        break
    else:
        print("Not a prime number")
        break
        
