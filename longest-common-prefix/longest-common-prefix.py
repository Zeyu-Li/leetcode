class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs, key=len)
        common = ""
        is_common = True
        
        for i, char in enumerate(strs[0]):
            for j, string in enumerate(strs):
                if j == 0:
                    continue
                if string[i] != strs[0][i]:
                    is_common = False
                    break
            if not is_common:
                break
            common+=char
        
        return common
    