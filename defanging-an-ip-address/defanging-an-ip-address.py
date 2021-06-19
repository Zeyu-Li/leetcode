class Solution:
    def defangIPaddr(self, address: str) -> str:
        result = ""
        for char in address:
            result += char if char != '.' else '[.]'
            
        return result