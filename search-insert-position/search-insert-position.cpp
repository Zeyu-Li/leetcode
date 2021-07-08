class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        // alternative trival solution
        // return lower_bound(nums.begin(), nums.end(), target) - nums.begin();
        
        int top, mid, bottom;
        top = nums.size()-1;
        bottom = 0;
        while (bottom <= top) {
            mid = bottom + (top-bottom) / 2;
            if (nums[mid] < target) {
                bottom = mid+1; 
            } else {
                top = mid-1;
            }
        }
        
        return bottom;
    }
};