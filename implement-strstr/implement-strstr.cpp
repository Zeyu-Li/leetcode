class Solution {
public:
    int strStr(string haystack, string needle) {
        // special cases
        if (haystack.size() < needle.size()) {
            return -1;
        }
        
        if (needle.size() == 0) {
            return 0;
        }
        
        for (int i = 0; i < haystack.size() - needle.size() + 1; i++) {
            if (haystack[i] == needle[0]) {
                // check the rest
                for (int j = 1; j < needle.size(); j++) {
                    if (haystack[i+j] != needle[j]) goto next;
                }
                return i;
            }
            next:
            continue;
        }
        return -1;
    }
};