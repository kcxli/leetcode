'''
maybe one for loop and within it do the normal two sum, to remove duplicates
only scan forward each time (no going backwards) --- wrote this out and 
it exceeds memory limit 
use a hashmap to map keys (two sum) to their values (two unique indexes) 
then for every num in nums see if there is a key in th map that adds to 0, 
and if the index of num is not in the value, append to solution 

oops forgot how to use hashmaps again lmao had to relearn the syntax

'''

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # sort array 
        nums.sort()
        sol = []

        # for every int i in array, want to find two corresponding int j and k 
        # such that j + k = -i. Achieve this using the two sum ii approach 

        for i, num in enumerate(nums):
            l = i + 1
            r = len(nums) - 1
            while (l < r):
                total = nums[l] + nums[r]
                if (total == -num):
                    sol.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif (total > -num):
                    r -= 1
                else:
                    l += 1 

        # remove duplicates
        return [list(x) for x in (set(tuple(y) for y in sol))]

