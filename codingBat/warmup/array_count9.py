#Given an array of ints, return the number of 9's in the array.
#array_count9([1, 2, 9]) → 1
#array_count9([1, 9, 9]) → 2
#array_count9([1, 9, 9, 3, 9]) → 3

def array_count9(nums):
    cont=0
    for x in nums:
        if  x==9:
            cont +=1
    return cont

print (array_count9([1, 2, 9]))
print (array_count9([1, 9, 9, 3, 9]))
print (array_count9([1, 9, 9]))
        
        