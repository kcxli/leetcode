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
            if (num != nums[i-1] or i == 0): 
                l = i + 1
                r = len(nums) - 1
                while (l < r):
                    total = nums[l] + nums[r]
                    if (total == -num):
                        sol.append((nums[i], nums[l], nums[r]))

                        while (l + 1 < r and nums[l] == nums[l+1]):
                            l += 1
                        l += 1
  
                        while (r - 1 > l and nums[r] == nums[r-1]):
                            r -= 1
                        r -= 1
                            
                    elif (total > -num):
                        while (r - 1 > l and nums[r] == nums[r-1]):
                            r -= 1
                        r -= 1

                    else:
                        while (l + 1 < r and nums[l] == nums[l+1]):
                            l += 1
                        l += 1
                            

        # remove duplicates
        return sol

