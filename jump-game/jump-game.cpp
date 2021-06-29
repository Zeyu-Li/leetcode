class Solution {
public:
    bool canJump(vector<int>& nums) {
        int currentMax = 0;
        // iterate greedily
        for (int reach = 0; currentMax < nums.size() && currentMax <= reach; ++currentMax) {
            reach = max(currentMax+nums[currentMax], reach);
        }
        
        return currentMax == nums.size();
    }
};