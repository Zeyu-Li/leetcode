class Solution {
public:
    bool isThree(int n) {
        if (n < 3) {
            return 0;
        }
        int count = 2;
        for (int i = 2; i < n && count <= 3; i++)
            count += n % i == 0;
        
        return count == 3;
    }
};