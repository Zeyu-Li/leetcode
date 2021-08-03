class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False 
        
        # if n is power of 2 it will take the form of
        # 1000...0 (base 2)
        # therefor 2^x-1 will be
        # 0111...1 (base 2)
        # taking the and will result in 0 since 0 a
        return n & (n-1) == 0
        
        # return math.log(n, 2).is_integer()