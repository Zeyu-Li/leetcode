class Solution {
public:
    int myAtoi(string s) {
        // separate into chucks
        // first chunck is trimming
        int ptr = 0;
        int sign = 1;
        long finalInt = 0;
        while (s[ptr] == ' ') {
            ptr++;
        }
        if (s[ptr] == '-' || s[ptr] == '+') {
            if (s[ptr] == '-') sign = -1;
            ptr++;
        }
        
        while (isdigit(s[ptr])) {
            if (INT_MAX / 10 < finalInt || (finalInt == INT_MAX / 10 && s[ptr] - '0' > 7)) {
                if (sign == 1) return INT_MAX;
                else return INT_MIN;
            }
            finalInt *= 10;
            finalInt += s[ptr] - '0';
            ptr++;
        }
        
        return finalInt * sign;
    }
};