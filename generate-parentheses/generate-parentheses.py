class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # assume closure number and a brain bigger than a truck
        # QED ◼
        if not n: return ['']
        
        result = []
        for i in range(n):
            for left in self.generateParenthesis(i):
                for right in self.generateParenthesis(n-1-i):
                    result.append(f"({left}){right}")
                    
        return result