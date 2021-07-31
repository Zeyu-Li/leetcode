class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        bubble sort because I'm lazy and there are a lot of unnecessary moves
        """
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                # swap elements if smaller
                if nums[j] == 0:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    