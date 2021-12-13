#Given an array of ints length 3, return a new array with the elements in reverse order, 
# so {1, 2, 3} becomes {3, 2, 1}.
#reverse3([1, 2, 3]) → [3, 2, 1]
#reverse3([5, 11, 9]) → [9, 11, 5]
#reverse3([7, 0, 0]) → [0, 0, 7]

def reverse3(nums):
    novo=[]
    cont=0
    for i in range(2,-1,-1):
        novo.append(nums[i]) 
        cont + 1
    return novo

def rev(nums):
    return nums[::-1]       
        

print (reverse3([1, 2, 3]) )
print (reverse3([5, 11, 9]))
print ('############################')
print (rev([1, 2, 3]) )
print (rev([5, 11, 9]))