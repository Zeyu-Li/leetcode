class Solution:
    def addBinary(self, a: str, b: str) -> str:
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
            if total == 3:
                carry = 1
                result+='1'
            elif total == 2:
                carry = 1
                result+='0'
            elif total == 1:
                carry = 0
                result+='1'
            else:
                carry = 0
                result+='0'
            
        # reverse string
        return result[::-1] if result[len(result)-1] != '0' else result[:-1][::-1]