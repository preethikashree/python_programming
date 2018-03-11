num=int(input())
array=[]
for i in range(num):
    m=int(input())
    array.append(m)
min=array[0]
for i in range(num):
    if(min>array[i]):
        min=array[i]
print(min)
    

