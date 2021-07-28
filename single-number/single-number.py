class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # hash map
        hash = dict()
        for num in nums:
            if str(num) not in hash:
                hash[str(num)] = True
            else:
                hash[str(num)] = False
                
        for key, value in hash.items():
            if value:
                return key
                