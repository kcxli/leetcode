class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        
        while l < r:
            sum = numbers[l] + numbers[r]
            if (sum == target):
                return [l + 1, r + 1]
            elif (sum < target):
                l += 1
            else:
                r -= 1
        
'''
     i recognize this solution is not the most time efficient but 
     i thought of it pretty quickly so i guess that counts? 
     time efficiency is O(n), space is O(1)
     i think if you did some variation of binary search it would be
     faster? oh shoot nevermind the other sols also do the same thing
     they just calculate numbers[l] + numbers[r] a single time instead
     of twice so it is faster ... otherwise is the same.. lemme change that. 
     there's also a faster
     sol that makes a list of "seen" numbers and then calculates target - curr
     for each number in the list and checks if it has been "seen" yet. 

     i should also remember that "for i, num in enumerate(numbers)" is 
     essentially a for loop i always write it in a more jank way 
    
'''     

