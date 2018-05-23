num=int(input())
for i in range(2,1001):
    if (num%i)!=0 and num%1==0:
        print("yes")
        break
    else:
        print("no")
        break
        
