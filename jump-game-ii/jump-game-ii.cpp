class Solution {
public:
    int jump(vector<int>& nums) {
        vector<int> dp(nums.size(), INT_MAX-1); // (INT_MAX does not work)
        
        return traverse(nums, dp);
    }
    
    int traverse(vector<int>& nums, vector<int>& dp, int position = 0) {
        // once we reach the end we can stop 
        if (position >= nums.size() - 1)
            return 0;
        
        // already calculated so return dp solution
        if (dp[position] != INT_MAX-1) 
            return dp[position];
        
        // do dp in single array instead of matrix
        for (int i = 1; i <= nums[position]; i++) {
            dp[position] = min(dp[position], 1 + traverse(nums, dp, position+i));
        }
        
        return dp[position];
    }
};