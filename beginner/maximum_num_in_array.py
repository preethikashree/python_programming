num=int(input("Enter the number:"))
array=[]
for i in range(num):
    m=int(input())
    array.append(m)
max=array[0]
for i in range(num):
    if(max<array[i]):
        max=array[i]
print("Max_num:",max)
    
