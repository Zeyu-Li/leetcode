class Solution:
    def sortSentence(self, s: str) -> str:
        result = ["" for _ in s.split()]
        for item in s.split():
            result[int(item[-1])-1] = item[:-1]
            
            
        return " ".join(result)