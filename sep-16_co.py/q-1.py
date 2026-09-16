fahrenheit = float(input("Enter the number: "))
f = fahrenheit
celsius = (f-32)*(5/9)
print(celsius)

#theek hai loop ka istemal karna hai taki multiple test cases hamare liye zaroori hai
#    select the function
#    give the two parameter are i and num.
#    i = input like fahrenheit
#    num = conversion
#    for loop for i 
#    for loop for num
#    return function

   
    
    
# def simple_temp(natsu):
#     natsu = float(input("Enter the temperature: "))
#     dumbbell = (natsu - 32) * (5/9)
#     for dumbell in natsu:
        
    
#     result.append[results]
#     return results


print("PROGRAM STARTED")

def simple_temp(natsu):
    results = []

    for dumbbell in natsu:
        celsius = (dumbbell - 32) * (5 / 9)
        results.append(celsius)

    return results

temperatures = [32, 212, 98.6]
results = simple_temp(temperatures)

print(results)
print("PROGRAM FINISHED")



# Do not stop after finding the first pair.
# LeetCode Homework — Find All Pairs

# Problem:
# Given an integer array nums and an integer target, return all pairs of indices [i, j] such that:

# nums[i] + nums[j] == target

# Each pair must satisfy:
# i < j

# Return an empty list if no such pair exists.

# Example 1:
# Input: nums = [2, 7, 4, 5, 3], target = 7
# Output: [[0, 4], [2, 3]]

# Example 2:
# Input: nums = [1, 2, 3, 4], target = 10
# Output: []

# Example 3:
# Input: nums = [3, 3, 3, 3], target = 6
# Output: [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]

# Constraints:
# 2 <= nums.length <= 100
# -1000 <= nums[i] <= 1000
# -2000 <= target <= 2000

# Requirement:
# Use nested loops.
# Do not use a hash map.
 
 
 #HINT: 
#  1. result = empty list
# 2. function(nums, target)
# 3.     n = length of nums
# 4.     for i in range(0, n)
# 5.         for j in range(i + 1, n)
# 6.             sum = nums[i] + nums[j]
# 7.             if sum == target
# 8.                 result.append([i, j])
# 9.     return result
# 10. print(result)



# result = []
# def simple_num(nums, target):
#     n = len(nums)
#     for i in range(0, n):
#         for j in range(i+1, n):
#             eater = nums[i] + nums[j]
#             if eater == target:
#                 result.append([i, j])
                
#         return result
#         nums = [1, 2, 3, 4]
#         target = 7
#         result = simple_num(nums, target)
#         print(result)



# finala hint : boss level
# def simple_num(nums, target):
#     result = []

#     loops...
#         checking...

#     return result


# nums = [...]
# target = ...

# answer = simple_num(nums, target)
# print(answer)


# def simple_num(nums, target):
#     result  = []
#     n = len(nums)
#     for i in range(0, n):
#         for j in range(i+1, n):
#             sum = nums[i] + nums[j]
#             if sum == target:
#                 result.append([i,j])
#             return result
#     nums = [1, 2, 3, 4]
#     target = 7
    
#     result = simple_num(nums, target)
#     print(result)




def simple_num(nums, target):
    result = []
    n = len(nums)

    for i in range(0, n):
        for j in range(i + 1, n):
            pair_sum = nums[i] + nums[j]

            if pair_sum == target:
                result.append([i, j])

    return result


nums = [1, 2, 3, 4]
target = 7

result = simple_num(nums, target)
print(result)