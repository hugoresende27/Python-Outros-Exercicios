#Given an array of ints length 3, figure out which is larger, the first or last element in the array, 
# and set all the other elements to be that value. Return the changed array.
#max_end3([1, 2, 3]) → [3, 3, 3]
#max_end3([11, 5, 9]) → [11, 11, 11]
#max_end3([2, 11, 3]) → [3, 3, 3]

def max_end3(nums):
    novo = []
    if nums[0]>=nums[2]:
        maior = nums[0]
    elif nums[2]>=nums[0]:
        maior = nums[2]  
    for i in range (3):
        novo.append(maior)  
    return novo  

# def max(nums):
#     # big = max(nums[0],nums[2])
#     # nums[0] = big
#     # nums[1] = big
#     # nums[2] = big
#     # return nums

def max(nums):
    return [nums[0]] * 3 if nums[0] >= nums[-1] else [nums[-1]] * 3


print (max_end3([1, 2, 3]) )
print (max_end3([2, 11, 3]))
print (max_end3([11, 5, 9]))
print ("#################################")
print (max([1, 2, 3]) )
print (max([2, 11, 3]))
print (max([11, 5, 9]))