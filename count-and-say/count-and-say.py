class Solution:
    def countAndSay(self, n: int) -> str:
        # base case
        if n == 1:
            return "1"
        
        result = "11"
        for i in range(1, n-1):
            count = 0
            new = ""
            previous = result[0]
            for char in result:
                if previous == char:
                    count+=1
                else:
                    new += str(count) + str(previous)
                    count = 1
                    
                previous = char
                
            new += str(count) + previous
            
            result = new
            
        return result
        