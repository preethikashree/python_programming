a=(1,2,3,4,5,6,7,8,9,10,11)
odd_number=0
even_number=0
for x in a:
    if(x%2==0):
        even_number+=1
    else:
        odd_number+=1
print("Numberof even numbers in list:")
print(even_number)
print("Numbert of odd numbers in list:")
print(odd_number)
