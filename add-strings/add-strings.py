class Solution:
    def addStrings(self, a: str, b: str) -> str:
        # similar to binary addition (https://leetcode.com/problems/add-binary/)
        # reverse
        a = a[::-1]
        b = b[::-1]
        
        max_length = max(len(a), len(b)) + 1
        
        # pack to max
        for _ in range(max_length-len(a)):
            a+='0'
        for _ in range(max_length-len(b)):
            b+='0'
            
        result = ''
        carry = 0
        current = 0
        for i in range(max_length):
            total = int(a[i]) + int(b[i]) + carry
            if total >= 10:
                carry = 1
                result+=str(total%10)
            else:
                carry = 0
                result+=str(total)
            
        # reverse string
        return result[::-1] if result[len(result)-1] != '0' else result[:-1][::-1]
        