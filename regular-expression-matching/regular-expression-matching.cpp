class Solution {
public:
    bool isMatch(string s, string p) {
        // recursive 
        // base case (all pattern has been matched, check if string is empty)
        if (p.size() == 0) return s.size() == 0;
        
        // this part does not account for star 
        bool match = (s.size() != 0 && (s[0] == p[0] || p[0] == '.'));
        
        if (p.size() >= 2 && p[1] == '*') {
            // check star
            // check 0 star matches then check remove the first star match
            return isMatch(s, p.substr(2)) || (match && isMatch(s.substr(1), p));
        } else {
            // go to the next item if no stars
            return match && isMatch(s.substr(1), p.substr(1));
        }
        
//         does not account for Kleene star correctly
//         int index = 0;
//         for (int i = 0; i < s.size() && index < p.size(); i++) {
//             if (p[index] == '.') {
//                 index++;
//             } else if (p[index] == '*') {
//                 if (p[index-1] != '.') {
//                     while (p[index] == s[i]) {
//                         i++;
//                     }
//                     index++;
//                 } else {
//                     for (int j = i; j < s.size(); j++) {
//                         i++;
//                     }
//                     index++;
//                 }
//             } else {
//                 if (p[index] != s[i]) {
//                     return false;
//                 }
//                 index++;
//             }
//         }
        
//         // return if all of pattern p has been used
//         return index == p.size()-1;
    }
};