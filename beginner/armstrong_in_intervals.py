m=int(input("Enter two intervals:"))
n=int(input())
for i in range(m,n+1):
    temp=i
    sum=0
    while(temp>0):
        a=temp%10
        temp=temp//10
        sum=sum+(a**3)
    if(sum==i):
        print(i)
