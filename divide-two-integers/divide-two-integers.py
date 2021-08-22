class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive = (dividend < 0) == (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        result = 0
        
        # thanks internet
        while divisor <= dividend:
            
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                result += i
                i <<= 1
                temp <<= 1
                
            
        # cap on both ends
        return min(max(-2 ** 31, result if positive else -result), 2 ** 31 - 1)
        