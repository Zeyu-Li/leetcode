class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        vector<int> runningS(nums.size());
        int sum = 0;
        for (int i = 0; i < nums.size(); i++) {
            sum+=nums[i];
            runningS.push_back(sum);
        }
        return runningS;
    }
};