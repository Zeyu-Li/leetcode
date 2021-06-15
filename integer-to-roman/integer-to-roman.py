class Solution:
    def intToRoman(self, num: int) -> str:
        # string to int array
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        
        final_str = ""

        i = 0
        while num > 0:
            final_str += (num // values[i]) * numerals[i]
            num = num % values[i]
            i+=1

        return final_str