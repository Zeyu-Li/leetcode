class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # bitmask way
        length = len(nums)
        result = []
        
        # combinatory ways to obtain power set
        for i in range(2**length, 2**(length+1)):
            bitmask = bin(i)[3:] # ignore first 3 char of 0bx
            
            result.append([nums[j] for j in range(length) if bitmask[j] == '1'])
            
        return result