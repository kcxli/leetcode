class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums) 
        if (l >= h):
            return -1
        m = (l+h)//2 
        if (nums[m] == target):
            return m 
        elif (nums[m] > target):
            h = m 
            return self.search(nums[l:h], target) 
        else:
            l = m + 1 
            rec = self.search(nums[l:h], target)
            if (rec == -1):
                return -1
            else: 
                return rec + (m - 0 + 1)