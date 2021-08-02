class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = dict()
        for char in s:
            if not char in s_hash:
                s_hash[char] = 1
            else:
                s_hash[char] += 1
                
        t_hash = dict()
        for char in t:
            if not char in t_hash:
                t_hash[char] = 1
            else:
                t_hash[char] += 1
                
        sorted(s_hash, key=s_hash.get)
        sorted(t_hash, key=t_hash.get)
        
        return t_hash == s_hash
    