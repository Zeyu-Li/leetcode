class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int max, current;
        max = 0;
        for (auto person : accounts) {
             current = 0;
            for (auto account : person) {
                current+=account;
            }
            if (current > max) {
                max = current;
            }
        }
        return max;
    }
};