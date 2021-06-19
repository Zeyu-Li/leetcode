class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelsList = [jewel for jewel in jewels]
        count = 0
        for stone in stones:
            count += 1 if stone in jewelsList else 0
            
        return count