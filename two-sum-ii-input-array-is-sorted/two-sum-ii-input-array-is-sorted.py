class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # could be same solution as two sum
        hash_map = dict()

        for i, num in enumerate(nums):
            canadiate = target - num

            # if the new target (canadiate is in the hash map, we return that otherwise we put it in the hash map)
            if canadiate in hash_map:
                return [hash_map[canadiate]+1, i+1]
            hash_map[num] = i
