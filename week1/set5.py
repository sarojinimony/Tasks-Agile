
#1. Write a program in Python to remove duplicate items from a list.
#Method1
def remove_dup(list):
    result=[]
    for i in list:
        if i not in result:
            result.append(i)
    return result
print(remove_dup([1,3,3,2,4,4,5]))

#Method2
def remove_dup(rlist):
   return list(set(inputlist))
inputlist=[1,2,3,4,5,4,3,2]
print(remove_dup(inputlist))

#2. Remove and replace elements
def remove_rep(nums,remove):
   count = 0
   for i in range(len(nums)):
      if nums[i]==remove:
         nums[i]="_"
         count += 1
   nums = [x for x in nums if x != "_"] + ["_"] * count
   return nums
print(remove_rep([3,2,2,3],3))

#3. Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
def dup(arr):
   for i in range(len(arr)):
      for j in range(i+1,len(arr)):
         if arr[i]==arr[j]:
            return True
   return False
print(dup([1,2,3,1]))
print(dup([1,2,3,4]))