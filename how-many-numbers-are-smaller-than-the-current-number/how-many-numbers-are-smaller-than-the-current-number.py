class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sort = sorted(nums)
        for i, num in enumerate(nums):
            nums[i] = sort.index(num)
            
        return nums