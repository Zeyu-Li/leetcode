class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        maps = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        
        # base case
        if len(digits) == 0:
            return []
        
        # dp solution
        dp = [[""]]
        for i, digit in enumerate(digits, 1):
            dp_tmp = []
            for item in dp[i-1]:
                for mapping in maps[int(digit)-2]:
                    dp_tmp.append(item + mapping)
                
            dp.append(dp_tmp)
                
        return dp[len(digits)]
            