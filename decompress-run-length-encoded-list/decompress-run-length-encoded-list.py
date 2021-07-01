class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        i = 0
        result = []
        while i < len(nums):
            result += [nums[i+1]] * nums[i]
            i+=2
            
        return result