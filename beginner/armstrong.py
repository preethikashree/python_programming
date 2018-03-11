num=int(input())
temp=num
sum=0
while(temp>0):
    a=temp%10
    sum=sum+(a**3)
    temp=temp//10
if(num==sum):
    print("Yes")
else:
    print("No")
    
