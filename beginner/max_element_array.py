n=(input())
if (n>='a' and n<='z') or (n>='A' and n<='Z'):
    print("Please enter integer")
else:
    n=int(n)
    a=[]
    for i in range (n):
        b=int(input())
        a.append(b)
        max=a[0]
    for i in range(n):
        if(max<a[i]):
            max=a[i]
    print(max)
