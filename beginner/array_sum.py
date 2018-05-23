n=int(input())
k=int(input())
a=[]
sum=0
for i in range(n):
    m=int(input())
    a.append(m)
for i in range(k):
    sum=sum+a[i]
print(sum)
    
