class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        string = ''
        for char in s:
            # if character is not in string, then append to it
            if char not in string:
                string += char
                
                count = max(count, len(string))
            else:
                # remove from the first instance of char in string
                same_char_index = string.index(char)
                string = string[same_char_index+1:] + char # add the new char after this
                
        return count