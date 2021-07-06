class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        # remove useless elements
        for i in range(n):
            if 1 > nums[i] or nums[i] > n:
                nums[i] = 0
                
        for i in range(n):
            if 1 <= nums[i] % (n + 1) <= n:
                nums[nums[i] % (n + 1) - 1] += n + 1
          
        for i in range(n):
            if nums[i] <= n:
                return i + 1
        
        return n + 1