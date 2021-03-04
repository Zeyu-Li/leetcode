# brute force
class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.start = 0
        self.end = 0
        self.string = s
        self.str_length = len(s)
        for index, char in enumerate(s):
            self.expand(index, index)
            self.expand(index, index+1)
                
        return s[self.start:self.start+self.end]
    
    def expand(self, left: int, right: int):
        while left >= 0 and right < self.str_length and self.string[left] == self.string[right]:
            left -= 1
            right += 1
        if (self.end < right - left - 1):
            self.end = right - left - 1
            self.start = left + 1
            