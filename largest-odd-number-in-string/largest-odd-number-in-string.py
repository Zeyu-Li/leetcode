class Solution:
    def largestOddNumber(self, num: str) -> str:
        max_item = ""
        for i, char in enumerate(num):
            if int(char) % 2:
                max_item = num[:i+1]
                
        return max_item