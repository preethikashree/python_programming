n=(input())
if (n>='a' and n<='z') or (n>='A' and n<='Z'):
    print("Please enter integer")
else:
    n=int(n)
    a=[]
    for i in range (n):
        b=int(input())
        a.append(b)
        min=a[0]
    for i in range(n):
        if(min>a[i]):
            min=a[i]
    print(min)
