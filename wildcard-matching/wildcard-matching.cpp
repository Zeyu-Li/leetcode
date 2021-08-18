class Solution {
public:
    bool isMatch(string s, string p) {
        // copied because the bottom solution clearly works
        int i = 0, j = 0;
        int m = s.length(), n = p.length();
        int last_match = -1, starj = -1;
        while (i < m){
            if (j < n && (s[i] == p[j] || p[j] == '?')){
                i++; j++;
            }
            else if (j < n && p[j] == '*'){
                starj = j;
                j++;
                last_match = i;
            }
            else if (starj != -1){
                j = starj + 1;
                last_match++;
                i = last_match;
            }
            else return false;
        }
        while (p[j] == '*' && j <n) j++;
        return j == n;
        
//         // modified from regex (TOO SLOW ON LEETCODE 😡)
//         // recursive 
//         // base case (all pattern has been matched, check if string is empty)
//         if (p.size() == 0) return s.size() == 0;
//         if (s.size() == 0) return (p[0] == '*' && isMatch(s, p.substr(1)));
        
        
//         // this part does not account for star 
//         bool match = (s.size() != 0 && (s[0] == p[0] || p[0] == '?'));
        
//         if (p[0] == '*') {
//             // check star
//             // check 0 star matches then check remove the first star match
//             return isMatch(s.substr(1), p) || isMatch(s, p.substr(1));
//         } else {
//             // go to the next item if no stars
//             return match && isMatch(s.substr(1), p.substr(1));
//         }
    }
};