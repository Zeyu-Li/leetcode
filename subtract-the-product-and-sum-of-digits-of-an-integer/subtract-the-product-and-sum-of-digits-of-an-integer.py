class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = sum([int(char) for char in str(n)])
        r = 1
        for char in str(n):
            r*=int(char)
            
        return r-s