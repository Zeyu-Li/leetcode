class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # sort at the start
        return self.kSum(sorted(nums), target, 4)
        
    def kSum(self, nums: List[int], target: int, k: int) -> List[List[int]]:
        result = []
        
        # if there are no numbers in the array or achieving target is not possible, return result 
        if len(nums) == 0 or nums[0] * k > target > nums[-1] * k:
            return result
        # (base case) do two sum if kSum is actually 2 sum
        if k == 2:
            return self.twoSum(nums, target)
        
        for i in range(len(nums)):
            if i == 0 or nums[i-1] != nums[i]:
                for sub in self.kSum(nums[i+1:], target - nums[i], k - 1):
                    result.append([nums[i]] + sub)
        
        return result
        
    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        efficient 2 sum from solutions (runs O(n))
        """
        result = []
        low, high = 0, len(nums) - 1
        
        while (low < high):
            sum = nums[low] + nums[high]
            if sum < target or (low > 0 and nums[low] == nums[low-1]):
                low+=1
            elif sum > target or (high < len(nums) - 1 and nums[high] == nums[high + 1]):
                high -= 1
            else:
                result.append([nums[low], nums[high]])
                low += 1
                high -= 1
            
        
        return result
        