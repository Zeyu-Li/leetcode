class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # backtrack
        results = []
        self.dfs(candidates, target, [], results)
        return results
    
    def dfs(self, nums, target, path, results):
        if target < 0:
            # if path negative, we don't need to consider it
            return 
        elif target == 0:
            # if exactly target, it is the right one and is a solution
            results.append(path)
            return 
        for i in range(len(nums)):
            # recurse dfs path (form branches to all numbers 
            # while updating the target and path)
            self.dfs(nums[i:], target-nums[i], path + [nums[i]], results)
        
        