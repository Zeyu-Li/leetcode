class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash = dict()
        for num in nums:
            if str(num) not in hash:
                hash[str(num)] = 1
            else:
                hash[str(num)] += 1
            
        current = 0
        max = 0
        for key, value in hash.items():
            if value > max:
                current = int(key)
                max = value
            
        return current