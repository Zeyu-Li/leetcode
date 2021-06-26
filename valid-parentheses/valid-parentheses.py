class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping.keys():
                
                if stack == []:
                    return False
                elif mapping[char] != stack[len(stack)-1]:
                    return False
                # else pop from stack
                stack.pop()
            else:
                return False
            
        return len(stack) == 0