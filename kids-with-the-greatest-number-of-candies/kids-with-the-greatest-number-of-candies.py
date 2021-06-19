class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum = max(candies)
        result = []
        for child in candies:
            result.append(child+extraCandies >= maximum)
        return result
        