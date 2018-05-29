n=int(input())
a=int(input())
d=int(input())
sum=0
for i in range(1,n+1):
    sum=sum+i
res=a+((sum-1)*d)
print(res)
    
