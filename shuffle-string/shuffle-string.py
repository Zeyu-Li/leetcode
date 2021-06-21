class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        returnString = [' ' for _ in range(len(indices))]
        for indice, char in zip(indices, s):
            returnString[indice] = char
            
        return ''.join(returnString)